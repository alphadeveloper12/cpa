from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager  # Import the TaggableManager
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from colorfield.fields import ColorField
# Model for Blog Categories (same as before)


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

# Model for Blog Posts with an Image Field
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(BlogCategory)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog_images/')  # Add an image field
    tags = TaggableManager()  # Add the tags field
    slug = models.SlugField(unique=True, max_length=255)  # Add the slug field

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while BlogPost.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

class CPACategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class CPALink(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(upload_to='cpa_links/title_images/')
    background_image = models.ImageField(upload_to='cpa_links/background_images/')
    product_image = models.ImageField(upload_to='cpa_links/product_images/')
    text = models.CharField(max_length=100)
    category = models.ForeignKey(CPACategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField()
    slug = models.SlugField(unique=True, max_length=255)  # Add the slug field
    color = ColorField(default='#ffffff')  # Color picker field
    button_text = models.CharField(max_length=50)  # Field for button text

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

