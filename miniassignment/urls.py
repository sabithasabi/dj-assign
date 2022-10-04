"""miniassignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from demo.models import Signup
from demo.models import Signup2
from demo.forms import SignupForm
from demo.forms import SignupForm2
from demo.views import add
from demo.views import login
from demo.views import signin
from demo.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/",index ,name = 'read'),
    path('sign/',add),
    path('doctor/',signin),
    path('',login)
]
