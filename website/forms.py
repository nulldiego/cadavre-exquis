from django import forms
    
class SendCadavrePartForm(forms.Form):
    content = forms.CharField(help_text="Introduce la continuación", required=True, label='Continuación', widget=forms.Textarea)
    author = forms.CharField(help_text="Introduce tu nombre", required=True, label='Nombre')