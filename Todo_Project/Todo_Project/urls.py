"""Todo_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from application import views
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home.as_view()),
    path("login/",views.log_in.as_view()),
    path('logout/',views.log_out.as_view()),
    path('login/',views.log_in.as_view()),
    path("addworks/<wrk>/",views.addworks.as_view(),name="wrk"),
    path("decisions/<email>/<No>/",views.decision.as_view(),name="decision"),
    path("update/<No>/",views.update.as_view(),name="update"),
    path("delete/<remove>/",views.delete.as_view(),name="delete"),
]

router=routers.SimpleRouter()
router.register("crud",views.Datas)
urlpatterns = urlpatterns + router.urls

# router.register("addwork",views.addwork)