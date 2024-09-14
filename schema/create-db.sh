#!/usr/bin/bash

DB_NAME="ta_dashboard"
DB_CREATE="CREATE DATABASE ${DB_NAME}"

echo "running ${DB_CREATE}"
psql -c "${DB_CREATE}" || exit 0