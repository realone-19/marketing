from django.shortcuts import render
from customer_info.models import Customer, Account_detail
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from . import models
from . import forms

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
class IndexView(TemplateView):
    template_name = 'customer_info/index.html'


class CustomerDetailView(DetailView):
    model = Customer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['max_value'] = 100
        return context


class PaymentListView(ListView):
    model = Account_detail

    def get_queryset(self):
        queryset = Account_detail.objects.filter(customer__full_name='{} {}'.format(self.request.user.first_name,
                                                                                            self.request.user.last_name).upper())
        return queryset




def register(request):
    registered = False
    user_form = forms.UserForm()
    profile_form = forms.UserProfileForm()

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileForm(data=request.POST)
        if user_form.is_valid:
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'phone_number' in request.POST:
                profile.phone_number = request.POST['phone_number']
                profile.save()

            registered = True
            return HttpResponseRedirect('user_login')
        else:
            print(user_form.errors)

    else:
        return render(request,'customer_info/registration.html',{'user_form':user_form,
                                                            'profile_form':profile_form,
                                                            'registered':registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('about'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            # print('Someone tried to log in and failed')
            return render(request, 'customer_info/user_login.html')
            # return HttpResponseRedirect(reverse('index'))
            # return HttpResponse('Invalid login details')
    else:
        return render(request, 'customer_info/user_login.html')
