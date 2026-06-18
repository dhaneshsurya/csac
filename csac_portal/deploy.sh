#!/bin/bash

# Exit immediately if any command fails
set -e

echo "======================================"
echo " Starting CSAC Portal Deployment"
echo "======================================"

# 1. Pull latest code from GitHub
echo "1. Pulling latest updates from GitHub..."
git pull origin main

# 2. Activate virtual environment if using a venv
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# 3. Install dependencies
echo "2. Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# 4. Run migrations
echo "3. Applying database migrations..."
python manage.py migrate

# 5. Collect static files
echo "4. Collecting static files..."
python manage.py collectstatic --noinput

# 6. Restart Server (uncomment/adjust based on your server setup, e.g. Gunicorn/Nginx)
# echo "5. Restarting application server..."
# sudo systemctl restart gunicorn

echo "======================================"
echo " Deployment Completed Successfully! "
echo "======================================"
