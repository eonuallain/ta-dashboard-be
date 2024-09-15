#!/usr/bin/bash

echo "running schema creation"

psql ./ta_dashboard_tables.sql
