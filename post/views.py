from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . import loginForm , commentForm ,signForm
from django.contrib import messages
from tkinter import messagebox
import os

from .admin import userAdmin


# Create your views here.
def index(request):
    posts = models.post.objects.all().order_by('-pub_date')[0:6]
    for post in posts:
        if post.pub_date.minute <10:
            post.pub_date=str(post.pub_date.year)+'-'+str(post.pub_date.month)+'-'+str(post.pub_date.day)+' '+str(post.pub_date.hour)+': 0'+str(post.pub_date.minute)
        else:
            post.pub_date= str(post.pub_date.year) + '-' + str(post.pub_date.month) + '-' + str(post.pub_date.day) + ' ' + str(post.pub_date.hour)+': '+str(post.pub_date.minute)
    top4post=[]
    try:
        top4post=posts[0:4]
    except:
        top4post=posts
    postVIP=posts[0]
    form=commentForm.CommentForm()
    users = models.user.objects.filter(teacher=True).all()
    users1 = models.user.objects.filter(ForumsMember=True).all()
    videos = models.videoclass.objects.all()
    for user in users:
        user.password=0
    return render(request, 'index.html',context={'posts':posts,'toppost':top4post,'users':users,'users1':users1,'videos':videos,'form':form,'postVIP':postVIP})
def blog(request):
    posts = models.post.objects.all().order_by('-id')
    for post in posts:
        if post.pub_date.minute < 10:
            post.pub_date = str(post.pub_date.year) + '-' + str(post.pub_date.month) + '-' + str(
                post.pub_date.day) + ' ' + str(post.pub_date.hour) + ': 0' + str(post.pub_date.minute)
        else:
            post.pub_date = str(post.pub_date.year) + '-' + str(post.pub_date.month) + '-' + str(
                post.pub_date.day) + ' ' + str(post.pub_date.hour) + ': ' + str(post.pub_date.minute)

    return render(request, 'blog.html',context={'posts':posts})
def contact(request):
    return render(request=request,template_name='Contact_us.html')
def singlepagePost(request,id):
    post=models.post.objects.get(id=id)
    images=models.ImageCollection.objects.filter(post=post).all()
    fistImage=0
    if len(images) != 0:
        fistImage = images[0]
        images = images[1:]
    else:
        images=0
    if post.pub_date.minute < 10:
        post.pub_date = str(post.pub_date.year) + '-' + str(post.pub_date.month) + '-' + str(post.pub_date.day) + ' '+' ساعت :' + str(post.pub_date.hour) + ': 0' + str(post.pub_date.minute)
    else:
        post.pub_date = str(post.pub_date.year) + '-' + str(post.pub_date.month) + '-' + str(post.pub_date.day) + ' ' + str(post.pub_date.hour)+ ': ' + str(post.pub_date.minute)

    content=models.largeContent.objects.filter(post=post).all()
    return render(request=request,template_name='single.html',context={'post':post,'images':images,'fistImage':fistImage,'content':content})
def logInView(request):
    form = loginForm.LoginForm()

    #messages.success(request,'لظفا برای نوشتن نظر اول وارد شوید !')
    #    return render(request=request, template_name='loginForm.html', context={'form': form})

    return render(request=request,template_name='loginForm.html',context={'form':form})
def logInView1(request,id):
     form = loginForm.LoginForm()
     messages.success(request,'لظفا برای نوشتن نظر اول وارد شوید !')
     return render(request=request, template_name='loginForm.html', context={'form': form})

def Login(request):
    posts = models.post.objects.all().order_by('-id')
    users = models.user.objects.all()
    videos = models.videoclass.objects.all()
    for user in users:
        user.password = 0
    if request.method=='POST':
        form=loginForm.LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(username=email,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'با موفقیت وارد شدید!')
                messageTmp=''
                return render(request=request,template_name='index.html',context={'posts':posts,'users':users,'videos':videos,'user.id':user.id,'messageTmp':messageTmp})
            else :
                messages.success(request,"رمز عبورتون یا نام کاربری درست نمی باشد")
                return redirect('LogIn')
        else:
            messages.error(request,'در ورود شما مشکلی پیش آمد!')
            return redirect('login')
