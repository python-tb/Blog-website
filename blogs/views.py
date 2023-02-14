from django.shortcuts import render, redirect
from blogs.models import Blog, Category
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages

# Create your views here.

@login_required(login_url="/login")
def home(request):
    categories = Category.objects.all()
    blogs = Blog.objects.all()
    lifestyle_blog = Blog.objects.all()
    for i in lifestyle_blog:
        if i.category.name == 'Food':
            print(i)
    return render(request, 'index.html', {'blogs': blogs, 'categories': categories})

def blog(request, id):
    blogs = Blog.objects.all()
    blog = Blog.objects.get(id=id)
    categories = Category.objects.all()
    context = {'blog': blog, 'all_blogs': blogs, 'categories': categories}
    return render(request, 'blog.html', context)

def add_blog(request):
    if request.method == "POST":
        title = request.POST['title'] 
        description = request.POST['description'] 
        category = request.POST['category'] 
        author = request.POST['author'] 
        image = request.FILES['image'] 

        # print(title, description, category, author, image)

        new_blog = Blog(title=title, description=description, category=category, image=image, author=author)
        new_blog.save()

        return redirect("/")
    else:
        return render(request, 'add_blog.html')

def login(request):
    if request.method == "POST":
        entered_username = request.POST['username']
        entered_password = request.POST['password']

        user = auth.authenticate(username=entered_username, password=entered_password)
        print(user)
        if user is not None:
            auth.login(request, user)   # login method starts a cookie-based session for that particular user.
            return redirect("/")
        else:
            messages.info(request, "Invalid Username or Password")
            return redirect("/login")
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        entered_email = request.POST['email']
        entered_firstname = request.POST['firstname']
        entered_lastname = request.POST['lastname']
        entered_username = request.POST['username']
        entered_password = request.POST['password']

        if User.objects.filter(email=entered_email).exists():
            messages.info(request, "Email is already in use")
            return redirect("/signup")

        if User.objects.filter(username=entered_username).exists():
            messages.info(request, "Username already exists")
            return redirect("/signup")

        new_user = User.objects.create_user(username=entered_username, email=entered_email, first_name=entered_firstname, last_name=entered_lastname, password=entered_password)

        new_user.save()

        return redirect("/login")
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def categorywise(request, id):
    category = Category.objects.get(id=id)
    categories = Category.objects.all()
    blogs = Blog.objects.filter(category=category)
    return render(request, 'category.html', {'blogs': blogs, 'categories': categories})