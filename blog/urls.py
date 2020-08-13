from	django.urls	import	path
from django.conf.urls import url 
from	.	import	views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns	=	[				
	path('',	views.post_list,	name='post_list'),
	path('blogging/', views.blogging , name='blogging'),
	path('Portfolio/', views.Portfolio, name='Portfolio'), 
	path('Resume/', views.Resume, name= 'Resume'),
	path('post/<int:pk>/',	views.post_detail,	name='post_detail'), 
	path('post/new/',	views.post_new,	name='post_new'),
	path('post/<int:pk>/edit/',	views.post_edit,	name='post_edit'),
	#url(r'^results/$', search, name= "search"),
]
urlpatterns += staticfiles_urlpatterns()