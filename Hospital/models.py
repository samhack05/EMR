"""

Created on Sun july 12 17:11:00 2020
@author: Ayush Saxena

"""

from django.contrib.auth.models import User
from django.db import models
from Patient.models import PatientRecord

class Licence(models.Model):
    Licence_number = models.AutoField(primary_key=True)
    Hospital_Name = models.CharField(max_length=60) #name of organization(Hospital name or clinic name)
    occupied = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    valid_till = models.DateTimeField()
    def save(self, *args, **kwargs):
        super(Licence, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.Licence_number)+' '+self.Hospital_Name

class Hospital(models.Model):
    Nodal_Person= models.ForeignKey(User, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Licence_number = models.ForeignKey(Licence, on_delete=models.DO_NOTHING)
    Nodal_Person_Designation = models.CharField(max_length=60)
    Nodal_Person_Email_ID = models.EmailField()
    Hospital_registration_No = models.AutoField(primary_key=True)
    Hospital_Name = models.CharField(max_length=60)
    Accreditation = models.CharField(max_length=60)
    Healthcare_Provider_Type = models.CharField(max_length=60)
    Registration_No_certificate = models.FileField(upload_to='govdocumentid')
    Hospital_Address = models.CharField(max_length=100)
    Hospital_State = models.CharField(max_length=60)
    Hospital_City = models.CharField(max_length=60)
    Hospital_Pincode = models.IntegerField()
    SPECIALTIES = models.CharField(max_length=500)
    AYUSH = models.CharField(max_length=100)
    Animal_Bite_Care = models.BooleanField(default=False)
    Poisoning_Centre_Cure = models.BooleanField(default=False)
    Rabies_Prevention_and_Care = models.BooleanField(default=False)
    Drug_De_Addiction = models.BooleanField(default=False)
    No_of_Doctors = models.IntegerField(blank=True)
    No_of_Medical_Consultants_or_Experts = models.IntegerField(blank=True)
    Total_No_of_Beds = models.IntegerField(blank=True)
    No_of_Private_Wards = models.IntegerField(blank=True)
    Emergency_Services = models.BooleanField(default=False)
    Mobile = models.BigIntegerField()
    Ambulance_Phone_no = models.BigIntegerField(blank=True)
    Blood_Bank_Phone_NO = models.BigIntegerField(blank=True)
    Foreign_Patient_Care_or_International_Patient_Wing = models.BooleanField(default=False)
    Toll_Free_No = models.BigIntegerField(blank=True)
    Helpline_no = models.BigIntegerField(blank=True)
    Hospital_Fax_No = models.BigIntegerField(blank=True)
    Hospital_Primary_Email_ID = models.EmailField(blank=True)
    Website = models.URLField(blank=True)
    Established_Year = models.IntegerField()
    Latitude = models.FloatField(blank=True)
    Longitude = models.FloatField(blank=True)
    def save(self, *args, **kwargs):
        super(Hospital, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.pk)+' '+self.Hospital_Name


class Doctor(models.Model):
    Doctoraccount = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile_no = models.BigIntegerField()
    additional_mobile_number = models.BigIntegerField()
    email = models.EmailField()
    specilization = models.CharField(max_length=50)
    licence_no = models.ForeignKey(Licence, blank=True, null=True, on_delete=models.DO_NOTHING,)
    Gender = models.CharField(max_length=1)
    address = models.CharField(max_length=60)
    City = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    Experiance_year = models.IntegerField()
    Hospital = models.ManyToManyField(Hospital, blank=True)
    Registration_Number = models.BigIntegerField()
    Registration_Council = models.CharField(max_length=30)
    Registration_Year = models.IntegerField()
    Registration_certificate = models.FileField(upload_to='govdocumentid')
    Government_ID_Proof = models.IntegerField()#1 for Aadhar Card, 2 for Driving Licence, 3 for Passport
    GovernmentIDNumber = models.CharField(max_length=18, unique=True)
    Document = models.FileField(upload_to='govdocumentid')
    def save(self, *args, **kwargs):
        super(Doctor, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.pk)+' '+self.first_name + ' ' + self.last_name

#
# class labtest(models.Model):
#     testname= models.CharField(max_length=50)
#     def save(self, *args, **kwargs):
#         super(labtest, self).save(*args, **kwargs)
#     def __str__(self):
#         return self.testname

class lab(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    PathologyName = models.CharField(max_length=80, unique=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    Designation= models.CharField(max_length=50)
    Address = models.CharField(max_length=80)
    PinCode = models.IntegerField()
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    ContactNo = models.BigIntegerField(unique=True)
    Email = models.EmailField(unique=True)
    Website = models.URLField(blank=True)
    open_at = models.TimeField()
    close_at = models.TimeField()
    WeeklyOff = models.IntegerField(blank=True) #0 for sunday 1 for monday
    Type_of_Test_Performed = models.CharField(max_length=140)
    Registration_Licence_No = models.CharField(max_length=20, unique=True)
    registration_Document = models.FileField(upload_to='govdocumentid')

    def save(self, *args, **kwargs):
        super(lab, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.pk)+self.PathologyName

class nurse(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    Address = models.CharField(max_length=80)
  #  Hospital_Name = models.ForeignKey(Hospital_staff_records) NOTE in view to add this in Hospital_staff_records
    PinCode = models.IntegerField(blank=True)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    ContactNo = models.BigIntegerField(unique=True)
    Email = models.EmailField(unique=True, blank=True)
    Government_ID_Proof = models.IntegerField()#1 for Aadhar Card, 2 for Driving Licence, 3 for Passport
    GovernmentIDNumber = models.CharField(max_length=18, unique=True)
    Document = models.FileField(upload_to='govdocumentid')

    def save(self, *args, **kwargs):
        super(nurse, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk) + self.firstname +' '+ self.lastname


class Hospital_staff_records(models.Model):
    Hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING)
    staff = models.ForeignKey(nurse, on_delete=models.DO_NOTHING)
    accepted = models.BooleanField(default=False)
    date_of_joining = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Hospital_staff_records, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk) + self.Hospital.Hospital_Name +' '+ self.staff.firstname +' ' + self.staff.lastname

from random import randrange

class HospitalCircle(models.Model):
    Hospitalref = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING)
    Patient = models.ForeignKey(PatientRecord, on_delete=models.DO_NOTHING)
    otp = models.CharField(max_length=20, default=randrange(100000, 999999))
    accepted = models.BooleanField(default=False)
    Timeofjoin = models.DateTimeField(blank=True)
    def save(self, *args, **kwargs):
        super(HospitalCircle, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.pk) +' '+ self.Hospitalref.Hospital_Name


class Hospital_labs_records(models.Model):
    Hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING)
    lab = models.ForeignKey(lab, on_delete=models.DO_NOTHING)
    accepted = models.BooleanField(default=False)
    date_of_joining = models.DateTimeField(blank=True)
    def save(self, *args, **kwargs):
        super(Hospital_labs_records, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.pk)+' '+self.Hospital.Hospital_Name +' ' + self.lab.PathologyName



