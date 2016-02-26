from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = "app/home.html"

    def get_context_data(self, **kwargs):
        template = get_template('app/home.py')
        python_context = Context({"foo": "bar"})

        return Context({
            'title': "Brythonを使ったやつ",
            'python': template.render(python_context)
        })

home = HomeView.as_view()
