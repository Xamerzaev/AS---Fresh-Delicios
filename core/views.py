from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import ListView

from .models import Dish
from .forms import ReviewForm
# from .models import Product

class Home(TemplateView):
    template_name = 'index.html'

    def post(self, request):

        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        email = 'as.company.1618@gmail.com'
        subject1 = f'{subject}'
        from_email = request.POST.get('email')
        text_content = ''
        html_content = ''

        html_content += f'''<h1>Здравстуйте, я {name},
        (сообщение: {message}), (email: {from_email})</h1>'''
        msg = EmailMultiAlternatives(
            subject1, text_content, from_email, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        email = request.POST.get('email')
        subject = 'Ваше письмо доставлено'
        from_email = request.POST.get('email')
        text_content = ''
        html_content = ''

        html_content += f'''<h1>Привет:"{subject1}" было успешно отправлено!</h1>'''
        msg = EmailMultiAlternatives(
            subject, text_content, from_email, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return redirect('home')


# def selectview(request):
#    product  = Product.objects.all()
#    form = request.POST
#    if request.method == 'POST':
#       selected_item = get_object_or_404(Product, pk=request.POST.get('product_id'))


#    return render ('index.html', {'items':product})


class JsonFilterMoviesView(ListView):
    """Фильтр блюд в json"""
    def get_queryset(self):
        queryset = Dish.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        ).distinct().values("title", "tagline", "url", "poster")
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"movies": queryset}, safe=False)