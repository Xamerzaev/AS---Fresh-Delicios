from django.views.generic import TemplateView
from django.views import generic
from django.shortcuts import redirect

from django.core.mail import EmailMultiAlternatives
from django.contrib import messages


class Home(TemplateView):
    template_name = 'index.html'


class ContactView(generic.TemplateView):
    template_name = 'index.html'

    def post(self, request):
        name = request.POST.get('contact-name')
        from_email = request.POST.get('contact-email')
        contact_phone = request.POST.get('contact-phone')
        message = request.POST.get('contact-message')
        subject = 'С Вами хотят связаться!'

        email = 'as.company.1618@gmail.com'
        text_content = ''
        html_content = ''

        html_content += f'''<h3>ФИО - {name}<h3> <br> <h5>(
            сообщение: {message}), (email: {from_email}),
            (номер телефона: {contact_phone})</h5>'''

        msg = EmailMultiAlternatives(
            subject, text_content, from_email, [email])

        msg.attach_alternative(html_content, "text/html")
        msg.send()
        messages.success(request, "Вы успешно отправили заявку,\
                        с Вами свяжутся в самые ближайшие сроки!")

        return redirect('home')
