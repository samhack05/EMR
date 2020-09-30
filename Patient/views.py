from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import PatientRecord, PatientBasicInfo, Patientlab_records, PatientMedication, PatientPrescription, Dischargedetails, billingdetails
from .models import Patientdisease, PatientSymtoms, PatientProblem, patientInsurance, patientvitalinfo, PatientAllergy
from django.core.paginator import Paginator


def Patientlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                objPatientRecord = PatientRecord.objects.get(user=user)
            except PatientRecord.DoesNotExist:
                objPatientRecord = None
            if objPatientRecord is not None:
                messages.info(request, f"You are now logged in as {username}")
                return HttpResponseRedirect('/user/Dashboard/')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        messages.error(request, "Invalid username or password.")

    return render(request=request,
                  template_name="login_patient.html",
                  context={})

def PatientRegistration(request, *args, **kwargs):
    if request.method == 'POST':
        First_Name=request.POST.get('firstname')
        Last_name = request.POST.get('lastname')
        password = request.POST.get('password')
        ContactNo = request.POST.get('mobile')
        Address = request.POST.get('address')
        City = request.POST.get('city')
        Pincode = request.POST.get('pincode')
        State = request.POST.get('state')
        Email=request.POST.get('email')
        user = User.objects.create_user(username=Email,
                                        email=Email,
                                        password=password, first_name=First_Name, last_name=Last_name)
        if user:
            objuser = PatientRecord.objects.create(user=user,
                                            firstname=First_Name,
                                            lastname=Last_name,
                                            Address=Address,
                                            PinCode=Pincode,
                                            City=City,
                                            State=State,
                                            ContactNo=ContactNo,
                                            Email=Email,
                                            )

            objuser.save()
            return HttpResponse("<html><body><h1>Account Created</h1></body></html>")
        else:
            return HttpResponse("<html><body><h1>Username/Email Already Used</h1></body></html>")
    return render(request=request,
                  template_name="PatientRegistration.html",
                  context={})

"""
def Patient_Basic_Info():
    if request.method=='POST':
        Gender = request.POST.get('ge')
        Fathers_id = request.POST.get('father')
        Mathers_id = request.POST.get('mother')
        Bloodgroup = request.POST.get('blood')
        dateofbirth = request.POST.get('dob')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        profilepic = request.POST.get('profile')
        MarriedStatus = request.POST.get('status')
        emergencyContact = request.POST.get('ecn')
        Government_ID_Proof = request.POST.get('proof')
        GovernmentIDNumber = request.POST.get('govid')
        Document = request.POST.get('doc')"""


@login_required()
def PatientDashboard(request):
    try:
        Patientobj = PatientRecord.objects.get(user=request.user)
    except PatientRecord.DoesNotExist:
        logout(request)
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")
    return render(request=request,
                  template_name="PatientDashboard.html",
                  context={})


@login_required()
def labreports(request):
    try:
        Patientobj = PatientRecord.objects.get(user=request.user)
    except PatientRecord.DoesNotExist:
        logout(request)
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")

    labrecordsobj = Patientlab_records.objects.filter(Patient=Patientobj)
    paginator = Paginator(labrecordsobj, 10)
    page_number = request.GET.get('labrecords_list_page')
    labrecordsobj = paginator.get_page(page_number)

    if request.method == 'POST' and request.FILES['report']:
        tname = request.POST.get('tname')+' (ADDED by '+ Patientobj.firstname + ' ' + Patientobj.lastname +' )'
        tdate = request.POST.get('tdate')
        report = request.FILES['report']
        if report:
            Patientlab_recordsobj = Patientlab_records.objects.create(
                Patient=Patientobj,
                testdate=tdate,
                testname=tname,
                testreport=report,
                labid=0,
            )
            Patientlab_recordsobj.save()
            return redirect('/user/labreports/')

    return render(request=request,
                  template_name="labreportsP.html",
                  context={'labrecordsobj': labrecordsobj})


@login_required()
def Medications(request):
    try:
        Patientobj = PatientRecord.objects.get(user=request.user)
    except PatientRecord.DoesNotExist:
        logout(request)
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")
    PatientMedicationobj = PatientMedication.objects.filter(Patient=Patientobj).order_by('-dateadd')
    paginator = Paginator(PatientMedicationobj, 5)
    page_number = request.GET.get('PatientMedicationrecords_list_page')
    PatientMedicationobj = paginator.get_page(page_number)

    PatientPrescriptionobj = PatientPrescription.objects.filter(Patient=Patientobj).order_by('-dateadd')
    paginator1 = Paginator(PatientPrescriptionobj, 5)
    page_number1 = request.GET.get('PatientPrescriptionrecords_list_page')
    PatientPrescriptionobj = paginator1.get_page(page_number1)

    return render(request=request,
                  template_name="MedicationsP.html",
                  context={'PatientMedicationobj': PatientMedicationobj,
                           'PatientPrescriptionobj': PatientPrescriptionobj})

@login_required()
def billDisgrecords(request):
    try:
        Patientobj = PatientRecord.objects.get(user=request.user)
    except PatientRecord.DoesNotExist:
        logout(request)
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")

    billingdetailsobj = billingdetails.objects.filter(Patient=Patientobj).order_by('-dateofbilling')
    paginator1 = Paginator(billingdetailsobj, 5)
    page_number1 = request.GET.get('billingdetailrecords_list_page')
    billingdetailsobj = paginator1.get_page(page_number1)

    Dischargedetailssobj = Dischargedetails.objects.filter(Patient=Patientobj).order_by('-dateofbilling')
    paginator = Paginator(Dischargedetailssobj, 5)
    page_number = request.GET.get('Dischargedetailrecords_list_page')
    Dischargedetailssobj = paginator.get_page(page_number)

    return render(request=request,
                  template_name="billDisgrecordsP.html",
                  context={'billingdetailsobj': billingdetailsobj,
                           'Dischargedetailssobj': Dischargedetailssobj})


