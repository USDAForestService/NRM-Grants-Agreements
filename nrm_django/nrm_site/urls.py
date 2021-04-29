"""nrm_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path

from nrm_app.views import HomePageView
from grants.views import GrantCreateView

urlpatterns = [
    # because these URLs will resolve first, they effectively override the admin URLs
    re_path(
        "admin/(?P<app_label>grants)/grant/add/$",
        GrantCreateView.as_view(),
        name="add-grant",
    ),
    # Now we can have the regular admin URLs
    path("admin/", admin.site.urls),
    path("", HomePageView.as_view(), name="home"),
]