class Doctors_staff_record(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    staff = models.ForeignKey(nurse, on_delete=models.DO_NOTHING)
    accepted = models.BooleanField(default=False)
    date_of_joining = models.DateTimeField()

    def save(self, *args, **kwargs):
        super(Doctors_staff_record, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk) + self.doctor.pk +' '+ self.staff.firstname +' ' + self.staff.lastname


class Hospital_Doctors_records(models.Model):
    Hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    accepted = models.BooleanField(default=False)
    date_of_joining = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Hospital_Doctors_records, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk) + self.Hospital.Hospital_Name +' '+ self.doctor.first_name +' ' + self.doctor.last_name


class LabCircle(models.Model):
    Labref = models.ForeignKey(lab, on_delete=models.DO_NOTHING)
    Patient = models.ForeignKey(PatientRecord, on_delete=models.DO_NOTHING)
    otp = models.CharField(max_length=20, default=randrange(100000, 999999))
    accepted = models.BooleanField(default=False)
    Timeofjoin = models.DateTimeField(blank=True)
    def save(self, *args, **kwargs):
        super(LabCircle, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.pk)

"""
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)
    is_labs = models.BooleanField(default=False)
    is_hospital = models.BooleanField(default=False)


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
class MyAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User Must Have an Email Address")
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        user = self.create_superuser(
            email=self.normalize_email(email),
            password=password
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)
    is_labs = models.BooleanField(default=False)
    is_hospital = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyAccountManager()
    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True
"""