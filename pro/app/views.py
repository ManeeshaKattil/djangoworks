from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# ---------------FUNCTION BASED VIEW-----------
# def Home(request):
#     if request.method == 'GET':
#         return HttpResponse("Welcome to Django")

# # index view --index page
# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('Index Page')

# -------------CLASS BASED VIEW--------------
from django.views import View

class Home(View):
    def get(self,request):
        return HttpResponse("Welcome to Django")

class Index(View):
    def get(self,request):
        return HttpResponse("Welcome to Index Page")