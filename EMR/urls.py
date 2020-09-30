"""EMR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import logout_user, homepage, dashboard
from .views import cardiovascular,diabetes,liver,symtoms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('management/', include('Hospital.urls')),
    path('user/', include('Patient.urls')),
    path('logout/', logout_user, name="logout_user"),
    path('', homepage, name="homepage"),
    path('dashboard/', dashboard, name="dashboard"),

    path('cardio/', cardiovascular, name='cardio'),
    path('diabetes/', diabetes, name='diabetes'),
    path('liver/', liver, name='liver'),
    path('symtoms/', symtoms, name='symtoms'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
