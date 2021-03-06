from django import forms
from django.core.mail import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'placeholder': 'Name...'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email...'}), required=True)
    subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Subject...'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message...'}), required=True)

    def send_email(self):
        subject = self.cleaned_data['subject']
        email = self.cleaned_data['email']
        name = self.cleaned_data['name']
        message = self.cleaned_data['message'] + f"\nFrom: {name}"
        EmailMessage(subject=subject, body=message, from_email=email, to=['contact.gtahacks@gmail.com'],
                     reply_to=[email]).send()
