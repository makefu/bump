# Bump
Bump is a minimalistic self-hosted pastebin.
It is written as a replacement for the gorgeous sprunge.us

## usage

    $ curl <host>
    Bump Usage:
    > echo balls | curl -F "p=<-" <host>
    <   http://<host>/q9a1bfljzm
    > curl <host>/q9a1bfljzm
    <   balls
    Source at http://github.com/makefu/bump

## Install

    virtualenv .
    . bin/activate
    pip install -r deps.txt

## Startup

    . bin/activate
    cd bump
    ./run.sh

## Configure nginx
    
    $EDITOR etc/bump.nginx.conf
    cp etc/bump.nginx.conf /etc/nginx/conf.d

## Configure supervisor

    $EDITOR etc/bump.supervisor.conf
    cp etc/bump.supervisor.conf /etc/supervisor/conf.d/bump.conf

## License

Copyright Felix Richter. All code is under WTFPL, see COPYING
