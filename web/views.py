from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Count
from django.core.paginator import Paginator
from random import sample
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.

def live_search(request):
    query = request.GET.get('q')

    # Search CPALinks and BlogPosts that match the query
    cpalinks = CPALink.objects.filter(Q(title__icontains=query) | Q(slug__icontains=query))
    blogposts = BlogPost.objects.filter(Q(title__icontains=query) | Q(slug__icontains=query))

    # Convert results to dictionaries
    cpalinks_data = [{'title': cpa.title, 'slug': cpa.slug, 'image_url': cpa.title_image.url} for cpa in cpalinks]
    blogposts_data = [{'title': blog.title, 'slug': blog.slug, 'image_url': blog.image.url} for blog in blogposts]

    results = {
        'cpalinks': cpalinks_data,
        'blogposts': blogposts_data,
    }

    return JsonResponse(results)


def all_blogs(request):
    # Retrieve all blog posts
    all_posts = BlogPost.objects.all()

    # Number of blog posts to display per page
    posts_per_page = 10

    # Create a Paginator instance
    paginator = Paginator(all_posts, posts_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    try:
        # Get the Page object for the current page number
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If the page parameter is not an integer, show the first page
        page = paginator.page(1)
    except EmptyPage:
        # If the page is out of range (e.g., page 9999), show the last page
        page = paginator.page(paginator.num_pages)

    context = {
        'blogs': page,
    }

    return render(request, 'blogs.html', context)


def all_links(request):
    # Retrieve all blog posts
    all_posts = CPALink.objects.all()

    # Number of blog posts to display per page
    posts_per_page = 10

    # Create a Paginator instance
    paginator = Paginator(all_posts, posts_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    try:
        # Get the Page object for the current page number
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If the page parameter is not an integer, show the first page
        page = paginator.page(1)
    except EmptyPage:
        # If the page is out of range (e.g., page 9999), show the last page
        page = paginator.page(paginator.num_pages)

    context = {
        'blogs': page,
    }

    return render(request, 'links.html', context)


def home(request):
    posts = BlogPost.objects.all()
    random_cpas = CPALink.objects.order_by('?')[:4]

    # Retrieve all CPACategory objects with their associated CPALink objects
    categories_with_links = CPACategory.objects.prefetch_related('cpalink_set')
    featured_blogs = BlogPost.objects.order_by('?')[:3]
    some_blogs = BlogPost.objects.order_by('?')[:9]

    # Retrieve the latest 5 blogs
    latest_blogs = BlogPost.objects.order_by('-created_at')[:3]

    # Retrieve 5 popular blogs (you can define your popularity criteria)
    popular_blogs = BlogPost.objects.order_by('?')[:3]

    featured_links = CPALink.objects.order_by('?')[:3]

    # Retrieve the latest 5 blogs
    latest_links = CPALink.objects.order_by('-created_at')[:3]

    # Retrieve 5 popular blogs (you can define your popularity criteria)
    popular_links = CPALink.objects.order_by('?')[:3]

    context = {'posts': posts,
               'random_cpas': random_cpas,
               'categories_with_links': categories_with_links,
               'featured_blogs': featured_blogs,
               'latest_blogs': latest_blogs,
               'popular_blogs': popular_blogs,
               'featured_links': featured_links,
               'latest_links': latest_links,
               'popular_links': popular_links,
               'some_blogs': some_blogs,
               }
    return render(request, 'index.html', context=context)

def BlogDetailView(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)

    # Retrieve up to 5 related blogs with the same category
    related_blogs = BlogPost.objects.filter(categories__in=post.categories.all()) \
        .exclude(pk=post.pk) \
        .distinct()[:5]

    # Retrieve random 5 featured blogs
    featured_blogs = BlogPost.objects.order_by('?')[:5]

    # Retrieve the latest 5 blogs
    latest_blogs = BlogPost.objects.order_by('-created_at')[:5]

    # Retrieve 5 popular blogs (you can define your popularity criteria)
    popular_blogs = BlogPost.objects.order_by('?')[:5]
    categories_with_count = BlogCategory.objects.annotate(blog_count=Count('blogpost'))


    context = {
        'post': post,
        'blogs': related_blogs,
        'featured_blogs': featured_blogs,
        'latest_blogs': latest_blogs,
        'popular_blogs': popular_blogs,  # Include popular blogs in the context
        'categories_with_count': categories_with_count,
    }

    return render(request, 'single-page.html', context)

def all_blogs_category_wise(request, category_slug=None):
    # Initialize categories queryset
    categories = BlogCategory.objects.all()

    # Initialize blogs queryset
    blogs_queryset = BlogPost.objects.all()

    # Initialize category name (empty by default)
    category_name = None

    # Filter blogs by category if category_slug is provided
    if category_slug:
        category = get_object_or_404(BlogCategory, slug=category_slug)
        blogs_queryset = blogs_queryset.filter(categories=category)
        category_name = category.name  # Set the category name

    # Create a Paginator instance for blogs with 10 items per page
    paginator = Paginator(blogs_queryset, 5)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the Page object for the current page number
    page = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'blogs': page,
        'category_name': category_name,  # Pass the category name to the template
    }

    return render(request, 'category_wise_blog.html', context)

def cpa_detail(request, slug):
    post = get_object_or_404(CPALink, slug=slug)
    context = {
        'cpa': post,
    }

    return render(request, 'cpa_details.html', context)


def contact(request):

    return render(request, 'contact.html')

def privacy(request):

    return render(request, 'privacy.html')

def my_view(request):
    # Retrieve 5 random CPALink objects
    random_cpas = CPALink.objects.order_by('?')[:5]

    context = {
        'random_cpas': random_cpas,
    }

    return render(request, 'base.html', context)