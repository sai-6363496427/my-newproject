from django.shortcuts import render,get_object_or_404,redirect
from jobpostapp.models import job_posts
from django.views.generic import DetailView,CreateView
from jobpostapp.models import job
from jobpostapp.forms import sai,kumar,com
from jobpostapp.models import add_job,comment
from django.http import HttpResponseRedirect
from django.urls import reverse

# from firstapp.models import 


# Create your views here.
def don(request):
    newjobs = job_posts.objects.all()
    return render(request,"jobposts/index.html",{"newjobs":newjobs})

class company_details(DetailView):
    context_object_name = 'job_details'
    model = job_posts


def jobs(request):
    form = sai
    submit = False
    if request.method == 'POST':
        form = sai(request.POST)
        if form.is_valid() :
            form.save()
            

            submit = True
            print("Submitted sucessfulley")
    return render(request,'jobposts/create.html',{"form":form,"submit":submit})

def apply(request):
    pavan = job.objects.all()
    return render(request,"applyed.html",{'pavan':pavan})

def posted(request):
    form = kumar()
    if request.method =='POST':
        form=kumar(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        
    return render(request,"jobposts/add_post.html",{"form":form})

def blogs(request):
    form=add_job.objects.all()
    return render(request,"blog.html",{"form":form})

def blogdetail(request,id):
    loby=add_job.objects.get(id=id)
    var = add_job.objects.all()
    sonu=add_job.objects.all().order_by("-view_count")[0:3]
    so=add_job.objects.all().order_by("-view_count")[0:1]
    son=add_job.objects.all().order_by("-Time")[0:3]
    comm = com()
    #likes
    liked=False
    if loby.likes.filter(id=request.user.id).exists():
        liked=True
    post_is_liked = liked
    number_of_likes = loby.no_of_likes()


    #Bookmarks

    book=False
    if loby.bookmarks.filter(id=request.user.id).exists():
        book=True
    post_is_click = book
    



    print("hello")
    if request.method == 'POST':
        comm_form=com(request.POST)
        if comm_form.is_valid:
            parent_obj = None
            print("hi")
            if request.POST.get('parent'):
                # save reply
                parent=request.POST.get('parent')
                parent_obj = comment.objects.get(id=parent)
                if parent_obj:
                    comment_reply = comm_form.save(commit=False)
                    comment_reply.parent = parent_obj
                    comment_reply.post = loby
                    comment_reply.save()
                    
            else:

                comment1 = comm_form.save(commit=False)
                # comment.user = request.user
                # comment.loby =loby
                postid = request.POST.get('post_id')
                post = add_job.objects.get(id=postid)
                comment1.post = post 
                comment1.save()
  
    if loby.view_count == None:
        loby.view_count = 1 
    else:
        loby.view_count += 1
    loby.save()

    usercomment = comment.objects.filter(post=loby)
    

    return render(request,"blog_details.html",{"loby":loby, "comm":comm,"usercomment":usercomment,'var':var,'post_is_liked':post_is_liked,'number_of_likes':number_of_likes,'post_is_click':post_is_click,'son':son,'so':so,'sonu':sonu})

# def search(request):
#     res = request.GET.get('qry')
#     search_qry = job_posts.objects.filter(title__icontains = res)
#     print(search_qry)

#     return render(request,'jobposts/search.html',{'search_qry':search_qry})
def search(request):
    py = add_job.objects.all().order_by("-view_count")[0:3]
    spider = add_job.objects.all().order_by("-Time")[0:3]
    if request.method == 'POST':
        search_qry = request.POST['search_qry']
        posts = add_job.objects.filter(Post_title__contains = search_qry)
        print(search_qry)
        return render(request, 'jobposts/search.html', {'search_qry':search_qry, 'posts':posts,'py':py,'spider':spider})
    else:
        return render(request, 'jobposts/search.html',{'py':py,'spider':spider})
    


def like_post(request,id):
    print(request.POST.get('post_id'))
    posts = get_object_or_404(add_job,id=request.POST.get('post_id'))
    if posts.likes.filter(id=request.user.id).exists():
        posts.likes.remove(request.user)
        print("hello hi")
    else:
        posts.likes.add(request.user)
        print("error")
    return redirect('blogdetail',id=id)
    # return HttpResponseRedirect(reverse('blogdetail',id=id))

def bookmarks(request,id):
    post=get_object_or_404(add_job,id=request.POST.get('post_id'))
    if post.bookmarks.filter(id=request.user.id):
        post.bookmarks.remove(request.user)
    else:
        post.bookmarks.add(request.user)
    return redirect('blogdetail',id=id)
    # return HttpResponseRedirect(reverse('blogdetail',id=id))

def book_post(request):
    let=add_job.objects.filter(bookmarks=request.user)
    
    return render(request,"jobposts/bookmark.html",{'let':let})

def liked_post(request):
    var=add_job.objects.filter(likes=request.user)
    return render(request,'jobposts/likes.html',{'var':var})



