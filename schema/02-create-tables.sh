#!/usr/bin/bash

echo "running inserts"

sudo -u postgres -i

psql -U postgres -d ta_dashboard -a -f ./ta_dashboard_insert.sql
