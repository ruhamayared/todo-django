#!/usr/bin/env bash

# Exit on error
set -o errexit

# Install dependencies
pip install -r dependencies.txt

# Run migrations in case any migrations hadn't been run yet
python manage.py migrate