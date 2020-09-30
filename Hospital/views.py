from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Hospital, Licence, Doctor, Hospital_Doctors_records, lab, nurse, HospitalCircle, Hospital_staff_records, Hospital_labs_records, LabCircle
from Patient.models import PatientRecord, PatientBasicInfo, billingdetails, Dischargedetails, patientInsurance, PatientAllergy, PatientPrescription, Patientdisease
from Patient.models import PatientPrescription, PatientMedication, patientvitalinfo, PatientProblem, PatientSymtoms, Patientlab_records, PatientMedication
from random import randrange
from datetime import datetime
from django.core.paginator import Paginator
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import matplotlib.pyplot as plt
import numpy as np

from EMR.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import joblib
medicinearr = joblib.load('medicinearr.pkl')

def HospitalRegistration(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        First_name = request.POST.get('firstname')
        Last_name = request.POST.get('lastname')
        Licence_number = request.POST.get('license')
        Nodal_Person_Designation = request.POST.get('nodaldesignation')
        Nodal_Person_Email_ID = request.POST.get('email')
        Hospital_Name = request.POST.get('hospitalname')
        Accreditation = request.POST.get('accreditation')
        Healthcare_Provider_Type = request.POST.get('type')
        Registration_No_certificate = request.FILES['registrationno']
        Hospital_Address = request.POST.get('address')
        Hospital_State = request.POST.get('state')
        Hospital_City = request.POST.get('city')
        Hospital_Pincode = request.POST.get('pincode')
        SPECIALTIES = ','.join([request.POST.get(str(i)+'optradio') for i in range(1, 57) if request.POST.get(str(i)+'optradio')])
        AYUSH = request.POST.get('optradio1')
        Animal_Bite_Care = request.POST.get('optradioanimal')
        Poisoning_Centre_Cure = request.POST.get('optradiopoisoning')
        Rabies_Prevention_and_Care = request.POST.get('optradiorabies')
        Drug_De_Addiction = request.POST.get('optradiodrug')
        No_of_Doctors = request.POST.get('nosdoctor')
        No_of_Medical_Consultants_or_Experts = request.POST.get('nmce')
        Total_No_of_Beds = request.POST.get('nosbed')
        No_of_Private_Wards = request.POST.get('ward')
        Mobile = request.POST.get('mobile')
        Emergency_no = request.POST.get('emergency')
        Ambulance_Phone_no = request.POST.get('ambulance')
        Blood_Bank_Phone_NO = request.POST.get('bloodbank')
        Foreign_Patient_Care_or_International_Patient_Wing = request.POST.get('')
        Toll_Free_No = request.POST.get('toll')
        Helpline_no = request.POST.get('helpline')
        Hospital_Fax_No = request.POST.get('fax')
        Website = request.POST.get('hospwebsite')
        Established_Year = request.POST.get('year')
        Latitude = 1234454
        Longitude = 1234454
        lno=None
        if Licence_number:
             try:
                 lno = Licence.objects.filter(pk=Licence_number, Hospital_Name=Hospital_Name, occupied=True, active=True).first()
             except Licence.DoesNotExist:
                 print('Oaky')
                 return HttpResponse("<html><body><h1>Invalid Licence Number or Incorrect Clinic/Hospital Name</h1></body></html>")
        if username and password and lno:
            user = User.objects.create_user(username=username,
                                            email=Nodal_Person_Email_ID,
                                            password=password)
            user.save()
            obj = Hospital.objects.create(Nodal_Person=user, First_name=First_name, Licence_number=lno,
                                          Last_name=Last_name, Website=Website, Established_Year=Established_Year,
                                          Healthcare_Provider_Type=Healthcare_Provider_Type, Hospital_Fax_No=Hospital_Fax_No,
                                          Hospital_Primary_Email_ID=username, Latitude=Latitude,
                                          Longitude=Longitude, Helpline_no=Helpline_no, Toll_Free_No=Toll_Free_No,
                                          Blood_Bank_Phone_NO=Blood_Bank_Phone_NO, Ambulance_Phone_no=Ambulance_Phone_no,
                                          Mobile=Mobile,
                                          No_of_Private_Wards=No_of_Private_Wards,
                                          Total_No_of_Beds=Total_No_of_Beds, No_of_Medical_Consultants_or_Experts=No_of_Medical_Consultants_or_Experts,
                                          No_of_Doctors=No_of_Doctors, Drug_De_Addiction=Drug_De_Addiction, Rabies_Prevention_and_Care=Rabies_Prevention_and_Care,
                                          Nodal_Person_Designation=Nodal_Person_Designation, Accreditation=Accreditation, Registration_No_certificate=Registration_No_certificate,
                                          Hospital_Address=Hospital_Address, Hospital_State=Hospital_State,
                                          Hospital_City=Hospital_City, Hospital_Pincode=Hospital_Pincode, SPECIALTIES=SPECIALTIES,
                                          AYUSH=AYUSH, Poisoning_Centre_Cure=Poisoning_Centre_Cure,
                                          Animal_Bite_Care=Animal_Bite_Care)
            obj.save()
            lno.occupied = False
            lno.save()
            return HttpResponse("<html><body><h1>Account Created</h1></body></html>")
        return HttpResponseRedirect('/')
    return render(request=request,
                  template_name="HospitallRegistration.html",
                  context={})



def DoctorRegistration(request, *args, **kwargs):
    if request.method == 'POST':
        First_name = request.POST.get('firstname')
        Last_name = request.POST.get('lastname')
        password = request.POST.get('password')
        Mobile_number = request.POST.get('mobile')
        Additional_mobile_number = request.POST.get('amobile')
        Email_id=request.POST.get('email')
        Specialization=request.POST.get('sp')
        Gender=request.POST.get('ge')
        Address=request.POST.get('address')
        City=request.POST.get('city')
        State=request.POST.get('state')
        Experience_year=request.POST.get('year')
        Registration_no=request.POST.get('reg')
        Registration_council=request.POST.get('regc')
        Registration_year=request.POST.get('regy')
        Hospitalname = request.POST.get('hospname')
        licence_no= request.POST.get('license')
        Registration_certificate= request.FILES['cert']
        Government_ID_Proof= request.POST.get('proof')
        GovernmentIDNumber= request.POST.get('govid')
        Document= request.FILES['doc']
        flag=0
        objHosp=None
        lno=None
        if Hospitalname:
            objHosp = Hospital.objects.get(pk=int(Hospitalname))
            flag = 1
        elif licence_no:
            try:
                lno = Licence.objects.filter(pk=licence_no, occupied=True, active=True).first()
                flag = 2
            except Licence.DoesNotExist:
                return HttpResponse("<html><body><h1>Invalid Licence Number or Licence Number is Expired</h1></body></html>")
        if flag:
            user = User.objects.create_user(username=Email_id,
                                            email=Email_id,
                                            password=password, first_name=First_name, last_name=Last_name)
            if user:
                objDoctor = Doctor.objects.create(Doctoraccount=user, first_name=First_name, last_name=Last_name,
                                                 mobile_no=Mobile_number, additional_mobile_number=Additional_mobile_number,
                                                 email=Email_id, specilization=Specialization,
                                                 Gender=Gender, address=Address, City=City,
                                                 state=State, Experiance_year=Experience_year,
                                                 Registration_Number=Registration_no,
                                                 Registration_Council=Registration_council, Registration_Year=Registration_year,
                                                 Registration_certificate=Registration_certificate, Government_ID_Proof=Government_ID_Proof,
                                                 GovernmentIDNumber=GovernmentIDNumber, Document=Document)
                objDoctor.save()

                if flag==1:
                    objDoctor.Hospital.add(objHosp)
                    objDoctor.save()
                    hospitalrecordsobj = Hospital_Doctors_records.objects.create(Hospital=objHosp, doctor=objDoctor)
                    hospitalrecordsobj.save()
                    return HttpResponse("<html><body><h1>Account Created-  You Get Access after Hospital Accept Your Request</h1></body></html>")
                elif flag==2:
                    objDoctor.licence_no = lno
                    objDoctor.save()
                    lno.occupied = False
                    lno.save()
                    return HttpResponse("<html><body><h1>Account Created</h1></body></html>")
            else:
                return HttpResponse("<html><body><h1>Username/Email Already Used</h1></body></html>")
    obj = Hospital.objects.all()
    arr={}
    for ob in obj:
        arr[ob.pk]=ob.Hospital_Name
    return render(request=request,
                  template_name="doctorRegistration.html",
                  context={'arr': arr})




def labRegistration(request, *args, **kwargs):
    if request.method == 'POST':
        Pathology_name=request.POST.get('pathology')
        First_name = request.POST.get('firstname')
        Last_name = request.POST.get('lastname')
        password = request.POST.get('password')
        Designation=request.POST.get('des')
        Address=request.POST.get('address')
        City = request.POST.get('city')
        Pincode = request.POST.get('pincode')
        State = request.POST.get('state')
        Contact_no=request.POST.get('mobile')
        Email_id=request.POST.get('email')
        Website=request.POST.get('hospwebsite')
        open_at=request.POST.get('open')
        close_at = request.POST.get('close')
        weeklyof= request.POST.get('off')
        Test=','.join([request.POST.get('test'+str(i)) for i in range(1, 11) if request.POST.get('test'+str(i))])
        Registration_no=request.POST.get('reg')
        Registration_certificate = request.POST.get('doc')
        print(Test)
        user = User.objects.create_user(username=Email_id,
                                        email=Email_id,
                                        password=password, first_name=First_name, last_name=Last_name)
        if user:
            objlab = lab.objects.create(user=user,PathologyName=Pathology_name,
                                        firstname = First_name,
                                        lastname = Last_name,
                                        Designation = Designation,
                                        Address = Address,
                                        PinCode = Pincode,
                                        City = City,
                                        State = State,
                                        ContactNo = Contact_no,
                                        Email = Email_id,
                                        Website = Website,
                                        open_at = open_at,
                                        close_at = close_at,
                                        WeeklyOff = weeklyof,
                                        Registration_Licence_No= Registration_no, Type_of_Test_Performed=Test,
                                        registration_Document= Registration_certificate)
            objlab.save()
            return HttpResponse("<html><body><h1>Account Created</h1></body></html>")
        else:
            return HttpResponse("<html><body><h1>Username/Email Already Used</h1></body></html>")
    return render(request=request,
                  template_name="labregistration.html",
                  context={})
def NurseRegistration(request, *args, **kwargs):
    if request.method == 'POST':
        First_Name = request.POST.get('firstname')
        Last_name = request.POST.get('lastname')
        password = request.POST.get('password')
        ContactNo = request.POST.get('mobile')
        Address = request.POST.get('address')
        City = request.POST.get('city')
        Pincode = request.POST.get('pincode')
        State = request.POST.get('state')
        Email = request.POST.get('email')
        Government_ID_Proof = request.POST.get('proof')
        GovernmentIDNumber = request.POST.get('govid')
        Document = request.POST.get('doc')

        user = User.objects.create_user(username=Email,
                                        email=Email,
                                        password=password, first_name=First_Name, last_name=Last_name)
        if user:
            objnurse = nurse.objects.create(user=user,
                                        firstname=First_Name,
                                        lastname=Last_name,
                                        Address= Address,
                                        PinCode = Pincode,
                                        City = City,
                                        State = State,
                                        ContactNo = ContactNo,
                                        Email = Email,
                                        Government_ID_Proof = Government_ID_Proof,
                                        GovernmentIDNumber = GovernmentIDNumber,
                                        Document = Document)
            objnurse.save()
            return HttpResponse("<html><body><h1>Account Created</h1></body></html>")
        else:
            return HttpResponse("<html><body><h1>Username/Email Already Used</h1></body></html>")
    return render(request=request,
                  template_name="nurseRegistration.html",
                  context={})

def Hospitallogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                objHospitalRecord = Hospital.objects.get(Nodal_Person=user)
            except Hospital.DoesNotExist:
                objHospitalRecord = None
                logout(request)
                return HttpResponseRedirect('/')
            if objHospitalRecord is not None:
                messages.info(request, f"You are now logged in as {username}")
                return HttpResponseRedirect('/management/HospitalDashboard/')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        messages.error(request, "Invalid username or password.")

    return render(request=request,
                  template_name="login_hospital.html",
                  context={})

def Doctorlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                objDoctorRecord = Doctor.objects.get(Doctoraccount=user)
            except Doctor.DoesNotExist:
                objDoctorRecord = None
                logout(request)
                return HttpResponseRedirect('/')
            if objDoctorRecord is not None:
                messages.info(request, f"You are now logged in as {username}")
                print("great")
                return HttpResponseRedirect('/management/DoctorDashboard/')
        else:
            messages.error(request, "Invalid username or password.")
            print("Invalid username or password. this")
    else:
        messages.error(request, "Invalid username or password.")
        print("Invalid username or password.")
    return render(request=request,
                  template_name="login_Doctor.html",
                  context={})


def Nurselogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                objnurseRecord = nurse.objects.get(user=user)
            except nurse.DoesNotExist:
                objnurseRecord = None
            if objnurseRecord is not None:
                messages.info(request, f"You are now logged in as {username}")
                return HttpResponseRedirect('/management/NurseDashboard/')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        messages.error(request, "Invalid username or password.")

    return render(request=request,
                  template_name="login_nurse.html",
                  context={})


def Lablogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                objlabRecord = lab.objects.get(user=user)
            except lab.DoesNotExist:
                objlabRecord = None
            if objlabRecord is not None:
                messages.info(request, f"You are now logged in as {username}")
                return HttpResponseRedirect('/management/LabDashboard/')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        messages.error(request, "Invalid username or password.")

    return render(request=request,
                  template_name="login_lab.html",
                  context={})


def SearchPatient(username=None, mobno=None, UID=None, PUID=None):
    if username:
        try:
            objpatient = PatientRecord.objects.get(Email=username)
        except PatientRecord.DoesNotExist:
            return False
        return objpatient
    if mobno:
        try:
            objpatient=PatientRecord.objects.get(ContactNo=mobno)
        except PatientRecord.DoesNotExist:
            return False
        return objpatient
    if UID:
        try:
            objpatient=PatientBasicInfo.objects.get(GovernmentIDNumber=UID)
        except PatientBasicInfo.DoesNotExist:
            return False
        return objpatient.Patient
    if PUID:
        try:
            objpatient=PatientBasicInfo.objects.get(Fathers_id=PUID)
        except PatientBasicInfo.DoesNotExist:
            objpatient=None
        if objpatient:
            return objpatient.Patient
        try:
            objpatient = PatientBasicInfo.objects.get(Mathers_id=PUID)
        except PatientBasicInfo.DoesNotExist:
            return False
        if objpatient:
            return objpatient.Patient

from datetime import timedelta
from django.utils import timezone

def removefromcircle(HospitalCircle_list):
    time_threshold = timezone.now()
    for rec in HospitalCircle_list:
        if (rec.Timeofjoin + timedelta(days=5)) < time_threshold:
            rec.delete()

@login_required()
def otpverfication(request, hospitalcircleobj):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if hospitalcircleobj.otp == otp:
            hospitalcircleobj.accepted=True
            hospitalcircleobj.save()
            return HttpResponseRedirect('/management/HospitalDashboard/')

    return render(request=request,
                  template_name="otpverfication.html",
                  context={})
@login_required()
def HospitalDashboard(request, username=None, pk=None):
    optrequired=None
    Hospitalobj = None
    rPatient=None
    try:
        Hospitalobj = Hospital.objects.get(Nodal_Person=request.user)
    except Hospital.DoesNotExist:
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")
    if pk==1 or pk==2:
        c=username[0]
        username = username[1:]
        #print(username, c)
        if c=='1':
            rPatient=SearchPatient(UID=int(username))
        if c == '2':
            rPatient=SearchPatient(PUID=int(username))
        if c == '3':
            rPatient=SearchPatient(username=username)
        if c == '4':
            rPatient=SearchPatient(mobno=int(username))
        if(rPatient):
            if pk==1:

                HospitalCircleobj = HospitalCircle.objects.create(Hospitalref=Hospitalobj,
                                                                  Patient=rPatient,
                                                                  otp=randrange(100000, 999999),
                                                                  Timeofjoin=datetime.now())
                HospitalCircleobj.save()
                subject = ' OTP to share Your Medical Records with' + Hospitalobj.Hospital_Name + ' Hospital for next 5 Days'
                message = ' Hospital : ' + Hospitalobj.Hospital_Name + '  Address :  ' + Hospitalobj.Hospital_Address + ' ' + Hospitalobj.Hospital_City + ' has Requested your Medical Records'
                message += ' To add your Records in Hospital Circle for Next 5 days share your OTP with Hospital Staff'
                message += 'OTP { '+ str(HospitalCircleobj.otp) + ' } '

                recepient = rPatient.Email
                send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
                return otpverfication(request, HospitalCircleobj)
            if pk == 2:
                HospitalCircleobj = HospitalCircle.objects.create(Hospitalref=Hospitalobj,
                                                                  Patient=rPatient,
                                                                  otp=randrange(100000, 999999),
                                                                  Timeofjoin=datetime.now(), accepted=True)
                HospitalCircleobj.save()
                subject = ' In Case of Emergency Your Medical Records are Shared with '+ Hospitalobj.Hospital_Name + ' Hospital for next 5 Days'
                message = ' Due to any Emergency Hospital : ' + Hospitalobj.Hospital_Name +'  Address :  ' + Hospitalobj.Hospital_Address + '  ' + Hospitalobj.Hospital_City + ' has Requested your Medical Records'
                message += ' your Records are successfully add in Hospital Circle for Next 5 days'
                recepient = rPatient.Email
                send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
                return HttpResponseRedirect('/management/HospitalDashboard/')
    if pk==3:
        objrecorddoctor = Hospital_Doctors_records.objects.get(pk=int(username))
        objrecorddoctor.accepted = True
        objrecorddoctor.date_of_joining = datetime.now()
        objrecorddoctor.save()
    if pk==4:
        Hospital_Doctors_records.objects.get(pk=int(username)).delete()
    if pk==5:
        objrecordstaff = Hospital_staff_records.objects.get(pk=int(username))
        objrecordstaff.accepted = True
        objrecordstaff.date_of_joining = datetime.now()
        objrecordstaff.save()
    if pk==6:
        Hospital_staff_records.objects.get(pk=int(username)).delete()
    if pk==7:
        objrecordlab = Hospital_labs_records.objects.get(pk=int(username))
        objrecordlab.accepted = True
        objrecordlab.date_of_joining = datetime.now()
        objrecordlab.save()
    if pk==8:
        Hospital_labs_records.objects.get(pk=int(username)).delete()

    HospitalCircle_list = HospitalCircle.objects.filter(Hospitalref=Hospitalobj)
    removefromcircle(HospitalCircle_list)

    HospitalCircle_list = HospitalCircle.objects.filter(Hospitalref=Hospitalobj)
    paginator = Paginator(HospitalCircle_list, 10)
    page_number = request.GET.get('HospitalCircle_list_page')
    page_obj = paginator.get_page(page_number)

    objHospital_Doctors_records = Hospital_Doctors_records.objects.filter(Hospital=Hospitalobj, accepted=False)
    paginator2 = Paginator(objHospital_Doctors_records, 3)
    page_number2 = request.GET.get('Doctors_records_list_page')
    page_obj2 = paginator2.get_page(page_number2)

    objHospital_staff_records = Hospital_staff_records.objects.filter(Hospital=Hospitalobj, accepted=False)
    paginator3 = Paginator(objHospital_staff_records, 3)
    page_number3 = request.GET.get('staff_records_list_page')
    page_obj3 = paginator3.get_page(page_number3)

    objHospital_lab_records = Hospital_labs_records.objects.filter(Hospital=Hospitalobj, accepted=False)
    paginator4 = Paginator(objHospital_lab_records, 3)
    page_number4 = request.GET.get('lab_records_list_page')
    page_obj4 = paginator4.get_page(page_number4)
    doccount = Hospital_Doctors_records.objects.filter(Hospital=Hospitalobj, accepted=True).count()
    Doctors_records = Hospital_Doctors_records.objects.filter(Hospital=Hospitalobj, accepted=True)
    staffcount = Hospital_staff_records.objects.filter(Hospital=Hospitalobj, accepted=True).count()
    staff_records = Hospital_staff_records.objects.filter(Hospital=Hospitalobj, accepted=True)
    Labcounts= Hospital_labs_records.objects.filter(Hospital=Hospitalobj, accepted=True).count()
    lab_records = Hospital_labs_records.objects.filter(Hospital=Hospitalobj, accepted=True)

    return render(request=request,
                  template_name="HospitalDashboard.html",
                  context={'optrequired': optrequired,
                           'Hospitalobj': Hospitalobj,
                           'page_obj': page_obj,
                           'page_obj2': page_obj2,
                           'page_obj3': page_obj3,
                           'page_obj4': page_obj4,
                           'Doctors_records': Doctors_records,
                           'staff_records': staff_records,
                           'lab_records': lab_records,
                           'doccount': doccount,
                           'staffcount': staffcount,
                           'Labcounts': Labcounts})


@login_required()
def PatientInfo(request, pk):
    try:
        Hospitalobj = Hospital.objects.get(Nodal_Person=request.user)
    except Hospital.DoesNotExist:
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")
    Patientobj = PatientRecord.objects.get(pk=pk)
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        filename = request.POST.get('filename')
        type = request.POST.get('type')
        if type==1 or type=='1':
            billingdetailsobj = billingdetails.objects.create(Patient=Patientobj,
                                                              Hospital=request.user,
                                                              billingpdf=file,
                                                              billname=filename)
            billingdetailsobj.save()
        if type==2 or type=='2':
            Dischargedetailsobj = Dischargedetails.objects.create(Patient=Patientobj,
                                                              Hospital=request.user,
                                                              Dischargepdf=file,
                                                              Dischargename=filename)
            Dischargedetailsobj.save()
    try:
        Hospitalobj = Hospital.objects.get(Nodal_Person=request.user)
    except Hospital.DoesNotExist:
        Hospitalobj = None
    if Hospitalobj:
        try:
            hospitalobjCircle = HospitalCircle.objects.get(Hospitalref=Hospitalobj, Patient=Patientobj)
        except HospitalCircle.DoesNotExist:
            hospitalobjCircle = None
        if hospitalobjCircle:
            objPatientBasicInfo = PatientBasicInfo.objects.get(Patient=Patientobj)
            objbilling = billingdetails.objects.filter(Patient=Patientobj, Hospital=request.user).order_by('-dateofbilling')
            paginator = Paginator(objbilling, 5)
            page_number = request.GET.get('bill_records_list_page')
            page_obj = paginator.get_page(page_number)
            objDischargedetails = Dischargedetails.objects.filter(Patient=Patientobj, Hospital=request.user).order_by('-dateofbilling')
            paginator2 = Paginator(objDischargedetails, 5)
            page_number2 = request.GET.get('bill_records_list_page')
            page_obj2 = paginator2.get_page(page_number2)
            patientInsuranceobj = patientInsurance.objects.filter(Patient=Patientobj).order_by('-todate')
            PatientPrescriptionobj = PatientPrescription.objects.filter(Patient=Patientobj).order_by('-date_from')
            #PatientMedicationobj = PatientMedication.objects.filter(Patient=Patientobj).order_by('-date_from')
            if(len(patientInsuranceobj)==0):
                patientInsuranceobj=None
                patientInsuranceobjimg=None
            else:
                patientInsuranceobjimg = patientInsuranceobj[0].Insurancecertificate
            if (len(PatientPrescriptionobj) == 0):
                PatientPrescriptionobj = None
            else:
                PatientPrescriptionobj=PatientPrescriptionobj[0]
            return render(request=request, template_name="PatientInfo.html", context={'objPatientBasicInfo': objPatientBasicInfo,
                                                                                      'Patientobj': Patientobj,
                                                                                      'hospitalobjCircle': hospitalobjCircle,
                                                                                      'page_obj': page_obj, 'page_obj2': page_obj2,
                                                                                      'patientInsuranceobj': patientInsuranceobj,
                                                                                      'PatientPrescriptionobj': PatientPrescriptionobj,
                                                                                      'patientInsuranceobjimg': patientInsuranceobjimg,
                                                                                      })
    return render(request=request,
                  template_name="PatientInfo.html", context={})
def plotgraph(x,y):
    # setting the x - coordinates
    x = np.arange(0, 2 * (np.pi), 0.1)
    # setting the corresponding y - coordinates
    y = np.sin(x)

    # potting the points
    plt.plot(x, y)

    # function to show the plot
    plt.show()

@login_required()
def DoctorDashboard(request,):
    try:
        Doctorobj = Doctor.objects.get(Doctoraccount=request.user)
    except Doctor.DoesNotExist:
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")
    Hospital_Doctors_recordsobj = Hospital_Doctors_records.objects.filter(doctor=Doctorobj, accepted=True)
    data=[]
    for rec in Hospital_Doctors_recordsobj:
        HospitalCircleobj = HospitalCircle.objects.filter(Hospitalref=rec.Hospital, accepted=True)

        for p in HospitalCircleobj:
            data.append(p.Patient)


    return render(request=request,
                  template_name="DoctorDashboard.html",
                  context={'data': data})

def geneticdisease(Patientrecord, tree):
    genetic = []
    geneticdiseasearr=['high blood pressure', 'diabetes', 'cystic fibrosis', 'down syndrome','hair loss', 'Cancer', 'asthma', 'tay sachs', 'thalassemia','Single Gene Disorders', 'sickle cell anemia', 'thalassemia']
    if Patientrecord:
        Patientdiseaseobj = Patientdisease.objects.filter(Patient=Patientrecord)
        genetic+=[rec.disease+' - '+tree for rec in Patientdiseaseobj if rec.disease.lower() in geneticdiseasearr]
        try:
            objPatientBasicInfo = PatientBasicInfo.objects.get(Patient=Patientrecord)
        except PatientBasicInfo.DoesNotExist:
            objPatientBasicInfo = None
        if objPatientBasicInfo is not None:
            if objPatientBasicInfo.Fathers_id is not None:
                try:
                    objPatientBasicInfo1 = PatientBasicInfo.objects.get(GovernmentIDNumber=objPatientBasicInfo.Fathers_id)
                except PatientBasicInfo.DoesNotExist:
                    objPatientBasicInfo1=None
                if objPatientBasicInfo1:
                    genetic += geneticdisease(objPatientBasicInfo1.Patient, tree+'F')
            if objPatientBasicInfo.Mathers_id is not None:
                try:
                    objPatientBasicInfo2 = PatientBasicInfo.objects.get(GovernmentIDNumber=objPatientBasicInfo.Mathers_id)
                except PatientBasicInfo.DoesNotExist:
                    objPatientBasicInfo2=None
                if objPatientBasicInfo2:
                    genetic += geneticdisease(objPatientBasicInfo2.Patient, tree+'M')
    return genetic

@login_required()
def PatientInfoDoc(request, pk, type=None, id=None):
    hrate=''
    dia=''
    sys=''
    glucose=''
    oxy=''
    btemp=''
    brate=''
    date=''
    if type==1 and id:
        ruf = PatientProblem.objects.get(pk=id)
        ruf.is_active = False
        ruf.save()
        return redirect('/management/PatientInfoDoc/'+str(pk))
    if type==2 and id:
        ruf = PatientSymtoms.objects.get(pk=id)
        ruf.is_active = False
        ruf.save()
        return redirect('/management/PatientInfoDoc/'+str(pk))
    if type==3 and id:
        ruf = Patientdisease.objects.get(pk=id)
        ruf.is_active = False
        ruf.save()
        return redirect('/management/PatientInfoDoc/'+str(pk))
    try:
        Doctorobj = Doctor.objects.get(Doctoraccount=request.user)
    except Doctor.DoesNotExist:
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")
    Patientobj = PatientRecord.objects.get(pk=pk)
    data = []
    Hospital_Doctors_recordsobj = Hospital_Doctors_records.objects.filter(doctor=Doctorobj, accepted=True)
    f=0
    for rec in Hospital_Doctors_recordsobj:
        HospitalCircleobj = HospitalCircle.objects.filter(Hospitalref=rec.Hospital, accepted=True)
        for p in HospitalCircleobj:
            data.append(p.Patient)
            if p.Patient.pk == pk:
                f=1
    if f==0:
        return HttpResponse("<html><body><h1>You are not authorized to Access this Record</h1></body></html>")


    if request.method == 'POST':
        formno = request.POST.get('formno')
        if formno == '1':
            height = request.POST.get('height')
            weight = request.POST.get('weight')
            objPatientBasicInfo = PatientBasicInfo.objects.get(Patient=Patientobj)
            objPatientBasicInfo.height =height
            objPatientBasicInfo.weight =weight
            objPatientBasicInfo.save()
        if formno=='2':
            btemp= request.POST.get('temp')
            bpsys= request.POST.get('bp')
            bpdia= request.POST.get('dia')
            hrate= request.POST.get('hrate')
            brate= request.POST.get('brate')
            bg= request.POST.get('bg')
            oxy= request.POST.get('oxy')
            Diabetic= True if request.POST.get('1')=='1' else False
            Alcoholic= True if request.POST.get('2')=='1' else False
            smoking= True if request.POST.get('3')=='1' else False
            other= request.POST.get('other')
            other1= request.POST.get('other1')
            patientvitalinfoobjruf = patientvitalinfo.objects.create(Patient=Patientobj,
                                                                    bodytemp=btemp,
                                                                    bpsys =bpsys,
                                                                    bpdia =bpdia,
                                                                    heartrate =hrate,
                                                                    breathingrate =brate,
                                                                    dibetic =Diabetic,
                                                                    alcoholic =Alcoholic,
                                                                    cigrate =smoking,
                                                                    bloodglucose =bg,
                                                                    oxygensaturation =oxy,
                                                                    other =other,
                                                                    other2 =other1,
                                                                    addedby =request.user,
                                                                    )
            patientvitalinfoobjruf.save()
            #find_record(Patientobj.pk)
        if formno=='3':
            prob = request.POST.get('prob')
            PatientProblemobjruf = PatientProblem.objects.create(
                Patient=Patientobj,
                problem=prob,
                addedby=request.user)
            PatientProblemobjruf.save()
        if formno == '4':
            symp = request.POST.get('symp')
            PatientSymtomsobjruf = PatientSymtoms.objects.create(
                Patient=Patientobj,
                symptom=symp,
                addedby=request.user
            )
            PatientSymtomsobjruf.save()
        if formno == '5':
            customRadioallergy = request.POST.get('customRadioallergy')
            allergy = request.POST.get('allergy')
            PatientAllergyruf = PatientAllergy.objects.create(
                Patient= Patientobj,
                allergyname = allergy,
                allergy_level = customRadioallergy,
                addedby = request.user,
            )
            PatientAllergyruf.save()
        if formno == '6':
            pres = request.POST.get('pres')
            fro = request.POST.get('fro')
            till = request.POST.get('till')
            PatientPrescriptionruf =  PatientPrescription.objects.create(
                Patient=Patientobj,
                directions = pres,
                date_from = fro,
                date_till = till,
                addedby = request.user,
            )
            PatientPrescriptionruf.save()
        if formno == '7':
            medname= request.POST.get('medname')
            medcode= request.POST.get('medcode')
            direc= request.POST.get('direc')
            from1= request.POST.get('from1')
            till1= request.POST.get('till1')
            PatientMedicationruf = PatientMedication.objects.create(
                Patient= Patientobj,
                medicinename = medname,
                medicationcode = medcode,
                direction = direc,
                date_from = from1,
                date_till = till1,
                addedby = request.user,
            )
            PatientMedicationruf.save()
        if formno == '8':
            Diseasename = request.POST.get('Diseasename')
            Patientdiseaseruf = Patientdisease.objects.create(
                Patient=Patientobj,
                disease=Diseasename,
                addedby=request.user)
            Patientdiseaseruf.save()
    objPatientBasicInfo = PatientBasicInfo.objects.get(Patient=Patientobj)
    PatientProblemobj = PatientProblem.objects.filter(Patient=Patientobj).order_by('-is_active')
    PatientSymtomsobj = PatientSymtoms.objects.filter(Patient=Patientobj).order_by('-is_active')
    try:
        patientvitalinfoobj = patientvitalinfo.objects.filter(Patient=Patientobj).order_by('-dateadd')
        if len(patientvitalinfoobj):
            patientvitalinfall = patientvitalinfoobj
            patientvitalinfoobj = patientvitalinfoobj[0]
            for val in patientvitalinfall[15::-1]:
                hrate += str(val.heartrate)+' '
                dia += str(val.bpdia)+' '
                sys += str(val.bpsys)+' '
                glucose += str(val.bloodglucose)+' '
                oxy += str(val.oxygensaturation)+' '
                btemp += str(val.bodytemp)+' '
                brate += str(val.breathingrate)+' '
                date += val.dateadd.strftime("%d/%b")+' '
    except patientvitalinfo.DoesNotExist:
        patientvitalinfoobj = None
        patientvitalinfall = None

    paginator = Paginator(PatientProblemobj, 10)
    page_number= request.GET.get('patient_list_page')
    PatientProblemobj = paginator.get_page(page_number)

    paginator2 = Paginator(PatientSymtomsobj, 10)
    page_number2 = request.GET.get('patient_list_page2')
    PatientSymtomsobj = paginator2.get_page(page_number2)

    Patientlab_recordsobj = Patientlab_records.objects.filter(Patient=Patientobj).order_by('-testdate')
    paginator3 = Paginator(Patientlab_recordsobj, 5)
    page_number3 = request.GET.get('patient_list_page3')
    Patientlab_recordsobj = paginator3.get_page(page_number3)

    PatientAllergyobj = PatientAllergy.objects.filter(Patient=Patientobj, is_active=True).order_by('-dateadd')
    paginator4 = Paginator(PatientAllergyobj, 5)
    page_number4 = request.GET.get('patient_list_page4')
    PatientAllergyobj = paginator4.get_page(page_number4)

    PatientPrescriptionobj = PatientPrescription.objects.filter(Patient=Patientobj).order_by('-date_till')
    paginator5 = Paginator(PatientPrescriptionobj, 1)
    page_number5 = request.GET.get('patient_list_page5')
    PatientPrescriptionobj = paginator5.get_page(page_number5)

    PatientMedicationnobj = PatientMedication.objects.filter(Patient=Patientobj).order_by('-dateadd')
    paginator6 = Paginator(PatientMedicationnobj, 5)
    page_number6 = request.GET.get('patient_list_page6')
    PatientMedicationnobj = paginator6.get_page(page_number6)

    Patientdiseaseobj = Patientdisease.objects.filter(Patient=Patientobj).order_by('-is_active')
    paginator7 = Paginator(Patientdiseaseobj, 10)
    page_number7 = request.GET.get('patient_list_page7')
    Patientdiseaseobj = paginator7.get_page(page_number7)

    geneticdiseaserec = geneticdisease(Patientobj, 'P')
    print(geneticdiseaserec)
    return render(request=request,
                  template_name="PatientInfoDoctor.html", context={'PatientProblemobj': PatientProblemobj,
                                                                   'patientvitalinfoobj': patientvitalinfoobj,
                                                                   'Patientobj': Patientobj,
                                                                   'objPatientBasicInfo': objPatientBasicInfo,
                                                                   'PatientSymtomsobj': PatientSymtomsobj,
                                                                   'Patientlab_recordsobj': Patientlab_recordsobj,
                                                                   'PatientAllergyobj': PatientAllergyobj,
                                                                   'PatientPrescriptionobj': PatientPrescriptionobj,
                                                                   'PatientMedicationnobj': PatientMedicationnobj,
                                                                   'Patientdiseaseobj': Patientdiseaseobj,
                                                                   'geneticdiseaserec': geneticdiseaserec,
                                                                   'medicinearr': medicinearr,
                                                                   'hrate': hrate,'dia': dia,'sys': sys,'glucose': glucose,'oxy': oxy,'btemp': btemp,'brate': brate, 'date': date})
def find_record(patientid):
    hrate=[]
    bp1=[]
    bp2=[]
    Blood_Glucose=[]
    Oxygen_Saturation=[]
    daterec=[]
    patientrec = PatientRecord.objects.get(pk=patientid)
    if patientvitalinfo.objects.filter(Patient=patientrec).count() >2:
        patientvitalinfoobj = patientvitalinfo.objects.filter(Patient=patientrec).order_by('-dateadd')[:20]
        for rec in patientvitalinfoobj:
            date = rec.dateadd.strftime("%Y-%m-%d %H:%M:%S")
            hrate.append(rec.heartrate)
            bp1.append(rec.bpsys)
            bp2.append(rec.bpdia)
            Blood_Glucose.append(rec.bloodglucose)
            Oxygen_Saturation.append(rec.oxygensaturation)
            daterec.append(date)
        x = daterec
        plt.style.use('ggplot')
        plt.title('Vital Info Visualization')
        plt.xlabel('Date Time')
        plt1 = plt.subplot2grid((11, 2), (0, 0), rowspan=4, colspan=2)
        plt2 = plt.subplot2grid((11, 2), (4, 0), rowspan=4, colspan=2)
        plt3 = plt.subplot2grid((11, 2), (8, 0), rowspan=4, colspan=2)
        plt1.plot(x, hrate, label='Heart Rate', color='b')
        plt2.plot(x, Blood_Glucose, label='Blood Glucose', color='r')
        plt3.plot(x, Oxygen_Saturation, label='Oxygen Saturation', color='g')
        plt1.legend()
        plt2.legend()
        plt3.legend()
        plt.gcf().autofmt_xdate()
        plt.savefig('media/graph/'+str(patientid)+'.png')
        plt.close()

        plt.style.use('ggplot')
        plt4 = plt.subplot2grid((11, 1), (0, 0), rowspan=6, colspan=2)
        plt4.plot(x, bp1, label='SYS', color='m')
        plt4.plot(x, bp2, label='DIA', color='y')
        plt4.legend()
        plt.title('Blood Pressure Visualization')
        plt.xlabel('Date Time')
        plt.gcf().autofmt_xdate()
        plt.savefig('media/graph/sysdia' + str(patientid) + '.png')
        plt.close()
        return




@login_required()
def NurseDashboard(request):
    try:
        Nurseobj = nurse.objects.get(user=request.user)
    except nurse.DoesNotExist:
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")

    Hospital_staff_recordsobj = Hospital_staff_records.objects.filter(staff=Nurseobj, accepted=True)
    data=[]
    for rec in Hospital_staff_recordsobj:
        HospitalCircleobj = HospitalCircle.objects.filter(Hospitalref=rec.Hospital, accepted=True)
        for p in HospitalCircleobj:
            data.append(p.Patient)

    return render(request=request,
                  template_name="NurseDashboard.html",
                  context={'data':data})


@login_required()
def PatientInfoNurse(request, pk, type=None, id=None):
    if type==1 and id:
        ruf = PatientProblem.objects.get(pk=id)
        ruf.is_active = False
        ruf.save()
        return redirect('/management/PatientInfoDoc/'+str(pk))
    if type==2 and id:
        ruf = PatientSymtoms.objects.get(pk=id)
        ruf.is_active = False
        ruf.save()
        return redirect('/management/PatientInfoDoc/'+str(pk))
    try:
        Nurseobj = nurse.objects.get(user=request.user)
    except nurse.DoesNotExist:
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")
    Patientobj = PatientRecord.objects.get(pk=pk)
    data = []
    Hospital_staff_recordsobj = Hospital_staff_records.objects.filter(staff=Nurseobj, accepted=True)
    f=0
    for rec in Hospital_staff_recordsobj:
        HospitalCircleobj = HospitalCircle.objects.filter(Hospitalref=rec.Hospital, accepted=True)
        for p in HospitalCircleobj:
            data.append(p.Patient)
            if p.Patient.pk == pk:
                f=1
    if f==0:
        return HttpResponse("<html><body><h1>You are not authorized to Access this Record</h1></body></html>")


    if request.method == 'POST':
        formno = request.POST.get('formno')
        if formno == '1':
            height = request.POST.get('height')
            weight = request.POST.get('weight')
            objPatientBasicInfo = PatientBasicInfo.objects.get(Patient=Patientobj)
            objPatientBasicInfo.height =height
            objPatientBasicInfo.weight =weight
            objPatientBasicInfo.save()
        if formno=='2':
            btemp= request.POST.get('temp')
            bpsys= request.POST.get('bp')
            bpdia= request.POST.get('dia')
            hrate= request.POST.get('hrate')
            brate= request.POST.get('brate')
            bg= request.POST.get('bg')
            oxy= request.POST.get('oxy')
            Diabetic= True if request.POST.get('1')=='1' else False
            Alcoholic= True if request.POST.get('2')=='1' else False
            smoking= True if request.POST.get('3')=='1' else False
            other= request.POST.get('other')
            other1= request.POST.get('other1')
            patientvitalinfoobjruf = patientvitalinfo.objects.create(Patient=Patientobj,
                                                                    bodytemp=btemp,
                                                                    bpsys =bpsys,
                                                                    bpdia =bpdia,
                                                                    heartrate =hrate,
                                                                    breathingrate =brate,
                                                                    dibetic =Diabetic,
                                                                    alcoholic =Alcoholic,
                                                                    cigrate =smoking,
                                                                    bloodglucose =bg,
                                                                    oxygensaturation =oxy,
                                                                    other =other,
                                                                    other2 =other1,
                                                                    addedby =request.user,
                                                                    )
            patientvitalinfoobjruf.save()
            find_record(Patientobj.pk)
        if formno=='3':
            prob = request.POST.get('prob')
            PatientProblemobjruf = PatientProblem.objects.create(
                Patient=Patientobj,
                problem=prob,
                addedby=request.user)
            PatientProblemobjruf.save()
        if formno == '4':
            symp = request.POST.get('symp')
            PatientSymtomsobjruf = PatientSymtoms.objects.create(
                Patient=Patientobj,
                symptom=symp,
                addedby=request.user
            )
            PatientSymtomsobjruf.save()
        if formno == '5':
            customRadioallergy = request.POST.get('customRadioallergy')
            allergy = request.POST.get('allergy')
            PatientAllergyruf = PatientAllergy.objects.create(
                Patient= Patientobj,
                allergyname = allergy,
                allergy_level = customRadioallergy,
                addedby = request.user,
            )
            PatientAllergyruf.save()


    objPatientBasicInfo = PatientBasicInfo.objects.get(Patient=Patientobj)
    PatientProblemobj = PatientProblem.objects.filter(Patient=Patientobj).order_by('-is_active')
    PatientSymtomsobj = PatientSymtoms.objects.filter(Patient=Patientobj).order_by('-is_active')
    try:
        patientvitalinfoobj = patientvitalinfo.objects.filter(Patient=Patientobj).order_by('-dateadd')
        if len(patientvitalinfoobj):
            patientvitalinfoobj = patientvitalinfoobj[0]
    except patientvitalinfo.DoesNotExist:
        patientvitalinfoobj = None


    paginator = Paginator(PatientProblemobj, 10)
    page_number= request.GET.get('patient_list_page')
    PatientProblemobj = paginator.get_page(page_number)

    paginator2 = Paginator(PatientSymtomsobj, 10)
    page_number2 = request.GET.get('patient_list_page2')
    PatientSymtomsobj = paginator2.get_page(page_number2)

    Patientlab_recordsobj = Patientlab_records.objects.filter(Patient=Patientobj).order_by('-testdate')
    paginator3 = Paginator(Patientlab_recordsobj, 5)
    page_number3 = request.GET.get('patient_list_page3')
    Patientlab_recordsobj = paginator3.get_page(page_number3)

    PatientAllergyobj = PatientAllergy.objects.filter(Patient=Patientobj, is_active=True).order_by('-dateadd')
    paginator4 = Paginator(PatientAllergyobj, 5)
    page_number4 = request.GET.get('patient_list_page4')
    PatientAllergyobj = paginator4.get_page(page_number4)

    PatientPrescriptionobj = PatientPrescription.objects.filter(Patient=Patientobj).order_by('-date_till')[:5]
    paginator5 = Paginator(PatientPrescriptionobj, 1)
    page_number5 = request.GET.get('patient_list_page5')
    PatientPrescriptionobj = paginator5.get_page(page_number5)

    PatientMedicationnobj = PatientMedication.objects.filter(Patient=Patientobj).order_by('-dateadd')
    paginator6 = Paginator(PatientMedicationnobj, 5)
    page_number6 = request.GET.get('patient_list_page6')
    PatientMedicationnobj = paginator6.get_page(page_number6)

    Patientdiseaseobj = Patientdisease.objects.filter(Patient=Patientobj).order_by('-is_active')
    paginator7 = Paginator(Patientdiseaseobj, 10)
    page_number7 = request.GET.get('patient_list_page7')
    Patientdiseaseobj = paginator7.get_page(page_number7)


    return render(request=request,
                  template_name="PatientInfoNurse.html", context={'PatientProblemobj': PatientProblemobj,
                                                                   'patientvitalinfoobj': patientvitalinfoobj,
                                                                   'Patientobj': Patientobj,
                                                                   'objPatientBasicInfo': objPatientBasicInfo,
                                                                   'PatientSymtomsobj': PatientSymtomsobj,
                                                                   'Patientlab_recordsobj': Patientlab_recordsobj,
                                                                   'PatientAllergyobj': PatientAllergyobj,
                                                                   'PatientPrescriptionobj': PatientPrescriptionobj,
                                                                   'PatientMedicationnobj': PatientMedicationnobj,
                                                                   'Patientdiseaseobj': Patientdiseaseobj})



@login_required()
def LabDashboard(request):
    try:
        labobj = lab.objects.get(user=request.user)
    except lab.DoesNotExist:
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")
    Hospital_labs_recordsobj = Hospital_labs_records.objects.filter(lab=labobj, accepted=True)

    data = []
    for rec in Hospital_labs_recordsobj:
        HospitalCircleobj = HospitalCircle.objects.filter(Hospitalref=rec.Hospital, accepted=True)
        for p in HospitalCircleobj:
            data.append(p.Patient)

    if request.method == 'POST':
        formno = request.POST.get('formno')
        if formno=='1':
             UID = request.POST.get('yes')
             puid = request.POST.get('yes1')
             pno =  request.POST.get('yes3')
             username = request.POST.get('yes2')
             if UID:
                 rPatient = SearchPatient(UID=int(UID))
             elif puid:
                 rPatient = SearchPatient(PUID=int(puid))
             elif pno:
                 rPatient = SearchPatient(mobno=int(pno))
             elif username:
                 rPatient = SearchPatient(mobno=username)
             if (rPatient):
                 LabCircleobj = LabCircle.objects.create(Labref=labobj,
                                                        Patient=rPatient,
                                                        otp=randrange(100000, 999999),
                                                        Timeofjoin=datetime.now(),
                                                        accepted=True)
                 LabCircleobj.save()
    LabCircleobj = LabCircle.objects.filter(Labref=labobj, accepted=True)
    removefromcircle(LabCircleobj)
    LabCircleobj = LabCircle.objects.filter(Labref=labobj, accepted=True)

    for p in LabCircleobj:
        data.append(p.Patient)
    return render(request=request,
                  template_name="LabDashboard.html",
                  context={'labobj': labobj,
                           'data': set(data)})


@login_required()
def PatientInfoLab(request, pk):
    try:
        labobj = lab.objects.get(user=request.user)
    except lab.DoesNotExist:
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")
    data = None
    LabCircleobj = LabCircle.objects.filter(Labref=labobj, accepted=True)
    for p in LabCircleobj:
        if (p.Patient.pk == pk):
            data=p.Patient

    if data is None:
        Hospital_labs_recordsobj = Hospital_labs_records.objects.filter(lab=labobj, accepted=True)
        for rec in Hospital_labs_recordsobj:
            HospitalCircleobj = HospitalCircle.objects.filter(Hospitalref=rec.Hospital, accepted=True)
            for p in HospitalCircleobj:
                if (p.Patient.pk == pk):
                    data = p.Patient
    if data:
        PatientPrescriptionobj = PatientPrescription.objects.filter(Patient=data).order_by('-date_till')[:5]
        paginator5 = Paginator(PatientPrescriptionobj, 1)
        page_number5 = request.GET.get('patient_list_page5')
        PatientPrescriptionobj = paginator5.get_page(page_number5)
        objPatientBasicInfo = PatientBasicInfo.objects.get(Patient=data)
    if request.method == 'POST' and request.FILES['report']:
        tname = request.POST.get('tname')
        tdate = request.POST.get('tdate')
        report = request.FILES['report']
        if report:
            Patientlab_recordsobj = Patientlab_records.objects.create(
                Patient=data,
                testdate = tdate,
                testname =tname,
                testreport = report,
                labid = labobj.pk,
            )
            Patientlab_recordsobj.save()
    return render(request=request,
                  template_name="PatientInfoLab.html",
                  context={'labobj': labobj,
                           'data': [data],
                           'PatientPrescriptionobj': PatientPrescriptionobj,
                           'objPatientBasicInfo':objPatientBasicInfo,
                           'Patientobj': data})


def DoctorHospitalCircleRecords(request):
    try:
        Doctorobj = Doctor.objects.get(Doctoraccount=request.user)
    except Doctor.DoesNotExist:
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")

    obj = Hospital.objects.all()
    if request.method == 'POST':
        hospid = request.POST.get('hospid')
        hospitalobj = Hospital.objects.get(pk=int(hospid))
        try:
            Hospital_Doctors_recordsobj = Hospital_Doctors_records.objects.get(Hospital=hospitalobj,
                                                                                  doctor=Doctorobj)
        except Hospital_Doctors_records.DoesNotExist:
            Hospital_Doctors_recordsobj = Hospital_Doctors_records.objects.create(Hospital=hospitalobj,
                                                                                  doctor=Doctorobj)
            Hospital_Doctors_recordsobj.save()
    survinghospitalobj = Hospital_Doctors_records.objects.filter(doctor=Doctorobj, accepted=True)
    print(survinghospitalobj)
    requestpending = Hospital_Doctors_records.objects.filter(doctor=Doctorobj, accepted=False)
    return render(request=request,
                  template_name="DoctorHospital.html",
                  context={'obj': obj,
                           'survinghospitalobj': survinghospitalobj,
                            'requestpending': requestpending})



def NurseHospitalCircleRecords(request):
    try:
        Nurseobj = nurse.objects.get(user=request.user)
    except nurse.DoesNotExist:
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")

    obj = Hospital.objects.all()
    if request.method == 'POST':
        hospid = request.POST.get('hospid')
        hospitalobj = Hospital.objects.get(pk=int(hospid))
        try:
            Hospital_staff_recordsobj = Hospital_staff_records.objects.get(Hospital=hospitalobj,
                                                                                  staff=Nurseobj)
        except Hospital_staff_records.DoesNotExist:
            Hospital_staff_recordsobj = Hospital_staff_records.objects.create(Hospital=hospitalobj,
                                                                                  staff=Nurseobj)
            Hospital_staff_recordsobj.save()
    survinghospitalobj = Hospital_staff_records.objects.filter(staff=Nurseobj, accepted=True)
    print(survinghospitalobj)
    requestpending = Hospital_staff_records.objects.filter(staff=Nurseobj, accepted=False)
    return render(request=request,
                  template_name="NurserHospital.html",
                  context={'obj': obj,
                           'survinghospitalobj': survinghospitalobj,
                            'requestpending': requestpending})

import random
import string

def createPatient(request):
    try:
        Hospitalobj = Hospital.objects.get(Nodal_Person=request.user)
    except Hospital.DoesNotExist:
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        uid = request.POST.get('uid')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        gridRadios1 = request.POST.get('gridRadios')
        address = request.POST.get('address')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        state = request.POST.get('state')
        fuid = request.POST.get('fuid')
        muid = request.POST.get('muid')
        letters = string.ascii_lowercase
        passwordraw = ''.join(random.choice(letters) for i in range(12))
        user = User.objects.create_user(username=email,
                                        password=passwordraw, first_name=firstname, last_name=lastname)
        subject = ' Welcome to EMR | OTP '
        message = ' Your account is created by Hospital : '+Hospitalobj.Hospital_Name +'  Address :  '+Hospitalobj.Hospital_Address+'   '+Hospitalobj.Hospital_City+'    Your login user id is  '+ email +'  Your default password is :   {' + passwordraw + '}'
        message+= ' you are successfully add in Hospital Circle for Next 5 days'
        recepient = email
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        if user:
             PatientRecordobj= PatientRecord.objects.create(
                                                             user=user,
                                                             firstname=firstname,
                                                             lastname=lastname,
                                                             Email=email,
                                                             Address=address,
                                                             PinCode=pincode,
                                                             City=city,
                                                             State=state,
                                                             ContactNo=mobile,)
             PatientRecordobj.save()
             PatientBasicInfoobj = PatientBasicInfo.objects.create(
                 Patient=PatientRecordobj,
                 Gender=gridRadios1,
                 Fathers_id=fuid,
                 Mathers_id=muid,
                 GovernmentIDNumber=uid,
             )
             PatientBasicInfoobj.save()
             HospitalCircleobj = HospitalCircle.objects.create(
                 Hospitalref=Hospitalobj,
                 Patient=PatientRecordobj,
                 otp=randrange(100000, 999999),
                 accepted=True,
                 Timeofjoin=datetime.now(),
             )
             HospitalCircleobj.save()
    return render(request=request,
                  template_name="hospitalcreatepatient.html",
                  context={})
