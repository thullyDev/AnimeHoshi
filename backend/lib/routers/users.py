from rest_framework.response import Response
from django.shortcuts import render, redirect
from .base import Base
from ..resources import ROOT_FILE

class Users(Base):
	def root(self, request): return render(request, ROOT_FILE)