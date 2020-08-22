from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=120, widget=forms.TextInput())
    due_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'datepicker'}))
    completed = forms.BooleanField(required=False)
    description = forms.CharField( required=False, widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))