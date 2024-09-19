from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post

# Create your views here.

def index(request):
    return render(request, 'index.html')

def customer(request):
    if request.method == 'POST':
        FullName = request.POST['FullName']
        email = request.POST['email']
        phoneNumber = request.POST['phoneNumber']
        subject = request.POST['subject']
        message_body = request.POST['message_body']

        posts = Post.objects.create(FullName = FullName, email = email, phoneNumber = phoneNumber, subject = subject, message_body = message_body)
        posts.save()

        messages.info(request, "Details Sumbitted Successfully")
        
    else:
        
        return render(request, 'customer.html')
        
    return render(request, 'customer.html')
    
def about(request):
    return render(request, 'about.html')


def post(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})

def portfolio(request):
    return render(request, 'portfolio.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/post')
        else:
            message.info(request, "Invalid Login Details")
            return redirect('/login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def read(request, pk):
    reads= Post.objects.get(id=pk)
    return render(request, 'read.html', {'reads': reads})

def deleteMessage(request, pk):
    reads= Post.objects.get(id=pk)
    reads.delete()
    return redirect('/post')
