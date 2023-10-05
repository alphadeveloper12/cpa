"""
URL configuration for cpa project.

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
from django.urls import path
from web.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('live-search/', live_search, name="search"),
    path('contact/', contact, name="contact"),
    path('privacy/', privacy, name="privacy"),
    path('blog/', all_blogs, name="blog"),
    path('offers/', all_links, name="offer"),
    path('blog/<slug:slug>/', BlogDetailView, name='blog-detail'),
    path('link/<slug:slug>/', cpa_detail, name='cpa-detail'),
    path('all-blogs-category-wise/', all_blogs_category_wise, name='all-blogs-category-wise'),
    path('all-blogs-category-wise/<slug:category_slug>/', all_blogs_category_wise, name='all-blogs-by-category'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
