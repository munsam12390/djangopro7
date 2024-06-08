from django.db import forms

class principal(forms.Forms):
    name=forms.CharField(max_length=25)
    adress=forms.CharField(max_length=30)
    email=forms.EmailField()

class teachers(forms.Forms):
    name=forms.CharField(max_length=26)
    adress=forms.CharField(max_length=30)
    materials=forms.onetomany(principal,on_delete=forms.CASCADE,primary_key=True)
    
class students(forms.Forms):
    id=forms.IntegerField()
    name=forms.CharField(max_length=40)
    price=forms.FloatField(max_length=50)
    company=forms.onetomanyfield(teachers,on_delete=forms.CASCADE,primary_key=True)
    
    
