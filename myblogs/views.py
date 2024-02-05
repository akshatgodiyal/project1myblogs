from django.shortcuts import render
from django.http import HttpResponse
from .models import blog_category,contact_info,SubscribedUser,blog_post,blog_comment
from .forms import BlogPost_Form,Blog_Form
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
def home(request):
         # return HttpResponse('<h1>This is the Home Page</h1>')
    x=blog_category.objects.all()
    print(x)
    return render(request,'myblogs/home.html',{'category':x})
def contact(request):
          #return HttpResponse('<h1>This is the Contact Page</h1>')
 
 if request.method == 'GET':
        return render(request, 'myblogs/contact.html')
 elif request.method == 'POST':
        email = request.POST.get('user_email')
        message = request.POST.get('message')
        x = contact_info(u_email=email, u_message=message)
        x.save()
        print(email)
        print(message)
        return render(request,'myblogs/contact.html',{'feedback':'Your message has been recorded'})
 

def home(request):
    # Fetch the data from db
    x = blog_category.objects.all()
    print(x)

    if request.method == 'GET':
        return render(request, 'myblogs/home.html', {"category": x})
    elif request.method == 'POST':
        email = request.POST.get('s_email')

        # Check if the email already exists
        existing_subscription = SubscribedUser.objects.filter(sub_email=email).exists()

        if not existing_subscription:
            # If the email doesn't exist, create a new subscription
            new_subscription = SubscribedUser(sub_email=email)
            new_subscription.save()
            return render(request, 'myblogs/home.html', {'feedback': 'Your message has been recorded', "category": x})
        
        # If the email already exists, display a message
        return render(request, 'myblogs/home.html', {'feedback': 'This email is already subscribed', "category": x})
def blog(request):
    # Extract the category from the request parameters
    category_name = request.GET.get('category')

    # If a category is provided, filter blog posts by that category, otherwise, get all blog posts
    if category_name:
        blogs = blog_post.objects.filter(blog_cat__blog_cat=category_name)
    else:
        blogs = blog_post.objects.all()
    
    p = Paginator(blogs, 2)
    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)

    return render(request, 'myblogs/blog.html', {"blogs": page_obj, "category": category_name})

def ck(request):
    x = BlogPost_Form()
    return render(request,'myblogs/ck.html',{"x":x}) 

def allblogs(request):
    y=blog_post.objects.all()
    return render(request,'myblogs/allblogs.html',{"y":y})

def blog_details(request, blog_id):
    obj = get_object_or_404(blog_post, pk=blog_id)
    z=obj.view_count
    z=z+1
    obj.view_count=z
    obj.save()
    print(obj)
    print(blog_id)
    _comments=blog_comment.objects.filter(blog_id=blog_id)

    return render(request,'myblogs/blog_details.html', {"obj":obj,"comments":_comments})
    # return HttpResponse('blog_details')


def loginuser(request):
    if request.method == 'GET':
        return render(request,'myblogs/loginuser.html',{'form':AuthenticationForm()})
    else:
        a=request.POST.get('username')
        b=request.POST.get('password')
        user=authenticate(request, username=a,password=b)
        if user is None:
            return render(request,'myblogs/loginuser.html',{'form':AuthenticationForm(),'error':'Invalid Credentials'})
        else:
            login(request,user)
            return redirect('home')
    

def signupuser(request):
    if request.method =='GET':
        return render(request,'myblogs/signupuser.html',{'form':UserCreationForm()})
    else:
        a=request.POST.get('username')
        b=request.POST.get('password1')
        c=request.POST.get('password2')
        if b==c:
            #check whether username is unique
            if(User.objects.filter(username=a)):
                return render(request,'myblogs/signupuser.html',{'form':UserCreationForm(),'error':'Username Already Exist'})
            else:
                user=User.objects.create_user(username=a,password=b)
                user.save()
                login(request,user)
                return redirect('home')
        else:
            #when password mismatch
            return render(request,'myblogs/signupuser.html',{'form':UserCreationForm(),'error':'password mistmatch Try Again...'})
    
def logoutuser(request):
    if request.method =='GET':
        logout(request)
        return redirect('home')

def searching(request):
    if request.method=="POST":
        x=request.POST.get('prodsearch')
        mydata=blog_category.objects.filter(Q(blog_cat__icontains=x) | Q(blogcat_description__icontains=x))
        if mydata:
            return render(request,'myblogs/home.html',{'category':mydata})
        else:
            return render(request,'myblogs/home.html',{'warning':'data not found'})
        
def aboutus(request):
    if request.method=="GET":
        return render(request,'myblogs/aboutus.html')

def add_like(request, blog_id):
    obj = get_object_or_404(blog_post, pk=blog_id)
    print (obj.like_count)
    y=obj.like_count
    y=y+1
    obj.like_count=y
    obj.save()
    return redirect('blog_details', obj.id)

def comments(request,blog_id):
        com = request.POST.get('comment1')
        print(com)
        x = blog_comment(u_comment=com, blog_id=blog_id)
        x.save()

        return redirect('/blog_details/'+blog_id)

