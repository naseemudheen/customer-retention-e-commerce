from django.shortcuts import render
from django.views import View

# Create your views here.

class HomePage(View):
    template_name = 'client/index.html'
    
    def get(self,request):
        return render(request,self.template_name)
    
    

class DocumentationView(View):
    template_name = 'client/docs.html'
    
    def get(self,request):
        return render(request,self.template_name)