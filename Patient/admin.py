"""
Created on Sun july 12 17:11:00 2020
@author: Ayush Saxena
"""

from django.contrib import admin
from .models import PatientRecord, PatientBasicInfo, patientvitalinfo, patientInsurance, billingdetails, Dischargedetails, Patientdisease
from .models import PatientPrescription, PatientMedication, PatientSymtoms, PatientAllergy, PatientProblem, Patientlab_records
# Register your models here.

admin.site.register(PatientRecord)
admin.site.register(PatientBasicInfo)
admin.site.register(patientvitalinfo)
admin.site.register(patientInsurance)
admin.site.register(PatientPrescription)
admin.site.register(PatientMedication)
admin.site.register(PatientSymtoms)
admin.site.register(PatientAllergy)
admin.site.register(PatientProblem)
admin.site.register(Patientlab_records)
admin.site.register(billingdetails)
admin.site.register(Dischargedetails)
admin.site.register(Patientdisease)