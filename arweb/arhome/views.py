from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework import generics, serializers
from arhome.serializers import MemberSerializer
from arhome.models import Member
from django.views import View

class Home(View):
	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, "home.html", context)

	# def post():
	# def ...():

class About(View):
	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, "about.html", context)

class Events(View):
	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, "events.html", context)

class Wip(View):
	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, "wip.html", context)

class ErrorPage(View):
	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, "error.html", context)


class MemberList(generics.ListCreateAPIView):
	queryset = Member.objects.all()
	serializer_class = MemberSerializer

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Member.objects.all()
	serializer_class = MemberSerializer
