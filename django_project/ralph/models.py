from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    profile = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.username


class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField()
    imgUrl = models.ImageField(upload_to='images/')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption


class Like(models.Model):
    likeId = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
