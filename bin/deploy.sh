#!/bin/bash
if [ $# -eq 0 ]
then
    echo "Usage: deploy.sh <env>"
    exit 1
fi

case $1 in
    local)
        cp config.local.ini config.ini
        ;;
    *)
        echo "$1 is not a recognized environment"
esac
