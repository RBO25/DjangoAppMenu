from django.views.generic import TemplateView


class MenuPageView(TemplateView):
    template_name = "treemenu/index.html"