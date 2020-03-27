from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Appointment
from .forms import CreateAppointment

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form })

@login_required(login_url='/login/')
def appointment_list(request):
    latest_appointments = Appointment.objects.order_by('-start')[:5]
    context = {
            'latest_appointments': latest_appointments
    }
    return render(request, 'calendars/index.html', context)

@login_required(login_url='/login/')
def details(request, appointment_id):
    print(appointment_id)
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, 'calendars/details.html', {'appointment': appointment})


@login_required(login_url='/login/')
def create_appointment(request):
    if request.method == 'POST':
        form = CreateAppointment(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendars:appointment_list')
    else:
        form = CreateAppointment()
    return render(request, 'calendars/create_appointment.html', {'form': form})
