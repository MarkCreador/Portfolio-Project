# In views.py of your portfolio app

from django.shortcuts import render
from .models import Project  # Import any models you need

def base(request):
    # Logic for base page (if any)
    return render(request, 'portfolio/base.html')
# Compare this snippet from portfolio_project/portfolio/templates/portfolio/home.html:

