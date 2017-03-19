from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
	class Meta:# meta --- parent 
		model=BlogPost
		fields=('title','category','content','file','image','publish_date')
