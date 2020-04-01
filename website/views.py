from django.shortcuts import render
from website.models import Cadavre
from django.views import generic
from website.forms import SendCadavrePartForm
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

class PlayCadavreView(generic.DetailView):
    model = Cadavre
    slug_field = 'code'
    slug_url_kwarg = 'code'

    def get_context_data(self, **kwargs):
        context = super(PlayCadavreView, self).get_context_data(**kwargs)
        context['form'] = SendCadavrePartForm
        return context

@require_http_methods(["POST"])
def send_cadavre(request, code):
    cadavre = get_object_or_404(Cadavre, code=code)
    form = SendCadavrePartForm(request.POST)
    if form.is_valid():
        cadavre.cadavrepart_set.create(content=form.cleaned_data['content'], author=form.cleaned_data['author'])
        return render(request, 'success.html')
    else:
        return HttpResponseRedirect(reverse('cadavre_detail', code=cadavre.code))