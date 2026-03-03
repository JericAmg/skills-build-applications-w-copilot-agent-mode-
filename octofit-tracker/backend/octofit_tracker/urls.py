import os
from django.contrib import admin
from django.urls import path, include

# Example api_root and router import (replace with actual imports in your project)
# from .views import api_root
# from .api import router

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

urlpatterns = [
    path('admin/', admin.site.urls),
    # Uncomment and update the following lines as you implement api_root and router
    # path('api/', api_root, name='api-root'),
    # path('api/', include(router.urls)),
]
