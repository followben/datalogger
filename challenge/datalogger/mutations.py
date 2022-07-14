import graphene
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from channels_redis.core import RedisChannelLayer

channel_layer: RedisChannelLayer = get_channel_layer()


class FeedStatusInput(graphene.InputObjectType):
    status = graphene.String(required=True)


class FeedStatusType(graphene.ObjectType):
    status = graphene.String()


class FeedStatusMutation(graphene.Mutation):
    class Arguments:
        input = FeedStatusInput(required=True)

    status = graphene.String()

    def mutate(root, _, input: FeedStatusType):
        if input.status not in ["on", "off"]:
            raise ValueError("Expected status of either 'on' or 'off'")
        async_to_sync(channel_layer.send)(
            "feed",
            {"type": "status.update", **input},
        )
        return input


class Mutation(graphene.ObjectType):
    toggle_feed = FeedStatusMutation.Field()
