#!/bin/bash

# Определение среды
ENVIRONMENT=${1:-dev}

# Копирование соответствующего .env-файла
cp ".env.$ENVIRONMENT" .env

# Запуск docker-compose
podman-compose up --build