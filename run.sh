#!/bin/sh
set -ef
. bin/activate
cd bump
gunicorn -b 127.0.0.1:4000 init:app
