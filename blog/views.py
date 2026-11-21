from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializers
from .models import Blog 
from django.shortcuts import get_object_or_404, redirect,render


# Create your views here.

# DRP API views

@api_view(['GET'])
def api_blog_list(request):
    blog = Blog.objects.all()
    serializer = BlogSerializers(blog, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def api_blog_create(request):
    serializer = BlogSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Blog create successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['get'])
def api_blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    serializer = BlogSerializers(blog)
    return Response(serializer.data)

@api_view(['PUT'])
def api_blog_change(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    serializer = BlogSerializers(blog, data=request.data, )
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'message': 'Blog  updated successfully', 'data': serializer.data},
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PATCH'])
def api_blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
   
    serializer = BlogSerializers(blog, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'message': 'Blog partially updated successfully', 'data': serializer.data},
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return Response(
        {'message': 'Blog deleted successfully'}, 
        status=status.HTTP_204_NO_CONTENT
    )


# HTML Template views

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, "index.html", {"blogs":blogs})

def blog_create(request):
    if request.method == "POST":
        Blog.objects.create(
            title=request.POST.get("title", "").strip(),
            description=request.POST.get("description", "").strip(),
            content=request.POST.get("content", "").strip(),

        )
        return redirect("blog_list")
    return render(request, "create_blog.html")

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    return render(request, "blog_detail.html", {"blog": blog})


def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == "POST":
        method = request.POST.get("_method")
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        content = request.POST.get("content", "").strip()

        if method == "PUT":
            if title and description and content:
                blog.title = title
                blog.description = description
                blog.content = content
                blog.save()
                return redirect("blog_detail", pk=blog.pk)

        elif method == "PATCH":
            if title:
                blog.title = title
            if description:
                blog.description = description
            if content:
                blog.content = content
            blog.save()
            return redirect("blog_detail", pk=blog.pk)

    return render(request, "update_blog.html", {"blog": blog})




def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        blog.delete()
        return redirect("blog_list")
    return redirect("blog_detail", pk=blog.pk)