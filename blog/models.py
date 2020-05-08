from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100)
    cover_img = models.ImageField(upload_to='blog_covers/%y/%m/%d', default='blog_covers/img5.jpg')
    isPublished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.heading


class block(models.Model):
    blog = models.ForeignKey(blog, on_delete=models.CASCADE)
    position = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    content = models.TextField()
    isMerged = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
