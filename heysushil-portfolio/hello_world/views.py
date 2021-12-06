from django.shortcuts import render

# Create your views here.
# MVC = model view controller
# MVT = modela view temeplate

# MVC => 
# Web Desighn = Temeplates Folder
# Developemtn = views.py = Controller
# Database = models.py

# YouTube = UI => Controller (views.py) <= Database

def hello_world(request):
        return render(request, 'hello_world.html', {})