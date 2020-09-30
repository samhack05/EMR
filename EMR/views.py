from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from Patient.models import PatientRecord
from Hospital.models import Hospital, Doctor, lab, nurse

def logout_user(request, *args, **kwargs):
    logout(request)
    messages.info(request, f"LOGGED OUT SUCCESSFULLY")
    return HttpResponseRedirect('/')


def homepage(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                objHospitalRecord = Hospital.objects.get(Nodal_Person=user)
            except Hospital.DoesNotExist:
                objHospitalRecord = None
            try:
                objDoctor = Doctor.objects.get(Doctoraccount=user)
            except Doctor.DoesNotExist:
                objDoctor = None
            try:
                objnurse = nurse.objects.get(user=user)
            except nurse.DoesNotExist:
                objnurse = None
            try:
                objlab = lab.objects.get(user=user)
            except lab.DoesNotExist:
                objlab = None
            try:
                objPatientRecord = PatientRecord.objects.get(user=user)
            except PatientRecord.DoesNotExist:
                objPatientRecord = None

            if objHospitalRecord:
                return HttpResponseRedirect('/management/HospitalDashboard/')
            if objDoctor:
                return HttpResponseRedirect('/management/DoctorDashboard/')
            if objnurse:
                return HttpResponseRedirect('/management/NurseDashboard/')
            if objlab:
                return HttpResponseRedirect('/management/LabDashboard/')
            if objPatientRecord:
                return HttpResponseRedirect('/user/Dashboard/')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request=request,
                  template_name="homepage.html",
                  context={})
@login_required()
def dashboard(request):
    user=request.user
    if user is not None:
        login(request, user)
        try:
            objHospitalRecord = Hospital.objects.get(Nodal_Person=user)
        except Hospital.DoesNotExist:
            objHospitalRecord = None
        try:
            objDoctor = Doctor.objects.get(Doctoraccount=user)
        except Doctor.DoesNotExist:
            objDoctor = None
        try:
            objnurse = nurse.objects.get(user=user)
        except nurse.DoesNotExist:
            objnurse = None
        try:
            objlab = lab.objects.get(user=user)
        except lab.DoesNotExist:
            objlab = None
        try:
            objPatientRecord = PatientRecord.objects.get(user=user)
        except PatientRecord.DoesNotExist:
            objPatientRecord = None

        if objHospitalRecord:
            return HttpResponseRedirect('/management/HospitalDashboard/')
        if objDoctor:
            return HttpResponseRedirect('/management/DoctorDashboard/')
        if objnurse:
            return HttpResponseRedirect('/management/NurseDashboard/')
        if objlab:
            return HttpResponseRedirect('/management/LabDashboard/')
        if objPatientRecord:
            return HttpResponseRedirect('/user/Dashboard/')
    else:
        messages.error(request, "Invalid username or password.")
    return HttpResponseRedirect('/')


#
#
from django.shortcuts import render,redirect
from django.contrib import messages
from cardio_predict import predict
from diabetes_predict import predict_diabetes
from liver_predict import liver_Predict
from predict_using_symtoms import pridict_sym

def cardiovascular(request, *args, **kwargs):
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    height = request.POST.get('height')
    weight = request.POST.get('weight')
    ap_hi = request.POST.get('sbp')
    ap_lo = request.POST.get('dbp')
    cholesterol = request.POST.get('chol')
    gluc = request.POST.get('glu')
    smoke = request.POST.get('smoke')
    alco = request.POST.get('alco')
    active = request.POST.get('active')

    if(age):
        data=[int(age)*365, int(gender), int(height), int(weight), int(ap_hi), int(ap_lo), int(cholesterol), int(gluc), int(smoke), int(alco), int(active)]
        result=predict(data)
        print(result)
        messages.info(request, result)
    return render(request, "cardio.html", {})

def diabetes(request, *args, **kwargs):
    Preg= request.POST.get('Preg')
    Glu= request.POST.get('Glu')
    bp = request.POST.get('bp')
    st = request.POST.get('st')
    insu = request.POST.get('insu')
    bmi = request.POST.get('bmi')
    dpf = request.POST.get('dpf')
    age = request.POST.get('age')
    if(Preg):
        data=[int(Preg),int(Glu),int(bp),int(st),int(insu),int(bmi),float(dpf),int(age)]
        result=predict_diabetes(data)
        print(result)
        messages.info(request, result)
    return render(request, "diabetes_predict.html", {})


def liver(request, *args, **kwargs):
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    Total_Bilirubin = request.POST.get('Total_Bilirubin')
    Direct_Bilirubin = request.POST.get('Direct_Bilirubin')
    Alkaline_Phosphotase = request.POST.get('Alkaline_Phosphotase')
    Alamine_Aminotransferase = request.POST.get('Alamine_Aminotransferase')
    Aspartate_Aminotransferase = request.POST.get('Aspartate_Aminotransferase')
    Total_Protiens = request.POST.get('Total_Protiens')
    Albumin = request.POST.get('Albumin')
    Albumin_and_Globulin_Ratio = request.POST.get('Albumin_and_Globulin_Ratio')

    if(age):
        data=[int(age),int(gender),float(Total_Bilirubin),float(Direct_Bilirubin),int(Alkaline_Phosphotase),int(Alamine_Aminotransferase),int(Aspartate_Aminotransferase),float(Total_Protiens),float(Albumin),float(Albumin_and_Globulin_Ratio)]
        result=liver_Predict(data)
        print(result)
        messages.info(request, result)
    return render(request, "liver.html", {})

def symtoms(request, *args, **kwargs):
    sy1 = request.POST.get('my1')
    sy2 = request.POST.get('my2')
    sy3 = request.POST.get('my3')
    sy4 = request.POST.get('my4')
    sy5 = request.POST.get('my5')
    sy6 = request.POST.get('my6')
    sy7 = request.POST.get('my7')
    sy8 = request.POST.get('my8')
    sy9 = request.POST.get('my9')
    sy10 = request.POST.get('my10')

    if(sy1 and sy2):
        data=[]
        if(sy1):
            data.append(sy1)
        if (sy2):
            data.append(sy2)
        if (sy3):
            data.append(sy3)
        if (sy4):
            data.append(sy4)
        if (sy5):
            data.append(sy5)
        if (sy6):
            data.append(sy6)
        if (sy7):
            data.append(sy7)
        if (sy8):
            data.append(sy8)
        if (sy9):
            data.append(sy9)
        if (sy10):
            data.append(sy10)
        print(data)

        result=pridict_sym(data)
        print(result)
        messages.info(request, result)
    return render(request, "predict_using_sym.html", {})

