"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from apps.custom_admin.admin import custom_admin_site


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('custom/', custom_admin_site.urls),

    #include
    path('', include('apps.settings.urls')),
    path('product/', include('apps.products.urls')),
    path('cart/', include('apps.carts.urls')),
    path('billing/', include('apps.billing.urls')),
    path('menu/', include('apps.tables.urls')),
    path('user/', include('apps.users.urls')),
    path('category/', include('apps.categories.urls')),

    #users
    path('logout/', LogoutView.as_view(next_page = 'index'), name = "logout"),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)