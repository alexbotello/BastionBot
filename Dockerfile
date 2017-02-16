# start from base
FROM python:3-onbuild
MAINTAINER Alexander Botello

# start app
CMD ["python", "bot.py"]
