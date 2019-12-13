from django.shortcuts import render

# Create your views here.

def post_list(requset):
    return render(requset, 'blog/post_list.html', {})