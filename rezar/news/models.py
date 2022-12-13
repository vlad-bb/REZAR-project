from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, blank=False)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='news/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
