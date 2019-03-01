# mysite/lib/views.py
from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator

def detail(request):
    blog_list = Blog.objects.order_by('-date')[:5]
    context = {'blog_list': blog_list}
    return render(request, 'lib/detail.html', context)

def blog(request):
    blog_list = Blog.objects.order_by('-date')
    context = {'blog_list': blog_list}
    blog_list_all=Blog.objects.order_by('-date')
    limit = 5
    paginator=Paginator(blog_list_all,limit)
    page=request.GET.get('page','1')
    result=paginator.page(page)
    return render(request,'lib/blog.html',locals())


def index(request):
    return render(request,'lib/base.html')
	
def addblog(request):
    if request.method =="POST":
        temp_author = "Alisa"
        temp_title=request.POST['title']
        temp_content=request.POST['content']
    
    from django.utils import timezone
    temp_blog =Blog(author=temp_author,title=temp_title,date=timezone.now(),content=temp_content)
    temp_blog.save()
    return HttpResponseRedirect(reverse('lib:blog'))
   # messages.info(request,"Successfully！")
   
	
def deleteblog(request,blog_id):
    blogID=blog_id
    Blog.objects.filter(id=blogID).delete()
    return HttpResponseRedirect(reverse('lib:blog'))

def edit(request,blog_id):
    blogID=blog_id
    print("id:",blogID)
    blogInfo = Blog.objects.get(id=blogID)
    return render(request,'lib/edit.html',{'blog_id':blogID,'author':blogInfo.author,'title':blogInfo.title,'content':blogInfo.content})

def editSaveblog(request):

    if request.method =="POST":
        blogid=request.POST['blog_id']
        temp_author = "Alisa"
        temp_title=request.POST['title']
        temp_content=request.POST['content']
    from django.utils import timezone
    entry =Blog.objects.get(id=blogid)
    cur_author=temp_author
    cur_title=temp_title
    cur_content=temp_content
    print("saveresult",cur_title)
    entry.author=cur_author
    entry.title=cur_title
    entry.date=timezone.now()
    entry.content=cur_content
    entry.save()
    blog_list = Blog.objects.order_by('-date')
    context = {'blog_list': blog_list}
    blog_list_all=Blog.objects.order_by('-date')
    limit = 5
    paginator=Paginator(blog_list_all,limit)
    page=request.GET.get('page','1')
    result=paginator.page(page)
    return render(request,'lib/blog.html',locals())
