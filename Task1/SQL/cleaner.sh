#!/bin/bash


docker-compose stop
docker rm psqlContainer
rm -r dump/*
