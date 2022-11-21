# datalogger

Consumes a temperature feed and implements a GraphQL API to query the processed data.

## Quick start

Ensure docker is running & you have docker compose

```
# start all containers
docker compose up

# setup the django admin
docker compose run web python manage.py createsuperuser
```

The following GraphQL queries and mutations are then available at `http://localhost:8080/graphql`:

```graphql
# get the latest temperature reading
query {
  currentTemperature {
    timestamp
    value
  }
}

# get min and max temperature in a window
query {
  temperatureStatistics(
    after: "2020-12-06T12:00:00+00:00"
    before: "2020-12-07T12:00:00+00:00"
  ) {
    min
    max
  }
}

# turn the feed off or on
mutation {
  toggleFeed(input: { status: "on" }) {
    status
  }
}
```

## What is this?

A sample backend created in early 2021 as part of a coding challenge. It's a little out of date now, but still demonstrates the use of [Django](https://www.djangoproject.com), [Channels](https://channels.readthedocs.io/en/stable/) and [Graphene-Django](https://docs.graphene-python.org/projects/django/en/latest/) to build a GraphQL api.

If this were real I'd:

- action deployment checklist, incl. secret and turn off debug (https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/)
- switch channels to use Redis (https://channels.readthedocs.io/en/stable/topics/channel_layers.html#redis-channel-layer)
- implement a BRIN index or use a Timeseries db (e.g. Timescale)
- pin docker image version and convert to an unprivileged conatiner and run docker rootless (https://docs.docker.com/engine/security/rootless/) or use podman
- deploy the monitor in it's own container
- run under hypercorn beind a reverse proxy like nginx
- deploy on app runnner or k8s
- use secrets rather than env for database secrets
- monitoring
- volume test
- structured logging

## To do:

- ~~move off graphene-django (it's no longer maintained)~~ migrate to graphene-django v3.0.0
- improve documentation
- use pytest for testing
- CI/ CD incl. tests and linting for mypy etc.
- Return the real status of the feed rather than echoing the mutated one
- Use an enum for feed status (embarrassed to say I was a bit stumped by string enums at the time)
- Use pydantic to load & validate env vars and (de)serialize messages
