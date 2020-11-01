from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView,TemplateView
from redirect.models import Article

def home(*args, **kwargs):
    return HttpResponse("<br><br><br><br><br><br><br><br><br><br><br><br><br><h1>Redirect View</h1><h3>In admin page you can create a article and assign a counter to it....</h3>")

class ArticleDetail(TemplateView):

    template_name = "redirect.html"

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_article'] = Article.objects.get(pk=self.kwargs.get('pk',None))
        return context


class ArticleCounterRedirectView(RedirectView):

    permanent = False
    query_string = True
    pattern_name = 'article-detail'

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        article.counter +=1
        article.save()
        return super().get_redirect_url(*args, **kwargs)