from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView,View
from client import models


class home(TemplateView):
    template_name = 'g-flightlist.html'

class flightList(View):
    def get(self,request):
        return render(request, 'g-flightlist.html')

class flightDetail(View):
    def get(self,request):
        passenger_list = models.passenger.objects.all()
        context = {'passenger_list': passenger_list}
        return render(request, 'g-flightdetail.html', context=context)

class flightBooking(View):
    def get(self,request):
        return render(request, 'g-flightbooking.html')

class myProfile(View):
    def get(self,request):
        return render(request, 'g-myprofile.html')

class myBooking(View):
    def get(self,request):
        return render(request, 'g-mybooking.html')

class bookingHistory(View):
    def get(self, request):
        return render(request, 'g-bookinghistory.html')

class logout(View):
    def get(self, request):
        return render(request, 'g-login.html')

class login(View):
    def get(self, request):
        return render(request, 'g-login.html')

class register(View):
    def get(self, request):
        return render(request, 'g-register.html')

class bookingConfirm(View):
    def get(self, request):
        return render(request, 'g-bookingconfirm.html')

class addPassenger(View):
    def get(self,request):
        return render(request, 'g-addpassenger.html')

    def post(self,request):
        passenger = models.passenger()
        passenger.name = request.POST.get('name')
        passenger.gender = request.POST.get('gender')
        passenger.nationality = request.POST.get('nationality')
        passenger.passport = request.POST.get('passport')
        passenger.save()
        return render(request, 'g-flightdetail.html')



