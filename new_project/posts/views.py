from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

class HelloWord(View):
    def get(self, request):
        data = {
            'name': 'Alejo cardona',
            'age': 30,
            'codes': ['python', 'laravel', 'go']
        }
        return render(request, 'hola_alejo.html', context=data)
