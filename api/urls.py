"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from api.accounts import urls as accounts_urls
from api.chats import urls as chats_urls
from api.chats.views import DataSetsAPIView, DatasetFiltersView


all_patterns = [
    path(r'accounts/', include(accounts_urls)),
    path(r'chats/', include(chats_urls)),
    path('data-sets/', DataSetsAPIView.as_view()),
    path('data-sets/<str:dataset_id>/filters/', DatasetFiltersView.as_view()),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/', include(all_patterns))
]
