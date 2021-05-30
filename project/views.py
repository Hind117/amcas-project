from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import requests
from django.shortcuts import render, get_object_or_404, redirect
from itertools import chain
from .models import Contact, Article, nasaNew, FilesAdmin, Profile, Topic, Book, MemberPost
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm, CommentForm, MemberPostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.static import serve
from django.db.models import Q
from django.core.exceptions import ValidationError


import os
import json
import datetime
from dateutil import parser
from dateutil.relativedelta import relativedelta


# Create your views here.
def index(request):

    posts = Article.objects.filter(published=True).order_by('-date')[0:2]
    return render(request, 'project/home.html', {'post': posts})

def about(request):
    return render(request, 'project/about.html')

def singlepost(request):
    return render(request, 'project/singlepost.html')


def earthMoon(request):
    return render(request, 'project/earthMoon.html')


def marsMoon(request):
    return render(request, 'project/marsMoon.html')


def mars_moon1(request):
    return render(request, 'project/mars_moon1.html')


def mars_moon2(request):
    return render(request, 'project/mars_moon2.html')


def jupitarMoon(request):
    return render(request, 'project/jupitarMoon.html')


def jupitarMoon1(request):
    return render(request, 'project/jupitarMoon1.html')


def jupitarMoon2(request):
    return render(request, 'project/jupitarMoon2.html')


def jupitarMoon3(request):
    return render(request, 'project/jupitarMoon3.html')


def jupitarMoon4(request):
    return render(request, 'project/jupitarMoon4.html')


def jupitarMoon5(request):
    return render(request, 'project/jupitarMoon5.html')


def saturnMoon(request):
    return render(request, 'project/saturnMoon.html')


def saturnMoon1(request):
    return render(request, 'project/saturnMoon1.html')


def saturnMoon2(request):
    return render(request, 'project/saturnMoon2.html')


def saturnMoon3(request):
    return render(request, 'project/saturnMoon3.html')


def saturnMoon4(request):
    return render(request, 'project/saturnMoon4.html')


def saturnMoon5(request):
    return render(request, 'project/saturnMoon5.html')


def uranusMoon(request):
    return render(request, 'project/uranusMoon.html')

def uranusMoon1(request):
    return render(request, 'project/uranusMoon1.html')

def uranusMoon2(request):
    return render(request, 'project/uranusMoon2.html')

def uranusMoon3(request):
    return render(request, 'project/uranusMoon3.html')

def uranusMoon4(request):
    return render(request, 'project/uranusMoon4.html')

def uranusMoon5(request):
    return render(request, 'project/uranusMoon5.html')

def neptuneMoon(request):
    return render(request, 'project/neptuneMoon.html')

def neptuneMoon1(request):
    return render(request, 'project/neptuneMoon1.html')

def neptuneMoon2(request):
    return render(request, 'project/neptuneMoon2.html')

def neptuneMoon3(request):
    return render(request, 'project/neptuneMoon3.html')

def neptuneMoon4(request):
    return render(request, 'project/neptuneMoon4.html')

def neptuneMoon5(request):
    return render(request, 'project/neptuneMoon5.html')


def blog(request):
    posts = Article.objects.filter(published=True).order_by('-date')[0:3]

    search_post = request.GET.get('search')
    if search_post:
        var_1 = Article.objects.filter(Q(title__icontains=search_post) & Q(body__icontains=search_post))
    else:
        var_1 = Article.objects.all().order_by('-date')
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_visits': num_visits,
        'var_1': var_1,
        'post':posts,
    }
    return render(request, 'project/blog.html', context)


def contact(request):
    if request.method == 'POST':
        Your_name = request.POST.get('name')
        Your_email = request.POST.get('email')
        Subject = request.POST.get('subject')
        Your_Message = request.POST.get('message')

        var_contact = Contact(name=Your_name, email=Your_email, subject=Subject, messages=Your_Message)
        var_contact.save()
        return render(request, 'project/home.html')
    else:
        return render(request, 'project/contact.html')