def LogOut(request):
    logout(request)
    messages.success(request,'خروج شما موفق بود!')
    return redirect ('index')
def commentRegister(request,id):
    message=request.GET.get('comment')
    comment=models.comment(text=message,user_id=id)
    comment.save()
    return redirect('index')

def signIN(request):
    form= signForm.SignForm()
    return render(request=request,template_name='singInForm.html',context={'form':form})
def signInReq(request):
    if request.method=='POST':
        form=signForm.SignForm(data=request.POST)
        if form.is_valid():
            users = models.user.objects.filter(email=form.cleaned_data['email']).all()
            if form.cleaned_data['password']==form.cleaned_data['repassword']:
                if len(users)==0:
                    form.save()
                    user=User.objects.create_user(form.cleaned_data['name'],form.cleaned_data['email'],form.cleaned_data['password'])
                    user.set_password(form.cleaned_data['password'])
                    user.save()
                    user=authenticate(request,username=form.cleaned_data['name'],password=form.cleaned_data['password'])
                    login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                    return redirect('index')
                else:
                    messages.success(request, 'فردی با این مشخصات قبلا ثبت نام کرده لطفا از ایمیل دیگری استفاده کنید')
                    return redirect('signIN')
            else:
                messages.success(request, '۲ فیلد پسورد با هم فرق میکنن دقت کن دانشجوی گل!')
                return redirect('signIN')
        elif any(char.isalpha() for char in form.data['studentCode']):
            messages.success(request,'لطفا در فیلد کد داشنجویی فقط عدد وارد کنید')
            return redirect('signIN')
        else:
            messages.success(request,'در ثبت نام شما مشکلی ایجاد شده است لطفا مجدد امتحان کنید')
    return redirect('index')
def Video(request):
    videos = models.videoclass.objects.all().order_by('-id')
    return render(request=request,template_name='videoPage.html',context={'videos':videos})
def singlepageVideo(request,id):
    video=models.videoclass.objects.get(id=id)
    return render(request=request,template_name='singleVideo.html',context={'post':video})
def teacher(request):
    users = models.user.objects.filter(teacher=True).all()
    return render(request=request,template_name='teacherForm.html',context={'users':users})
def VipUser(request):
    users = models.user.objects.filter(vip=True).all()
    return render(request=request,template_name='vipUserPage.html',context={'users':users})
def singlepageteacher(request,id):
    user = models.user.objects.get(id=id)
    return render(request=request, template_name='singleTeacher.html', context={'user': user})
def singlepageVipUser(request,id):
    user = models.user.objects.get(id=id)
    return render(request=request, template_name='singleVipUser.html', context={'user': user})
def Certificate(request,id):
    user = User.objects.get(id=id)
    if not user.is_staff:
        user1=models.user.objects.get(name=user.username)
        certificate=models.Certificate.objects.filter(user=user1).all()

        if len(certificate)==0:
            messages.success(request,'شما مدرکی ندارید!')
            return redirect('index')
        else:
            return render(request=request,template_name='certificateAll.html',context={'certificate':certificate})
    else:
        messages.success(request,'شما مدیر هستید و منظقا مدرکی ندارید!')
        return redirect('index')
def singleCertificate(request,id):
    certificate=models.Certificate.objects.get(id=id)
    return render(request=request,template_name='singleCertificate.html',context={'certificate':certificate})

def download_pdf(request, post_id):
    post = get_object_or_404(models.post, id=post_id)
    file_path = post.pdf.path if post.pdf else None

    if file_path and os.path.exists(file_path):
        with open(file_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
    else:
        return HttpResponse("File not found", status=404)