from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import request, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Dataflar Django Tutorial<html><body></body> Hello World DataFlar Django tutorials</body></html>")
