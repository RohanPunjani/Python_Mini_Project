from django.db import models

# Create your models here.


class blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.heading


class block(models.Model):
    block_id = models.AutoField(primary_key=True)
    blog_id = models.ForeignKey(blog, on_delete=models.CASCADE)
    position = models.IntegerField()
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title
