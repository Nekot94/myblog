from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post

def post_list(request):
	queryset = Post.objects.all()
	# return HttpResponse("<h1>Вы такие молодцы!!!</h1>")
	content = {
		"title": "задохнись",
		"object_list": queryset
	}
	return render(request, "post_list.html",content)

def post_detail(request, id=None):
	queryset = get_object_or_404(Post, id=id)
	# return HttpResponse("<h1>Вы такие молодцы!!!</h1>")
	content = {
		"title": "статья",
		"object": queryset
	}
	return render(request, "post_detail.html",content)

