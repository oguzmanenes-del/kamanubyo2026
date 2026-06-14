from django.shortcuts import render, get_object_or_404
from .models import Page, BlogPost, FAQ


def home(request):
    homepage = Page.objects.filter(is_homepage=True, is_published=True).first()
    faqs = FAQ.objects.filter(is_active=True)[:6]
    latest_posts = BlogPost.objects.filter(is_published=True)[:3]

    context = {
        "page": homepage,
        "faqs": faqs,
        "latest_posts": latest_posts,
    }
    return render(request, "core/home.html", context)


def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    return render(request, "core/page_detail.html", {"page": page})


def blog_list(request):
    posts = BlogPost.objects.filter(is_published=True)
    return render(request, "core/blog_list.html", {"posts": posts})