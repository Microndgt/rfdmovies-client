#!/bin/bash

BIN_DIR=$(dirname $0)
PROJECT_ROOT=$(perl -mCwd -e "print Cwd::abs_path('$BIN_DIR/..')")

get_config() {
    cd ${PROJECT_ROOT} >/dev/null 2>&1
    RESULT=$(python -c "from rfdmovie.config import get_config; print(get_config('$1') or \"\")" 2>/dev/null)
    cd - >/dev/null 2>&1
    echo ${RESULT}
}


USER=$(get_config "rfdmovie.postgresql.user")
DB_NAME=$(get_config "rfdmovie.postgresql.db_name")
PORT=$(get_config "rfdmovie.postgresql.port")
DB_HOST=$(get_config "rfdmovie.postgresql.host")

echo "alembic -c misc/db-migrations/alembic.ini -n rfdmovie -x dburl=postgresql+psycopg2://${USER}@${DB_HOST}:${PORT}/${DB_NAME} upgrade head"
alembic -c migrations/alembic.ini -n rfdmovie -x dburl=postgresql+psycopg2://${USER}@${DB_HOST}:${PORT}/${DB_NAME} downgrade -1