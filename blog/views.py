import operator
from django.db.models import Q
from	django.shortcuts	import	render 
from	django.utils	import	timezone 
from	.models	import	Post
from	django.shortcuts	import	render,	get_object_or_404
from	.forms	import	PostForm
from django.shortcuts import redirect




def	post_list(request):				
	posts	=	Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')				
	return	render(request,	'blog/post_list.html',	{'posts':	posts})
def blogging(request):
	posts	=	Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/blogging.html', {'posts':	posts})

def Portfolio(request):
	return render(request, 'blog/Portfolio.html')

def Resume(request):
	return render(request, 'blog/Resume.html')

def	post_detail(request,	pk):				
	post	=	get_object_or_404(Post,	pk=pk)				
	return	render(request,	'blog/post_detail.html',	{'post':	post})

def	post_new(request):
	if	request.method	==	"POST":								
		form	=	PostForm(request.POST)								
		if	form.is_valid():												
			post	=	form.save(commit=False)												
			post.author	=	request.user												
			post.published_date	=	timezone.now()												
			post.save()												
			return	redirect('post_detail',	pk=post.pk)				
	else:								
		form	=	PostForm()								
	return	render(request,	'blog/post_edit.html',	{'form':	form})

def	post_edit(request,	pk):				
	post	=	get_object_or_404(Post,	pk=pk)				
	if	request.method	==	"POST":								
		form	=	PostForm(request.POST,	instance=post)								
		if	form.is_valid():												
			post	=	form.save(commit=False)												
			post.author	=	request.user												
			post.published_date	=	timezone.now()												
			post.save()												
			return	redirect('post_detail',	pk=post.pk)				
	else:								
		form	=	PostForm(instance=post)				
	return	render(request,	'blog/post_edit.html',	{'form':	form})


def search(request):
	template = 'blog/blogging.html'
	query = request.Get.get('q')
	results= Post.objects.filter(Q(title__icontains= query) | Q(body__icontains = query))
	pages = pagination(request, results, num=1)
	context = {
	'items': pages[0],
	'page_range' : pages[1],
	}
	return render(request, template, context)