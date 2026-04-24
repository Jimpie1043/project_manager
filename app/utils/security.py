from flask_talisman import Talisman

def init_security(app):
    Talisman(
        app,
        content_security_policy={
            "default-src": "'self'",
            "script-src": ["'self'"],
            "style-src": ["'self'", "'unsafe-inline'"],
            "img-src": ["'self'", "data:"]
        },
        
        force_https=app.config.get("FORCE_HTTPS", False),
        session_cookie_secure=app.config.get("SESSION_COOKIE_SECURE", False),
        session_cookie_http_only=app.config.get("SESSION_COOKIE_HTTPONLY", True)
    )