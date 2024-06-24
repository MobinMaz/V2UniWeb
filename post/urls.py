from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='posts'),
    path('contact/', views.contact, name='post'),
    path('singlepagePost/<int:id>', views.singlepagePost, name='singlepage'),
    path('singlepageVideo/<int:id>', views.singlepageVideo, name='singlepageVideo'),
    path('singlepageteacher/<int:id>', views.singlepageteacher, name='singlepageVideo'),
    path('singlepageVipUser/<int:id>', views.singlepageVipUser, name='singlepageVideo'),
    path('LogIn/', views.logInView, name='LogIn'),
    path('LogIn1/<int:id>', views.logInView1, name='LogIn'),
    path('LogInReq/', views.Login, name='LogInReq'),
    path('LogOut/', views.LogOut, name='LogOut'),
    path('signIN/', views.signIN, name='signIN'),
    path('comment/<int:id>/', views.commentRegister, name='comment'),
    path('signInReq/', views.signInReq, name='signInReq'),
    path('video/', views.Video, name='video'),
    path('teacher/', views.teacher, name='video'),
    path('VipUser/', views.VipUser, name='video'),
    path('Certificate/<int:id>/', views.Certificate, name='certificate'),
]