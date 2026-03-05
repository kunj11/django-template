# django-template

## Using Django Rest Framework
1. Define models
2. Define serializers
3. Define views
4. Define urls
    - use router
5. Include app urls in project urls
    - path('', include(app.urls))
6. Add the apps name in settings
    - INSTALLED_APPS = [
        'app',
        'rest_framework'
    ]