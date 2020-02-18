from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "boticashback/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context