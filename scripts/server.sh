#!/bin/bash

if [ -z "$VIRTUAL_ENV" ]; then   
    virtualenv -p ~/.pyenv/versions/3.6.3/bin/python venv
	. venv/bin/activate
fi

pip install -r requirements/server.txt
moto_server -H swf.aws.local
