#!/bin/bash

# build the bastionbot container
docker build -t bastion-bot .

# start the bastionbot container
docker run -it --rm --name BastionBot bastion-bot
