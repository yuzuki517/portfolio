# core/views.py
from django.shortcuts import render
from django.http import HttpResponse
from content.models import Article

# Create your views here.
def home(request):
    articles = Article.objects.published().order_by("-published_at")[:8]
    return render(request, "core/home.html", {"articles": articles})

def ads_txt(request):
    body = "google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0\n"
    return HttpResponse(body, content_type="text/plain")

