from	django.urls	import	path 
from	.	import	views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns	=	[				
	path('',	views.post_list,	name='post_list'),
	path('blogging/', views.blogging , name='blogging'), 
]
urlpatterns += staticfiles_urlpatterns()