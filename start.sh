#!/usr/bin/env bash

# acticate enviroment
. venv/bin/activate
APP=$1

case $APP in
  parent)
    PORT=8000;
    ;;
  child)
    export PARENT_BASE_URL="http://localhost:8000"
    PORT=7000;
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
export FLASK_ENV=development
flask run
#gunicorn --bind=0.0.0.0:8000 --workers=4 "app_${APP}:app
