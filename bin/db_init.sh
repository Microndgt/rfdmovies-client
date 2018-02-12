#!/bin/bash

BIN_DIR=$(dirname $0)
PROJECT_ROOT=$(perl -mCwd -e "print Cwd::abs_path('$BIN_DIR/..')")

get_config() {
    cd ${PROJECT_ROOT} >/dev/null 2>&1
    RESULT=$(python -c "from rfdmovie.config import get_config; print(get_config('$1') or \"\")" 2>/dev/null)
    cd - >/dev/null 2>&1
    echo ${RESULT}
}


DATA_DIR=${PROJECT_ROOT}/data/pg_data
USER=$(get_config "rfdmovie.postgresql.user")
DB_NAME=$(get_config "rfdmovie.postgresql.db_name")
PORT=$(get_config "rfdmovie.postgresql.port")
DB_HOST=$(get_config "rfdmovie.postgresql.host")

if [ -d /usr/lib/postgresql/9.4/bin ]; then
    export PATH=$PATH:/usr/lib/postgresql/9.4/bin
fi

if [ -d /usr/lib/postgresql/9.5/bin ]; then
    export PATH=$PATH:/usr/lib/postgresql/9.5/bin
fi

if [ -d /usr/lib/postgresql/9.6/bin ]; then
    export PATH=$PATH:/usr/lib/postgresql/9.6/bin
fi

if [ -d /usr/local/pgsql/bin ]; then
    export PATH=$PATH:/usr/local/pgsql/bin
fi

#mkdir -p ${DATA_DIR}

initdb -D ${DATA_DIR}
pg_ctl -D ${DATA_DIR} -l ${DATA_DIR}/postgresql.log start -o "-p ${PORT}"
echo "wait 2 seconds..."
sleep 2
# TODO check the process

createuser -s ${USER} -h ${DB_HOST} -p ${PORT}

echo "create database ${DB_NAME} encoding='utf-8' template=template0;" | psql -U ${USER} -h ${DB_HOST} -p ${PORT}
