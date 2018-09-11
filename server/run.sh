#!/usr/bin/env bash
export FLASK_APP=server/main.py
export FLASK_ENV=development
export FLASK_RUN_PORT=3020

python3 -m flask run