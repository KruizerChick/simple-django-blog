"""
Production settings for Family Tree on Heroku project.

- Use WhiteNoise for serving static files
- Use Amazon's S3 for storing uploaded media
- Use mailgun to send emails
- Use Redis for cache

- Use sentry for error logging
"""

import os
import logging

from .base import *  # noqa


# ADMIN CONFIGURATION
# ------------------------------------------------------------------------------
ENVIRONMENT_NAME = 'Production'
ENVIRONMENT_COLOR = '#dc4c4c'
