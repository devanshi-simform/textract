from cgitb import html
from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView
from .models import file_Upload
from .form import File1Upload
from django.urls import reverse_lazy
from analyse import analyze
import pandas as pd

class file_upload(CreateView):
    form_class = File1Upload
    model = file_Upload
    success_url = reverse_lazy('page1')

    def post(self, request, *args, **kwargs):
        document = str(request.FILES['profile_image'])
        choice_data = request.POST['choice']
        response = super().post(request, *args, **kwargs)
        # breakpoint()
        analyze(document,choice_data)
        return response

class file_show(ListView):
    template_name = 'templates/success.html'
    
    def get(self, request):
        file_name = 'table.csv'
        # file_name = 'forms.txt'
        if file_name.endswith('.csv'):
            readed_file = pd.read_csv(file_name)
            table_data = readed_file.to_html()
            context = {
                    'table_data':table_data
            }
        elif file_name.endswith('.txt'):
            f = open(file_name, 'r')
            text_data = f.read()
            f.close()
            context= {
                'text_data':text_data
            }
        return render(request, self.template_name, context)