@login_required(login_url='login')
def post_form(request):
    post_form = MemberPostForm(data=request.POST)
    if request.method == 'POST':

        if post_form.is_valid():
            new_post = post_form.save()
            new_post.save()
            return redirect('blog')
    return render(request, 'project/post_form.html', {'post_form':post_form})



def detail(request, article_id):
    detail_page = get_object_or_404(Article, pk=article_id)
    comments = detail_page.comments.all()
    like_count = detail_page.like_count
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'You have to login to like this post')
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid() and request.user.is_authenticated:
            new_comment = comment_form.save(commit=False)
            new_comment.post = detail_page
            new_comment.save()
            return render(request, 'project/singlepost.html',
                          {'detail_blog': detail_page, 'post': detail_page, 'like_count': like_count,
                           'comments': comments,
                           'new_comment': new_comment,
                           'comment_form': comment_form})
        if request.method == 'POST' and request.user.is_authenticated:
            article_id = get_object_or_404(Article, pk=article_id)
            article_id.like = True
            article_id.like_count += 1
            article_id.save()
            like_count = article_id.like_count
    else:
        comment_form = CommentForm()
    return render(request, 'project/singlepost.html',
                  {'detail_blog': detail_page, 'post': detail_page, 'like_count': like_count,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})



def signup(request):
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'project/signup.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'project/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

def nasa(request):
    search_post = request.GET.get('search')
    if search_post:
        var_2 = nasaNew.objects.filter(Q(title__icontains=search_post) & Q(body__icontains=search_post))
    else:
        var_2 = nasaNew.objects.all().order_by('-date')
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_visits': num_visits,
        'var_2': var_2,
    }
    return render(request, 'project/nasa.html', context)



def detail1(request, nasaNew_id):
    detail_page1 = get_object_or_404(nasaNew, pk=nasaNew_id)
    return render(request, 'project/singlepost1.html', {'detail_blog1': detail_page1})

def planets(request):
    return  render(request, 'project/planets.html')

def mercury(request):
    return render(request, 'project/mercury.html')

def venus(request):
    return render(request, 'project/venus.html')

def earth(request):
    return render(request, 'project/earth.html')

def mars(request):
    return render(request, 'project/mars.html')

def jupiter(request):
    return render(request, 'project/jupiter.html')

def saturn(request):
    return render(request, 'project/saturn.html')

def uranus(request):
    return render(request, 'project/uranus.html')

def neptune(request):
    return render(request, 'project/neptune.html')

def singlepost1(request):
    return render(request, 'project/singlepost1.html')



def events(request):
    context={'file':FilesAdmin.objects.all()}
    return render(request,'project/events.html',context)

@login_required(login_url='login')
def telescope(request):
    return render(request, 'project/telescope.html')


@login_required
def profile(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)


        if u_form.is_valid():
            u_form.save()



            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)



    context = {
        'u_form': u_form,

    }

    return render(request, 'project/profile.html', context)



def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Article, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})



@login_required(login_url='login')
def topics(request):
    topics = Topic.objects.order_by('-time')
    context={'topics':topics}
    return render(request, 'project/topics.html', context=context)


def library(request):
    books = Book.objects.order_by('-time')
    context={'books':books}
    return render(request, 'project/library.html', context=context)


@login_required(login_url='login')
def downtopics(request, file):
    top = Topic.objects.get(id=file)

    filepath = top.pdfupload.path

    return serve(request, os.path.basename(filepath),os.path.dirname(filepath))

def countdown(request):
    a = '2061-07-27T17:00:00.000-07:00'
    date = parser.parse(a)
    b = datetime.datetime.now().astimezone()
    diff = relativedelta(date, b)
    print(diff)

    context = {'date':'2061-07-27T17:00:00.000-07:00', 'formatted_date':'JULY 27, 2061','year':diff.years, 'mon':diff.months, 'day':diff.days}
    return render(request, 'project/countdown.html', context=context)


