# Generated by Django 3.0.5 on 2020-05-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_blog_cover_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover_img',
            field=models.ImageField(default='images/img3.svg', upload_to='blog/static/blog_covers/'),
        ),
    ]
