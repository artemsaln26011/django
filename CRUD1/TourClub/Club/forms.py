from django import forms
from .models import Route, Instructor, Equipment, Trip, Tourist

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'

class TouristForm(forms.ModelForm):
    class Meta:
        model = Tourist
        fields = '__all__'