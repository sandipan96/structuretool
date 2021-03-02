from django import forms
from .models import ProjectDetails, AlloyGrade

class ProjectDetailsForm(forms.ModelForm):
    class Meta:
        model= ProjectDetails
        fields= ["owner","projectCode","projectName","clientName","clientEmail","clientPhone","clientAddress"]


