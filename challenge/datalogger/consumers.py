import asyncio
import json
import logging
import os

import websockets as ws
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from challenge.datalogger.models import TemperatureReading

logger = logging.getLogger(__name__)


@database_sync_to_async
def process_data(data):
    value = data.get("payload").get("data").get("temperature")
    if value is not None:
        reading = TemperatureReading.objects.create(value=value)
        logging.info(f"Saved {reading}")
    else:
        logger.warn(f"Could not find payload.data.temperature in {data}")


async def monitor():
    uri = f"ws://{os.getenv('WS_HOST', 'localhost')}:{os.getenv('WS_PORT', 1000)}/graphql"
    start = {"type": "start", "payload": {"query": "subscription { temperature }"}}
    logging.debug(f"Connecting to {uri}")
    async for websocket in ws.connect(uri, subprotocols=["graphql-ws"]):
        logging.debug(f"Sending message {start}")
        await websocket.send(json.dumps(start))
        try:
            async for payload in websocket:
                data = json.loads(payload)
                await process_data(data)
        except ws.ConnectionClosed:
            logger.warn("Connection lost. Retrying...")
            continue  # retry connection with exponential backoff


class FeedConsumer(AsyncConsumer):
    task = None

    async def status_update(self, message):
        if message["status"] not in ["on", "off"]:
            raise ValueError(f"Cannot process status.update of {message}")

        logger.debug(f"Received status.update of {message}")
        enable = message["status"] == "on"
        if enable and (not self.task or self.task.cancelled()):
            self.task = asyncio.create_task(monitor())
        elif self.task and not enable:
            self.task.cancel()
