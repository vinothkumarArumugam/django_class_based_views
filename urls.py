from django.contrib import admin
from django.urls import path
from cbvapp import views         ####importing view file 
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('check/',views.FirstView.as_view()),          #### you to tell django ,make this class as function (.as_view) ,it is for class based views
    path('check2/',views.SecondView.as_view()),
]
