
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from customers.models import NewEntry
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(login_required, name='dispatch')
class list_view(ListView):
    model = NewEntry
    context_object_name = "list_view"
    template_name = "customers/list.html"

class gen_eng_visa(DetailView):
    model = NewEntry
    context_object_name = "detail_visa"
    template_name = "customers/gen_eng_visa.html"

def error_404(request):
        data = {}
        return render(request,'customers/error_404.html', data)

def error_500(request):
        data = {}
        return render(request,'customers/error_500.html', data)
