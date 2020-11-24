from django.shortcuts import render
from django.views import View
from . import forms

# Create your views here.
# user will sees


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        print(form)