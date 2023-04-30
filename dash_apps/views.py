from django.shortcuts import render

def first_app(request):
    return render(request, 'dash_apps/first_app.html', {})