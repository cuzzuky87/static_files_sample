"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from app1.views import App1DifferentnameView as App1Diff
from app2.views import App2DifferentnameView as App2Diff

from app1.views import App1SamenameView as App1Same
from app2.views import App2SamenameView as App2Same

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/diff/',App1Diff.as_view()),
    path('app2/diff/',App2Diff.as_view()),
    path('app1/same/',App1Same.as_view()),
    path('app2/same/',App2Same.as_view()),
]
