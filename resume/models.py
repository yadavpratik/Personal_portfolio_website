from django.db import models

from django.contrib.auth.models import User
from django.db import connection, models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Expression
from django.db.models.fields import CharField


# Create your models here.

class userprofile(models.Model):
    connection=models.OneToOneField(to=User,on_delete=CASCADE)
    name=models.CharField(max_length=30,null=True,blank=True)
    profile_pic=models.ImageField(upload_to='pic',null=True,blank=True)
    profession=models.CharField(max_length=30,null=True,blank=True)
    intro=models.TextField(null=True,blank=True)
    career_object=models.TextField(null=True,blank=True)
    Dob=models.DateField(null=True,blank=True)
    city=models.CharField(max_length=20, null=True,blank=True)
    website=models.CharField(max_length=30,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    email=models.CharField(max_length=30,null=True,blank=True)
    phone=models.CharField(max_length=10,null=True,blank=True)
    address=models.CharField(max_length=60,null=True,blank=True)
    
class education(models.Model):
    connection=models.ForeignKey(to=User, on_delete=CASCADE)
    degree_name=models.CharField(max_length=30,null=True,blank=True)
    college_name=models.CharField(max_length=30,null=True,blank=True)
    start_year=models.IntegerField(null=True,blank=True)
    end_year=models.IntegerField(null=True,blank=True)

class experience(models.Model):
    connection=models.ForeignKey(to=User,on_delete=CASCADE)
    position=models.CharField(max_length=30,null=True,blank=True)
    company_name=models.CharField(max_length=30,null=True,blank=True)
    start_year=models.IntegerField(null=True,blank=True)
    end_year=models.IntegerField(null=True,blank=True)


class skills(models.Model):
    connection=models.ForeignKey(to=User,on_delete=CASCADE)
    tech_name=models.CharField(max_length=20,null=True,blank=True)
    progress=models.IntegerField(null=True,blank=True)

class projects(models.Model):
    connection=models.ForeignKey(to=User,on_delete=CASCADE)
    project_name=models.CharField(max_length=20,null=True,blank=True)
    description=models.CharField(max_length=50,null=True,blank=True)
    project_link=models.CharField(max_length=60,null=True,blank=True)

class services(models.Model):
    connection=models.ForeignKey(to=User,on_delete=CASCADE)
    title=models.CharField(max_length=20,null=True,blank=True)
    services_description=models.TextField(null=True,blank=True)
    services_icon=models.TextField(null=True,blank=True)


class portfollios(models.Model):
    connection=models.ForeignKey(to=User,on_delete=CASCADE)
    gallary=models.ImageField(upload_to='gallary',null=True,blank=True)


class contacts(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    email=models.CharField(max_length=20,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    message=models.TextField(null=True,blank=True)

class intro(models.Model):
    connection=models.ForeignKey(to=User,on_delete=CASCADE)
    skill_intro=models.CharField(max_length=120,null=True,blank=True)
    project_intro=models.CharField(max_length=120,null=True,blank=True)
    portfolio_intro=models.CharField(max_length=120,null=True,blank=True)
    service_intro=models.CharField(max_length=120,null=True,blank=True)

class certificates(models.Model):
    connection=models.ForeignKey(to=User,on_delete=CASCADE)
    certificate_name=models.CharField(max_length=20,null=True,blank=True)
    year=models.IntegerField(null=True,blank=True)
