# content/views.py
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Article, Tag

# Create your views here.
def list_view(request):
    qs = Article.published().order_by("-published_at")
    paginator = Paginator(qs, 10)
    page = paginator.get_page(request.GET.get("page"))
    return render(request, "content/list.html", {"page": page})

def detail_view(request, slug):
    obj = get_object_or_404(Article, slug=slug, status="PUBLISHED")
    return render(request, "content/detail.html", {"article": obj})

def tag_view(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    qs = Article.published().filter(tags=tag).order_by("-published_at")
    return render(request, "content/tag.html", {"tag": tag, "articles": qs})

def preview_view(request, slug, token):
    obj = get_object_or_404(Article, slug=slug)
    if obj.status == "PUBLISHED" or token == obj.preview_token or (request.user.is_authenticated and request.user.is_staff):
        return render(request, "content/detail.html", {"article": obj, "is_preview": True})
    raise Http404()

