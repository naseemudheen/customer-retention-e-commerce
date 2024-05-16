from django.shortcuts import render,redirect
from django.views import View

from client.forms import EnquiryCreateForm


class HomePage(View):
    template_name = "client/index.html"

    def get(self, request):
        return render(request, self.template_name)


class DocumentationView(View):
    template_name = "client/docs.html"

    def get(self, request):
        return render(request, self.template_name)


class enquiryCreate(View):
    template_name = "client/index.html"

    def post(self, request):
        form = EnquiryCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  
        else:
            # Print form errors to the console or display them in the template
            print(form.errors)
        return render(request, self.template_name)
