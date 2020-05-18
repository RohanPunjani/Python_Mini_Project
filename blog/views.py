from django.contrib.auth.models import User, auth
from django.shortcuts import HttpResponse, redirect, render
from django.http import JsonResponse
from .models import blog, block
import json

# Create your views here.


def index(request):
    if(request.user.is_authenticated):
        feeds = blog.objects.filter(isPublished=True).order_by('?')
        return render(request, 'userhome.html', {
            "feeds": feeds,
        })
    else:
        return render(request, 'minimal_blog.html', {})


def view_blog(request, id):
    if(not request.user.is_authenticated):
        return redirect('/')
    feed = blog.objects.get(pk=id)
    feed.views = feed.views + 1
    feed.save()
    blocks = feed.block_set.all().order_by('position')
    return render(request, 'view.html', {
        "feed" : feed,
        "blocks": blocks
    })

def drafts(request):
    if(request.user.is_authenticated):
        user = request.user
        if request.method == 'POST':
            cover_img = request.FILES['cover_img']
            title = request.POST['title']
            blog = user.blog_set.create(heading=title, cover_img=cover_img) #creates a new blog
        drafts = user.blog_set.filter(isPublished=False).order_by('-id')
        return render(request, 'drafts.html', {
            'drafted_feeds': drafts,
        })
    else:
        return redirect('/')

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
        return redirect('/')
    user = request.user
    blog = user.blog_set.get(id=id)
    if blog: # if it exists for that user
        if request.method == "POST":
            title = request.POST['title']
            content = request.POST['content']
            image = request.FILES.get('image',False)
            length = len(blog.block_set.all())+1
            b = blog.block_set.create(blog=blog, title=title, content=content, image=image, position=length) # create a new block of that kind :)
        blocks = blog.block_set.all().order_by('position')
        return render(request, 'edit.html',
                    {
                        'feed': blog,
                        'blocks': blocks
                    }
                    )
    else:
        return redirect('/')


def delete_blog(request, id):
    if (not request.user.is_authenticated):
        return redirect('/')
    user = request.user
    blog = user.blog_set.get(id=id)
    blog.delete()
    return redirect('/drafts')


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

def delete_block(request, id, blockid):
    if (not request.user.is_authenticated):
        return redirect('/')
    user = request.user
    user.blog_set.get(id=id).block_set.filter(
        id=blockid).delete()
    url = '/edit/'+str(id)
    return redirect(url)


def update_position(request,id):
    if(not request.user.is_authenticated):
        return redirect('/')
    user = request.user
    blog = user.blog_set.get(id=id)
    data = request.POST.getlist('data[]')

    for blocks in data:
        blocks = json.loads(blocks)
        for i in range(len(blocks)):
            block_id = blocks[i]['block_id']
            position = blocks[i]['position']
            b = blog.block_set.get(pk=block_id)
            b.position = position
            b.save()
    return JsonResponse({
        'message': "Success"
    })

def update_block(request,id):
    if(not request.user.is_authenticated):
        return redirect('/')
    user = request.user
    blog = user.blog_set.get(id=id)
    


# def create_blog(request, heading):
#     if (not request.user.is_authenticated):
#         return redirect('')
#     user = request.user
#     blog = user.blog_set.create(heading=heading)
#     return redirect('/')
#
# def create_block(request, id, title, content):
#     if (not request.user.is_authenticated):
#         return redirect('/')
#     user = request.user
#     blog = user.blog_set.get(id=id)
#     content = content.replace('\n', '<br>')
#     blog.block_set.create(title=title, content=content)
#     url = '/edit/'+str(id)
#     return redirect(url)
#
# def update_block(request, blogId, id, isMerged):
#     if (not request.user.is_authenticated):
#         return redirect('/')
#     user = request.user
#     if isMerged == 'True':
#         isM = True
#     else:
#         isM = False
#     user.blog_set.get(id=blogId).block_set.filter(
#         id=id).update(isMerged=isM)
#     url = '/edit/'+str(blogId)
#     return redirect(url)
#
# def update_block_content(request, blogId, id, title, content):
#     if (not request.user.is_authenticated):
#         return redirect('/')
#     content = content.replace('\n', '<br>')
#     user = request.user
#     user.blog_set.get(id=blogId).block_set.filter(
#         id=id).update(title=title, content=content)
#     url = '/edit/'+str(blogId)
#     return redirect(url)

