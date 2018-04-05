from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

def index(request):
    return render(request,'index.html')


# class HomePage(TemplateView):
#     template_name = "index.html"
#
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated():
#             return HttpResponseRedirect(reverse("test"))
#         return super().get(request, *args, **kwargs)
