
"""
Created on Sun july 12 17:11:00 2020
@author: Ayush Saxena
"""

from django.contrib import admin
from .models import Hospital, Licence, Doctor, lab, nurse, Hospital_staff_records, Hospital_labs_records, Hospital_Doctors_records, Doctors_staff_record, HospitalCircle, LabCircle

admin.site.register(LabCircle)
admin.site.register(HospitalCircle)
admin.site.register(Hospital)
admin.site.register(Licence)
admin.site.register(Doctor)
admin.site.register(lab)
admin.site.register(nurse)
admin.site.register(Hospital_staff_records)
admin.site.register(Hospital_Doctors_records)
admin.site.register(Doctors_staff_record)
admin.site.register(Hospital_labs_records)