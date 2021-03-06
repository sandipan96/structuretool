from django import forms
from .models import ProjectDetails, MatStrength, SectionLibrary

class ProjectDetailsForm(forms.ModelForm):
    class Meta:
        model= ProjectDetails
        fields= ["owner","projectCode","projectName","clientName","clientEmail","clientPhone","clientAddress"]

class MatStrengthForm(forms.ModelForm):
    class Meta:
        model = MatStrength
        fields = ["owner","name","bendStress"]


class SectionLibraryForm(forms.ModelForm):
    class Meta:
        model = SectionLibrary
        fields= ["system","profileCodeInner","profileCodeOuter","addReinfInner","addReinfOuter","addInserts","drawing","ixx","wxx","sectionName"] 


class SectionFormTwo(forms.ModelForm):
    class Meta:
        model = SectionLibrary
        fields = ["system","drawing","sectionName"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sectionName'].queryset = SectionLibrary.objects.none()    