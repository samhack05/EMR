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
from .views import HospitalRegistration, DoctorRegistration, labRegistration, NurseRegistration, Hospitallogin, HospitalDashboard, PatientInfoLab, DoctorHospitalCircleRecords, createPatient
from .views import DoctorDashboard, NurseDashboard, LabDashboard, Doctorlogin, Nurselogin, Lablogin, PatientInfo, PatientInfoDoc, PatientInfoNurse, NurseHospitalCircleRecords
urlpatterns = [
    path('HospitalRegistration/', HospitalRegistration, name="HospitalRegistration"),
    path('DoctorRegistration/', DoctorRegistration, name="DoctorRegistration"),
    path('LabRegistration/', labRegistration, name="LabRegistration"),
    path('NurseRegistration/', NurseRegistration, name="LabRegistration"),

    path('LoginHospital/', Hospitallogin, name="LoginHospital"),

    path('Doctorlogin/', Doctorlogin, name="Doctorlogin"),
    path('Nurselogin/', Nurselogin, name="Nurselogin"),
    path('Lablogin/', Lablogin, name="Lablogin"),

    path('HospitalDashboard/', HospitalDashboard, name="HospitalDashboard"),
    path('DoctorDashboard/', DoctorDashboard, name="DoctorDashboard"),


    path('NurseDashboard/', NurseDashboard, name="NurseDashboard"),
    path('LabDashboard/', LabDashboard, name="LabDashboard"),

    path('HospitalDashboard/', HospitalDashboard, name="HospitalDashboard"),
    path('HospitalDashboard/<int:pk>/<str:username>/', HospitalDashboard, name="HospitalDashboard"),

    path('PatientInfo/<int:pk>/', PatientInfo, name="PatientInfo"),

    path('PatientInfoDoc/<int:pk>/', PatientInfoDoc, name="PatientInfoDoc"),
    path('PatientInfoDoc/<int:pk>/<int:type>', PatientInfoDoc, name="PatientInfoDoc"),
    path('PatientInfoDoc/<int:pk>/<int:type>/<int:id>', PatientInfoDoc, name="PatientInfoDoc"),


    path('PatientInfoNurse/<int:pk>/', PatientInfoNurse, name="PatientInfoNurse"),
    path('PatientInfoNurse/<int:pk>/<int:c>', PatientInfoNurse, name="PatientInfoNurse"),
    path('PatientInfoNurse/<int:pk>/<int:c>/<str:data>/', PatientInfoNurse, name="PatientInfoNurse"),

    path('PatientInfoLab/<int:pk>/', PatientInfoLab, name="PatientInfoLab"),

    path('DoctorHospitalCircleRecords/', DoctorHospitalCircleRecords, name="DoctorHospitalCircleRecords"),

    path('NurseHospitalCircleRecords/', NurseHospitalCircleRecords, name="NurseHospitalCircleRecords"),

    path('createPatient/', createPatient, name="createPatient"),

]
