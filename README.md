# Quick start

Ensure docker is running & you have docker compose

```
# start all containers
docker compose up

# setup the django admin
docker compose run web python manage.py createsuperuser
```

# To do

- better docs
- pytest
- CI/ CD incl. tests and linting for mypy, flake8
- Subscription to rolling average
- Frontend

# Highlights

- choice of image (https://pythonspeed.com/articles/base-image-python-docker-images/)
- use of multistage build (needed gcc for channels/ redis)
- use of custom command for monitor
- use of channels to communicate monitor to subscribers

# To Productionise

- Action deployment checklist, incl. secret and turn off debug (https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/)
- Switch channels to use Redis (https://channels.readthedocs.io/en/stable/topics/channel_layers.html#redis-channel-layer)
- Pin docker image version
- Run under uvicorn beind a reverse proxy like nginx
- Deploy on app runnner or k8s
- use secrets rather than env for database secrets
- Monitoring
- Volume test
- Structured logging

# Possible Enhancements

- Move off graphene-django (it's no longer maintained)
- Return the real status of the feed rather than echoing the mutated one
- Use an enum for feed status (embarrassed to say I was a bit stumped by string enums)
- Use pydantic to load & validate env vars and (de)serialize messages
- BRIN index or use a Timeseries db (e.g. Timescale)
- Convert to an unprivileged conatiner and run docker rootless (https://docs.docker.com/engine/security/rootless/) or use podman
- Deploy the monitor in it's own container
