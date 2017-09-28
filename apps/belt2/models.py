from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages
from models import *
import random, re, datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import bcrypt
from django.db import models
from ..login.models import Member



class ItemManager(models.Manager):
	def validate_item(self, formdata):
		errors = []
		if len(formdata['name']) < 3 :
			errors.append("Item name must be at least 3 characters long.")
		return errors

	def add_item(self, formdata):
		member = Member.objects.get(id=formdata['member'])
		item = self.create (
			name = formdata['name'],
			added_by = member,
		)
		item.liked_by.add(member)
		return item

	def add_like(self, formdata, id):
		member = Member.objects.get(id=id)
		item = Item.objects.get(id=formdata['itemid'])
		item.liked_by.add(member)
		return item

	def remove_like(self, formdata, id):
		member = Member.objects.get(id=id)
		item = Item.objects.get(id=formdata['itemid'])
		item.liked_by.remove(member)

class Item(models.Model):
	name = models.CharField(max_length=25)
	added_by = models.ForeignKey(Member, related_name="added_items")
	liked_by = models.ManyToManyField(Member, related_name="liked_items", default="")
	posted_date = models.DateField(default=datetime.date.today)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = ItemManager()
