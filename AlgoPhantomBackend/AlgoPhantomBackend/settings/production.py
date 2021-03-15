from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240