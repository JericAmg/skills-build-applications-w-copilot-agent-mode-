import os
from django.contrib import admin
from django.urls import path, include

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

# Placeholder for DRF router and api_root (implementations should be in other files)
# from .views import api_root
# from .api import router

urlpatterns = [
    path('admin/', admin.site.urls),
    # Expose REST API endpoints under /api/ as required
    # path('api/', api_root, name='api-root'),
    # path('api/', include(router.urls)),
]
