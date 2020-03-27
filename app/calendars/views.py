from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm
from .models import Appointment
from .forms import AppointmentForm

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

def index(request):
    latest_appointments = Appointment.objects.order_by('-start')[:5]
    context = {
            'latest_appointments': latest_appointments
    }
    return render(request, 'calendars/index.html', context)

def detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, 'calendars/detail.html', {'appointment': appointment})

def get_name(request):
    print("HERE IT WAS")
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = AppointmentForm(initial={'description': "Type here"})
        print("Here after", form)
    return render(request, 'calendars/appointment.html', {'form': form })

class AppointmentCreate(CreateView):
    model = Appointment
    fields = ['title', 'description', 'start', 'end']

    def form_valid(self, form):
#        form.instance.created_by = self.request.user
        return super().form_valid(form)