@login_required()
def DiseaseRecords(request):
    try:
        Patientobj = PatientRecord.objects.get(user=request.user)
    except PatientRecord.DoesNotExist:
        logout(request)
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")


    Patientdiseaseobj = Patientdisease.objects.filter(Patient=Patientobj).order_by('-dateadd').order_by('-is_active')
    paginator = Paginator(Patientdiseaseobj, 5)
    page_number = request.GET.get('Patientdisease_records_list_page')
    Patientdiseaseobj = paginator.get_page(page_number)

    PatientProblemobj = PatientProblem.objects.filter(Patient=Patientobj).order_by('-dateadd').order_by('-is_active')
    paginator1 = Paginator(PatientProblemobj, 5)
    page_number1 = request.GET.get('PatientProblem_records_list_page')
    PatientProblemobj = paginator1.get_page(page_number1)


    PatientSymtomsobj = PatientSymtoms.objects.filter(Patient=Patientobj).order_by('-dateadd').order_by('-is_active')
    paginator2 = Paginator(PatientSymtomsobj, 5)
    page_number2 = request.GET.get('PatientSymtoms_records_list_page')
    PatientSymtomsobj = paginator2.get_page(page_number2)


    return render(request=request,
                  template_name="DiseaseRecordsP.html",
                  context={'Patientdiseaseobj': Patientdiseaseobj,
                           'PatientProblemobj': PatientProblemobj,
                           'PatientSymtomsobj': PatientSymtomsobj,})

@login_required()
def Insurance(request):
    try:
        Patientobj = PatientRecord.objects.get(user=request.user)
    except PatientRecord.DoesNotExist:
        logout(request)
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")

    patientInsuranceobj = patientInsurance.objects.filter(Patient=Patientobj).order_by('-todate')
    paginator = Paginator(patientInsuranceobj, 5)
    page_number = request.GET.get('patientInsurance_records_list_page')
    patientInsuranceobj = paginator.get_page(page_number)
    if request.method == 'POST' and request.FILES['fupload']:
        fupload = request.FILES['fupload']
        ctill = request.POST.get('ctill')
        cfrom =request.POST.get('cfrom')
        insure = request.POST.get('insure')
        patientInsuobj = patientInsurance.objects.create(
            Patient=Patientobj,
            Insurancecertificate=fupload,
            insurancecompany=insure,
            fromdate=cfrom,
            todate=ctill,
        )
        patientInsuobj.save()
    return render(request=request,
                  template_name="InsuranceP.html",
                  context={'patientInsuranceobj': patientInsuranceobj,
                           })

@login_required()
def vitalinfo(request):
    try:
        Patientobj = PatientRecord.objects.get(user=request.user)
    except PatientRecord.DoesNotExist:
        logout(request)
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")

    patientvitalinfoobj = patientvitalinfo.objects.filter(Patient=Patientobj).order_by('-dateadd')
    paginator1 = Paginator(patientvitalinfoobj, 5)
    page_number1 = request.GET.get('patientvitalinfo_records_list_page')
    patientvitalinfoobj = paginator1.get_page(page_number1)

    PatientAllergyobj = PatientAllergy.objects.filter(Patient=Patientobj).order_by('-dateadd')
    paginator2 = Paginator(PatientAllergyobj, 5)
    page_number2 = request.GET.get('PatientAllergy_records_list_page')
    PatientAllergyobj = paginator2.get_page(page_number2)
    if request.method == 'POST':
        allergy = request.POST.get('allergy')
        level = request.POST.get('customRadio')
        PatientAllergyruf = PatientAllergy.objects.create(
            Patient=Patientobj,
            allergyname = allergy,
            allergy_level = level,
            addedby=request.user,
        )
        PatientAllergyruf.save()
    return render(request=request,
                  template_name="vitalinfoP.html",
                  context={'patientvitalinfoobj': patientvitalinfoobj,
                           'PatientAllergyobj': PatientAllergyobj})

@login_required()
def account(request):
    try:
        Patientobj = PatientRecord.objects.get(user=request.user)
    except PatientRecord.DoesNotExist:
        logout(request)
        return HttpResponse("<html><body><h1>You are not authorized to Access</h1></body></html>")
    if request.method == 'POST':
        Formno = request.POST.get('formno')
        if Formno=='1' or Formno==1:
             email= request.POST.get('email')
             Address= request.POST.get('Address')
             City= request.POST.get('City')
             Pincode = request.POST.get('Pincode')
             state = request.POST.get('state')
             Patientobj.email = email
             Patientobj.Address = Address
             Patientobj.City = City
             Patientobj.Pincode = Pincode
             Patientobj.state = state
             Patientobj.save()

       # if Formno == '2' or Formno == 2:

    try:
        PatientBasicInfoobj = PatientBasicInfo.objects.get(Patient=Patientobj)
    except PatientBasicInfoobj.DoesNotExist:
        PatientBasicInfoobj=None

    return render(request=request,
                  template_name="accountP.html",
                  context={'Patientobj': Patientobj,
                           'PatientBasicInfoobj': PatientBasicInfoobj})




@login_required()
def PredictDisease(request):
    Patientobj = PatientRecord.objects.get(user=request.user)
    return render(request=request,
                  template_name="PredictDiseaseP.html",
                  context={})