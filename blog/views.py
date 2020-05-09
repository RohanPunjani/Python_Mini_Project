from django.shortcuts import render, redirect, HttpResponse
from .models import blog
from django.contrib.auth.models import User, auth
# Create your views here.


def index(request):
    if(request.user.is_authenticated):
        feeds = blog.objects.filter(isPublished=True).order_by('?')
        return render(request, 'userhome.html', {
            "feeds": feeds,
        })
    else:
        return render(request, 'minimal_blog.html', {})


def drafts(request):
    if(request.user.is_authenticated):
        user = request.user
        if request.method == 'POST':
            cover_img = request.FILES['cover_img']
            title = request.POST['title']
            blog = user.blog_set.create(heading=title, cover_img=cover_img)
        drafts = user.blog_set.filter(isPublished=False).order_by('-id')
        return render(request, 'drafts.html', {
            'drafted_feeds': drafts,
        })
    else:
        return redirect('/')

def view_blog(request, id):
    if(not request.user.is_authenticated):
        return redirect('/')
    feed = blog.objects.get(pk=id)
    feed.views = feed.views + 1
    feed.save()
    return render(request, 'view.html', {"feed" : feed})

def published(request):
    if(request.user.is_authenticated):
        user = request.user
        published = user.blog_set.filter(isPublished=True).order_by('-id')
        return render(request, 'published.html', {
            'published_feeds': published,
        })
    else:
        return redirect('/')



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
    return redirect('/drafts')


def create_blog(request, heading):
    if (not request.user.is_authenticated):
        return redirect('')
    user = request.user
    blog = user.blog_set.create(heading=heading)
    return redirect('/')


def publish_blog(request, id):
    if (not request.user.is_authenticated):
        return redirect('/')
    user = request.user
    user.blog_set.filter(id=id).update(isPublished=True)
    return redirect('/')

def unpublish_blog(request, id):
    if (not request.user.is_authenticated):
        return redirect('/')
    user = request.user
    user.blog_set.filter(id=id).update(isPublished=False)
    return redirect('/published')


def create_block(request, id, title, content):
    if (not request.user.is_authenticated):
        return redirect('/')
    user = request.user
    blog = user.blog_set.get(id=id)
    content = content.replace('\n', '<br>')
    blog.block_set.create(title=title, content=content)
    url = '/edit/'+str(id)
    return redirect(url)


def update_block(request, blogId, id, isMerged):
    if (not request.user.is_authenticated):
        return redirect('/')
    user = request.user
    if isMerged == 'True':
        isM = True
    else:
        isM = False
    user.blog_set.get(id=blogId).block_set.filter(
        id=id).update(isMerged=isM)
    url = '/edit/'+str(blogId)
    return redirect(url)


def update_block_content(request, blogId, id, title, content):
    if (not request.user.is_authenticated):
        return redirect('/')
    content = content.replace('\n', '<br>')
    user = request.user
    user.blog_set.get(id=blogId).block_set.filter(
        id=id).update(title=title, content=content)
    url = '/edit/'+str(blogId)
    return redirect(url)


def delete_block(request, id, blockid):
    if (not request.user.is_authenticated):
        return redirect('/')
    user = request.user
    user.blog_set.get(id=id).block_set.filter(
        id=blockid).delete()
    url = '/edit/'+str(id)
    return redirect(url)
