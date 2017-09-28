from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from models import *
import random, re, datetime
from datetime import date
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import bcrypt
from django.db import models
from ..login.models import Member


def current_member(request):
    id = request.session['id']
    member = Member.objects.get(id=id)
    return member

def logout(request):
    request.session.pop('id')
    return redirect(reverse('index'))

def dashboard(request):
    member = current_member(request)
    liked = member.liked_items.all()
    print liked
    items = Item.objects.all()
    print items
    context = {
    	"member": member,
    	"liked": liked,
    	"items": items,
    }
    return render(request, "belt2/dashboard.html", context)

def add_item(request):
	member = current_member(request)
	if "errors" in request.session :
		errors = request.session['errors']
		request.session.pop('errors')
	else :
		errors = []
	context = {
		"member": member,
		"errors": errors,
	}
	return render(request, "belt2/add_item.html", context)

def create(request):
	if request.method == "POST":
		errors = Item.objects.validate_item(request.POST)
		if errors:
                    request.session['errors'] = errors
                    return redirect(reverse('add_item'))
        item = Item.objects.add_item(request.POST)
        return redirect(reverse('dashboard'))

def showitem(request, id):
    item = Item.objects.get(id=id)
    print item.name
    people = item.liked_by.all()
    print people
    context = {
		"item": item,
        "people": people,
	}
    return render(request, "belt2/show_item.html", context)

def add_like(request):
    memberid = request.session['id']
    liked_item = Item.objects.add_like(request.POST, memberid)
    return redirect(reverse("dashboard"))

def remove_like(request):
    memberid = request.session['id']
    unliked_item = Item.objects.remove_like(request.POST, memberid)
    return redirect(reverse("dashboard"))

def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect(reverse('dashboard'))
