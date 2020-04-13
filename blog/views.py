from django.shortcuts import render, redirect
from .models import blog
from django.contrib.auth.models import User, auth
# Create your views here.


def index(request):
    if(request.user.is_authenticated):
        user = request.user
        published = user.blog_set.filter(isPublished=True).order_by('-id')
        drafts = user.blog_set.filter(isPublished=False).order_by('-id')
        return render(request, 'blog.html', {
            "drafts": drafts,
            "published": published,
        })
    else:
        return render(request, 'blog.html', {'blog': None})


def edit_blog(request, id):
    if (not request.user.is_authenticated):
        return redirect('')
    user = request.user
    blog = user.blog_set.get(id=id)
    merged_block = blog.block_set.filter(isMerged=True)
    unmerged_block = blog.block_set.filter(isMerged=False)
    return render(request, 'content.html',
                  {
                      'blog': blog,
                      'merged_block': merged_block,
                      'unmerged_block': unmerged_block
                  }
                  )


def delete_blog(request, id):
    if (not request.user.is_authenticated):
        return redirect('/')
    user = request.user
    blog = user.blog_set.get(id=id)
    blog.delete()
    return redirect('/')


def create_blog(request, heading):
    if (not request.user.is_authenticated):
        return redirect('')
    user = request.user
    blog = user.blog_set.create(heading=heading)
    print(blog.id)
    # return render(request, "./edit/{{blog.id}}")
    return redirect('/')


def publish_blog(request, id):
    if (not request.user.is_authenticated):
        return redirect('/')
    user = request.user
    user.blog_set.filter(id=id).update(isPublished=True)
    return redirect('/')
