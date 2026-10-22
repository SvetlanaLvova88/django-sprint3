
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post


def published_posts():
    return Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    ).select_related(
        'author',
        'location',
        'category',
    )


def index(request):
    post_list = published_posts()[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, pk):
    post = get_object_or_404(
        published_posts(),
        pk=pk,
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = published_posts().filter(
        category=category,
    )
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
