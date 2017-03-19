from django.shortcuts import render
from .models import BlogPost
from django.shortcuts import get_object_or_404, redirect
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
	template_name='index.html'

	blogs = BlogPost.objects.all() #queryset-- which return all objects of BlogPost class

	context={'title':'Home','name':'Ajay','blogs':blogs}
	return render(request,template_name,context)

def contact(request):
	template_name='contact.html'
	context={'title':'contact'}
	return render(request,template_name,context)

def about(request):
	template_name='about.html'
	context={'title':'About'}
	return render(request,template_name,context)
def post(request):
	template_name='post.html'
	context={}
	return render(request,template_name)

@login_required
def createblog(request):
	if request.method=='POST':
		form=BlogPostForm(request.POST, request.FILES)
		if form.is_valid():
			form=form.save(commit=False)
			form.author=request.user
			form.save()
			return redirect('home')
	else:
		form=BlogPostForm()

	context={'form':form}
	template_name='blog_create.html'
	return render(request,template_name,context)
def detail(request,pk):
	template_name='blog_detail.html'
	blog= get_object_or_404(BlogPost,pk=pk)
	context={'blog':blog, 'title':blog.title}
	return render (request,template_name,context)

def signup(request):
	template_name='registration/signup.html'
	if request.method=="POST":
		form= UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form=UserCreationForm()
	context={'form':form}
	return render(request,template_name,context)