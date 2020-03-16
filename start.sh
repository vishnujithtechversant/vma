#!/usr/bin/env bash

# acticate enviroment
. ~/Env/venv/bin/activate
APP=$1
PORT=$2

MIGRATE=0


echo "starting app" $APP " at port" $PORT;
CERT_OPTIONS="--certfile certs/server.crt --keyfile certs/server.key --ca-certs certs/root_ca.pem"
export PARENT_BASE_URL="https://127.0.0.1:8000"
export FLASK_RUN_PORT=$PORT
export FLASK_APP="app_parent:app"
export DATABASE_URL="postgres://postgres:postgres@127.0.0.1:5432/vma_${APP}"
case $APP in
  parent)
    export DATABASE_URL="postgres://postgres:postgres@127.0.0.1:5432/vma_parent"
    ;;
  *)
    export DATABASE_URL="postgres://postgres:postgres@127.0.0.1:5432/vma_child"
    ;;
esac
if [ $MIGRATE -eq 1 ]; then
  echo "Migrating database updates"
  flask db upgrade
fi

# export FLASK_ENV=development
# $CMD
gunicorn --bind=0.0.0.0:$PORT --preload --workers=4 "app_parent:app" $CERT_OPTIONS
