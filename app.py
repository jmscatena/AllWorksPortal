import os
import logging
from flask import Flask
from flask_wtf.csrf import CSRFProtect

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default-dev-key-replace-in-production")

# Enable CSRF protection
csrf = CSRFProtect(app)

# Import routes after the app is created to avoid circular imports
from routes import *  # noqa: E402, F403
