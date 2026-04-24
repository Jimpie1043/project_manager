import os

class Config:
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_HTTPONLY = True

    # Both true only in production
    SESSION_COOKIE_SECURE = os.getenv('ENVIRONMENT') == 'production'
    FORCE_HTTPS = os.getenv('ENVIRONMENT') == 'production'