from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import loader
from django.views.generic import TemplateView


def home_view(request):
    context = {'name': 'name', 'num': 'num'}
    return render(request, 'home.html', context=context)


def test_view(request, num=0, name='balloons'):
    import pdb; pdb.set_trace()
    context = {'num': num, 'name': name}
    return render(request, 'home.html', context=context)


class ClassView(TemplateView):

    def get_context_data(self, num=0, name='balloons'):
        import pdb; pdb.set_trace()
        return {'num': num, 'name': name}
