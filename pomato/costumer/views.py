from django.shortcuts import render
from costumer.forms import *
# Create your views here.
def home(request):
    return render(request, 'home.html')

def costumer_registration(request):
    ECFO = CostumerForm()
    d = {'ECFO': ECFO}
    if request.method=='POST':
        CFDO = CostumerForm(request.POST)
        if CFDO.is_valid():
            pw = CFDO.cleaned_data['password']
            MCFDO=CFDO.Save(commit=False)
            MCFDO.set_password(pw)
            MCFDO.Save()
    return render(request, 'costumer_registration.html', d)
    