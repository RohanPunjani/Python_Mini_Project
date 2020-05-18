from django.contrib.auth.models import User, auth
from django.shortcuts import HttpResponse, redirect, render
from django.http import JsonResponse
from .models import blog, block
from django.db.models import Q, Value
from django.db.models.functions import Concat
import json

# Create your views here.


def index(request):
    if(not request.user.is_authenticated):
        return render(request, 'minimal_blog.html', {})
    if(request.method=="GET"):
        try:
            if(request.GET['search']):
                search_query = request.GET['search']
                feeds = blog.objects.filter(Q(heading__icontains=search_query), isPublished=True)
                status = 1
                if(len(feeds)==0):
                    queryset = User.objects.annotate(fullname=Concat('first_name', Value(' '), 'last_name'))
                    feeds = queryset.filter(Q(fullname_search=search_query)).blog_set.all()
                    if(len(feeds)==0):
                        status = -1
                        feeds = blog.objects.filter(isPublished=True).order_by('?')
                        return render(request, 'userhome.html', {
                            'status': status,
                            'feeds':feeds
                        })
        except:
            status = 0
            feeds = blog.objects.filter(isPublished=True).order_by('?')
            pass
    else:
        status = 0
        feeds = blog.objects.filter(isPublished=True).order_by('?')
    return render(request, 'userhome.html', {
        "feeds": feeds,
        'status':status
    })


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
    blocks = blog.block_set.all().order_by('position')
    return render(request, 'edit.html',
                {
                    'feed': blog,
                    'blocks': blocks
                }
                )

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
    if request.method=='POST':
        position = request.POST['edit_position']
        title = request.POST['edit_title']
        content = request.POST['edit_content']
        image = request.FILES.get('edit_image',False)
        block_id = request.POST['block_id']
        b = blog.block_set.get(pk=block_id)
        b.title = title
        b.content = content
        b.image = image
        b.position = position
        b.save()
    blocks = blog.block_set.all().order_by('position')
    url = '../../../edit/' + str(id)
    return redirect(url)

def search_view(request):
    if(not request.user.is_authenticated):
        return redirect('/')
    return render(request, '', {})
# def create_blog(request, heading):
#     if (not request.user.is_authenticated):
#         return redirect('')
#     user = request.user
#     blog = user.blog_set.create(heading=heading)
#     return redirect('/')
#
def create_block(request, id):
    if (not request.user.is_authenticated):
        return redirect('/')
    user = request.user
    blog = user.blog_set.get(id=id)
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image',False)
        length = len(blog.block_set.all())+1
        b = blog.block_set.create(blog=blog, title=title, content=content, image=image, position=length) # create a new block of that kind :)
    blocks = blog.block_set.all().order_by('position')
    url = '../../../edit/'+str(id)
    return redirect(url)
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

