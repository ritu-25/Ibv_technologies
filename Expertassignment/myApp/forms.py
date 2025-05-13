from django import forms
from .models import Myapp
from .models import Contact




class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Myapp
        fields = ['name', 'email', 'phone', 'title', 'word_count']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number', 'id': 'phone'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assignment title'}),
            'word_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter word count'}),
        }
        



CITY_CHOICES = [
    ('Jaipur', 'Jaipur'),
    ('Delhi', 'Delhi'),
    ('Mumbai', 'Mumbai'),
    ('Chandigarh', 'Chandigarh'),
    ('Bangalore', 'Bangalore'),
    ('Hyderabad', 'Hyderabad'),
    ('Kolkata', 'Kolkata'),
    ('Pune', 'Pune'),
    ('Lucknow', 'Lucknow'),
    ('Indore', 'Indore'),
]

STATE_CHOICES = [
    ('Rajasthan', 'Rajasthan'),
    ('Delhi', 'Delhi'),
    ('Maharashtra', 'Maharashtra'),
    ('Punjab', 'Punjab'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Karnataka', 'Karnataka'),
    ('Haryana', 'Haryana'),
    ('West Bengal', 'West Bengal'),
    ('Telangana', 'Telangana'),
]


          
class ContactForm(forms.ModelForm):
    city = forms.ChoiceField(choices=CITY_CHOICES, widget=forms.Select(attrs={'class': 'form-select', 'required': True}))
    state = forms.ChoiceField(choices=STATE_CHOICES, widget=forms.Select(attrs={'class': 'form-select', 'required': True}))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'city', 'state', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter 10-digit phone number', 'required': True, 'pattern': '[0-9]{10}'}),
            'city': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'state': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'required': True}),
        }