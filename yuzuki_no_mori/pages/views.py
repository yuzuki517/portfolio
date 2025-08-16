# pages/views.py
from django.shortcuts import get_object_or_404,render
from .models import Page

# Create your views here.
def detail(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    return render(request, "pages/detail.html", {"page": page})

