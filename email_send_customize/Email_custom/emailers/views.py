from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail

#with document send
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from django.core.mail import EmailMessage

from django.conf import settings
from .forms import EmailForm
from django.core.mail import send_mail



'''class SendFormEmail(View):

    def  get(self, request):

        # Get the form data
        name = request.GET.get('name', None)
        email = request.GET.get('email', None)
        message = request.GET.get('message', None)

        # Send Email
        send_mail(
            'Subject - Django Email Testing',
            'Hello ' + name + ',\n' + message,
            'sender@example.com', # Admin
            [
                email,
            ]
        )

        # Redirect to same page after form submit
        messages.success(request, ('Email sent successfully.'))
        return redirect('home')'''

#email send with document
class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'emailattachment.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'email_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            files = request.FILES.getlist('attach')

            try:
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                return render(request, self.template_name,
                              {'email_form': form, 'error_message': 'Sent email to %s' % email})
            except:
                return render(request, self.template_name,
                              {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

        return render(request, self.template_name,
                      {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})

    # Single File Attachment
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST, request.FILES)

    #     if form.is_valid():

    #         subject = form.cleaned_data['subject']
    #         message = form.cleaned_data['message']
    #         email = form.cleaned_data['email']
    #         attach = request.FILES['attach']

    #         try:
    #             mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
    #             mail.attach(attach.name, attach.read(), attach.content_type)
    #             mail.send()
    #             return render(request, self.template_name, {'email_form': form, 'error_message': 'Sent email to %s'%email})
    #         except:
    #             return render(request, self.template_name, {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

    #     return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})
