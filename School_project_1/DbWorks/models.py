from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Comments(models.Model):
    user_name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.user_name
    def __str__(self):
        return self.comment
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Buscket(models.Model):
    tech_list = models.CharField(max_length=20)

class Products(models.Model):
    tech = models.CharField(max_length=500)

"""DO MIGRATIONS!!!!"""
