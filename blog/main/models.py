from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# model for blog posts
class Post(models.Model):
    post_id = models.CharField(default='', max_length=200)
    title = models.CharField(default='', max_length=200)
    description = models.CharField(default='', max_length=200)
    content = RichTextField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    # string representation of the post
    def __str__(self):
        return f'{self.title}'
