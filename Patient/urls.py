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

from django.urls import path
from .views import PatientRegistration, PatientDashboard, Patientlogin
from .views import labreports, Medications, vitalinfo, billDisgrecords, DiseaseRecords, Insurance, PredictDisease, account
urlpatterns = [
    path('Registration/', PatientRegistration, name="PatientRegistration"),
    path('Login/', Patientlogin, name="Patientlogin"),
    path('Dashboard/', PatientDashboard, name="Dashboard"),

    path('account/', account, name="account"),
    path('labreports/', labreports, name="labreports"),
    path('Medications/', Medications, name="Medications"),
    path('vitalinfo/', vitalinfo, name="vitalinfo"),
    path('billDisgrecords/', billDisgrecords, name="billDisgrecords"),
    path('DiseaseRecords/', DiseaseRecords, name="DiseaseRecords"),
    path('Insurance/', Insurance, name="Insurance"),
    path('PredictDisease/', PredictDisease, name="PredictDisease"),


]
