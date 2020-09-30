"""
Created on Sun july 12 17:11:00 2020
@author: Ayush Saxena
"""

from django.contrib.auth.models import User
from django.db import models

#from Hospital.models import lab

class PatientRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    Email = models.EmailField(unique=True, blank=True)
    Address = models.CharField(max_length=80)
    PinCode = models.IntegerField(blank=True)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    ContactNo = models.BigIntegerField(unique=True)

    def save(self, *args, **kwargs):
        super(PatientRecord, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk) + self.user.username

class PatientBasicInfo(models.Model):
    Patient = models.ForeignKey(PatientRecord, on_delete=models.DO_NOTHING)
    Gender = models.CharField(max_length=1)  #0 MAle, 1 for Female, 2 for Transgender
    Fathers_id = models.BigIntegerField(blank=True, null=True)
    Mathers_id = models.BigIntegerField(blank=True, null=True)
    Bloodgroup = models.CharField(max_length=3, null=True)
    dateofbirth = models.DateField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    profilepic = models.ImageField(blank=True, upload_to='userimage', null=True, default="userimage/default-user-icon.png")
    MarriedStatus = models.BooleanField(blank=True, null=True)
    emergencyContact = models.BigIntegerField(blank=True, null=True)
    Government_ID_Proof = models.IntegerField(null=True) #   1 for Aadhar Card, 2 for Driving Licence, 3 for Passport
    GovernmentIDNumber = models.CharField(max_length=18, null=True, unique=True)
    Document = models.FileField(null=True, upload_to='govdocumentid')

    def save(self, *args, **kwargs):
        super(PatientBasicInfo, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk) + self.Patient.user.username + ' ' + str(self.GovernmentIDNumber)


class Patientlab_records(models.Model):
    Patient = models.ForeignKey(PatientRecord, on_delete=models.DO_NOTHING)
    testdate = models.DateField(auto_now_add=True)
    testname = models.CharField(max_length=60)
    testreport = models.FileField(upload_to='Patientreports')
    labid = models.IntegerField(null=True)
    def save(self, *args, **kwargs):
        super(Patientlab_records, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk) + self.testname


class PatientProblem(models.Model):
    Patient = models.ForeignKey(PatientRecord, on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)
    problem = models.CharField(max_length=30)
    problem_occur_date= models.DateField(auto_now_add=True, blank=True)
    problem_till_date= models.DateField(blank=True, null=True)
    addedby = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateadd = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        super(PatientProblem, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.pk) + self.Patient.Email + ' ' + self.problem

class PatientAllergy(models.Model):
    Patient = models.ForeignKey(PatientRecord, on_delete=models.DO_NOTHING)
    allergyname = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    allergy_occur_date = models.DateField(auto_now_add=True, blank=True)
    allergy_till_date = models.DateField(blank=True, null=True)
    allergy_level = models.CharField(max_length=5) #high, mid, low
    addedby = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateadd = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        super(PatientAllergy, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.pk) + self.Patient.Email + ' ' + self.allergyname

class PatientSymtoms(models.Model):
    Patient = models.ForeignKey(PatientRecord, on_delete=models.DO_NOTHING)
    symptom = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    occur_date = models.DateField(auto_now_add=True, blank=True)
    addedby = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateadd = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        super(PatientSymtoms, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.pk) + self.Patient.Email + ' ' + self.symptom


class PatientMedication(models.Model):
    Patient = models.ForeignKey(PatientRecord, on_delete=models.DO_NOTHING)
    medicinename = models.CharField(max_length=30)
    medicationcode = models.CharField(max_length=30, blank=True, null=True)
    direction = models.CharField(max_length=60)
    date_from = models.DateField(auto_now_add=True, blank=True)
    date_till = models.DateField(blank=True)
    addedby = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateadd = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        super(PatientMedication, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.pk) + self.Patient.Email + ' ' + self.medicinename


class PatientPrescription(models.Model):
    Patient = models.ForeignKey(PatientRecord, on_delete=models.DO_NOTHING)
    directions = models.CharField(max_length=200)
    date_from = models.DateField(auto_now_add=True, blank=True)
    date_till = models.DateField(blank=True)
    addedby = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateadd = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        super(PatientPrescription, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.pk) + self.Patient.Email + ' ' + self.addedby.username

class patientInsurance(models.Model):
    Patient = models.ForeignKey(PatientRecord, on_delete=models.DO_NOTHING)
    Insurancecertificate = models.FileField(upload_to='insurance')
    insurancecompany = models.CharField(max_length=25)
    fromdate = models.DateField()
    todate = models.DateField()

    def save(self, *args, **kwargs):
        super(patientInsurance, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk) + self.Patient.Email


class patientvitalinfo(models.Model):
    Patient = models.ForeignKey(PatientRecord, on_delete=models.DO_NOTHING)
    bodytemp = models.FloatField(blank=True)
    bpsys = models.IntegerField(blank=True)
    bpdia = models.IntegerField(blank=True)
    heartrate = models.IntegerField(blank=True)
    breathingrate = models.IntegerField(blank=True)
    dibetic = models.BooleanField(default=False)
    alcoholic = models.BooleanField(default=False)
    cigrate = models.BooleanField(default=False)
    bloodglucose = models.FloatField(blank=True)
    oxygensaturation = models.IntegerField(blank=True)
    other = models.CharField(max_length=20, blank=True)
    other2 = models.CharField(max_length=20, blank=True)
    addedby = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateadd = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        super(patientvitalinfo, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.pk) + self.Patient.Email + ' ' + self.addedby.username


class billingdetails(models.Model):
    Patient = models.ForeignKey(PatientRecord, on_delete=models.DO_NOTHING)
    Hospital = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateofbilling = models.DateTimeField(auto_now_add=True)
    billingpdf = models.FileField(upload_to='bills')
    billname=models.CharField(max_length=25)
    def save(self, *args, **kwargs):
        super(billingdetails, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.pk) + self.Patient.Email + ' ' + self.billname

class Dischargedetails(models.Model):
    Patient = models.ForeignKey(PatientRecord, on_delete=models.DO_NOTHING)
    Hospital = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateofbilling = models.DateTimeField(auto_now_add=True)
    Dischargepdf = models.FileField(upload_to='Dischargepapers')
    Dischargename=models.CharField(max_length=25)

    def save(self, *args, **kwargs):
        super(Dischargedetails, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk) + self.Patient.Email + ' ' + self.Dischargename

class Patientdisease(models.Model):
    Patient = models.ForeignKey(PatientRecord, on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)
    disease = models.CharField(max_length=30)
    disease_occur_date= models.DateField(auto_now_add=True, blank=True)
    disease_till_date= models.DateField(blank=True, null=True)
    addedby = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateadd = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        super(Patientdisease, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.pk) + self.Patient.Email + ' ' + self.disease