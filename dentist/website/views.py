from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Appointment
from . forms import AppointmentForm
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout 


def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		contact = "Name: " +  message_name +  " Email: " +  message_email +  " Message: " +  message
		send_mail(
			'Contact',
			contact,
			message_email,
			['seniorproject242@gmail.com']
			)

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		return render(request, 'contact.html', {})



def about(request):
	return render(request, 'about.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

def service(request):
	return render(request, 'service.html', {})

def appointment(request):
	if request.method == "POST":
		your_name = request.POST['name']
		your_phone = request.POST['phone']
		your_email = request.POST['email']
		your_address = request.POST['address']
		your_schedule = request.POST['schedule']
		your_date = request.POST['date']
		your_message = request.POST['message']

		appointment = "Name: " + your_name + " Phone: " + your_phone + " Email: " + your_email + " Address: " + your_address + " Schedule: " + your_schedule + " Date: " + your_date + " Message: " + your_message 



		send_mail(
			'Appointment Request',
			appointment,
			your_email,
			['seniorproject242@gmail.com']
			)

		return render(request, 'appointment.html', {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_address': your_address,
			'your_schedule': your_schedule,
			'your_date': your_date,
			'your_message': your_message
			})
	else:
		return render(request, 'home', {})

def booking(request):
	if request.method == "POST":
		form = AppointmentForm(request.POST or None)
		if form.is_valid():
			form.save()
		else:
			name = request.POST['name']
			phone = request.POST['phone']
			email = request.POST['email']
			address = request.POST['address']
			schedule = request.POST['schedule']
			date = request.POST['date']
			message = request.POST['message']

			messages.success(request, ('There was an error in registration! Please try again'))
			return render(request, 'booking.html')
		messages.success(request, ('You have been registered successfully'))
		return redirect('appointment')
	else:
		return render(request, 'booking.html', {})

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login.html')
			

		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

