from django.shortcuts import render
from django.http import HttpResponse

def welcome_Response(request):
    return HttpResponse("Welcome to Library Management System")
def library_information(request):
    return HttpResponse("Welcome to our Library")
def Book_list(request):
    return HttpResponse("Available Books: Python,Django,Java,React,MySQL")
def Book_details(request):
    return HttpResponse("Book Name: Django | Author: William S.Vincent")
def contact_information(request):
    return HttpResponse("Contact us at library@gmail.com")
# Create your views here.
