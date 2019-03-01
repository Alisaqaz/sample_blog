from django.urls import path
from . import views

app_name='lib'
urlpatterns=[
	path('',views.index,name='index'),
	path('home/',views.index,name='index'),
	path('detail/',views.detail,name='detail'),
	path('addblog/',views.addblog,name='addblog'),
	path('deleteblog/<int:blog_id>',views.deleteblog,name='deleteblog'),
    path('editSaveblog',views.editSaveblog,name='editSaveblog'),
    path('edit/<int:blog_id>',views.edit,name='edit'),
    path('blog/',views.blog,name='blog'),
]