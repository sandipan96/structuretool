from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.urls import reverse
import django_tables2 as tables

class ProjectDetails(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    projectCode = models.IntegerField()
    projectName = models.CharField(max_length = 100)
    clientName  = models.CharField(max_length = 100)
    clientEmail = models.EmailField()
    clientPhone = models.CharField(max_length = 15)
    clientAddress = models.CharField(max_length = 100)

    def __str__(self):
        return self.projectName

    def get_absolute_url(self):
        return reverse('ProjectDetails-detail', kwargs = {'pk' : self.pk})    


class SimpleTable(tables.Table):
    class Meta:
        model = ProjectDetails


class AlloyGrade(models.Model):
    alloygrade = models.CharField(max_length = 20)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.alloygrade

    def get_absolute_url(self):
        return reverse('alloyEdit', kwargs = {'pk' : self.pk})   


class MatStrength(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 20)
    bendStress = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('matStrEdit', kwargs = {'pk' : self.pk})       

class SectionLibrary(models.Model):
    system = models.CharField(max_length = 10)
    profileCodeInner = models.CharField(max_length = 10)
    profileCodeOuter = models.CharField(max_length = 10)
    addReinfInner = models.CharField(max_length = 10)
    addReinfOuter = models.CharField(max_length = 10)
    addInserts = models.CharField(max_length = 3)
    drawing = models.ImageField(upload_to = 'images/', null = True, verbose_name="")
    ixx = models.FloatField(default= 0.0)
    wxx = models.FloatField(default= 0.0)
    sectionName = models.CharField(max_length = 50, default = "SECTION-NAME")

    def __str__(self):
        return self.system + ": " + str(self.drawing)

    def get_absolute_url(self):
        return reverse('structSpecs', kwargs = {'pk' : self.pk})      

