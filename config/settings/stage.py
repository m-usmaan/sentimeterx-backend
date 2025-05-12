ALLOWED_HOSTS = ['api.demo.sentimeter.io']

# CSRF settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ['https://api.demo.sentimeter.io', 'https://*.demo.sentimeter.io']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# CORS settings
CORS_ALLOWED_ORIGINS = [
    'https://api.demo.sentimeter.io',
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    r'^https:\/\/.*\.demo\.sentimeter\.io$',
]
