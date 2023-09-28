from django.shortcuts import render
from django.views.generic import View,TemplateView               ##### if you want to use class based views ,you have to import View ,also templateview(for templates)
from django.http import HttpResponse                            ##### this is for http response
class FirstView(View):                                          ### make class with View(class in django.views.generic) as mainclass(parent class)
    def get(self,request):                 ##### this get() function is  ****** view's class function ******
        self.name='vinoth'
        return HttpResponse(self.name)
class SecondView(TemplateView):            #### this function are built in function to use templates this will automatically returns httpresponse to templates ,it doesnot requires function
    template_name='cbvapp/base.html' 
