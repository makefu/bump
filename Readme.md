# Bump
Bump is a minimalistic self-hosted pastebin.
It is written as a replacement for the gorgeous sprunge.us

# usage

## Install

    virtualenv .
    . bin/activate
    pip install -r deps.txt

## Startup

    . bin/activate
    cd bump
    gunicorn -b 127.0.0.1:4000 init:app
