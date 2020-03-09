#!/usr/bin/env bash

# acticate enviroment
. venv/bin/activate
APP=$1

case $APP in
  parent)
    PORT=8000;
    CERT_OPTIONS="--certfile certs/server.crt --keyfile certs/server.key --ca-certs certs/root_ca.pem"
    # CMD="python app_parent.py $PORT $CERT_OPTIONS"
    ;;
  child)
    export PARENT_BASE_URL="https://127.0.0.1:8000"
    PORT=7000;
    # CMD="flask run"
    ;;
  *)
    echo "app should be 'parent' or 'child'";
    exit 1;
    ;;
esac

echo "starting app" $APP " at port" $PORT;

export FLASK_RUN_PORT=$PORT
export FLASK_APP="app_${APP}:app"
export DATABASE_URL="postgres://postgres:postgres@127.0.0.1:5432/vma_${APP}"
# export FLASK_ENV=development
# $CMD
gunicorn --bind=0.0.0.0:$PORT --preload --workers=4 "app_${APP}:app" $CERT_OPTIONS
