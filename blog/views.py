from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializers
from .models import Blog 
from django.shortcuts import get_object_or_404


# Create your views here.


@api_view(['GET'])
def blog_list(request):
    blog = Blog.objects.all()
    serializer = BlogSerializers(blog, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def blog_create(request):
    serializer = BlogSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Blog create successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['get'])
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    serializer = BlogSerializers(blog)
    return Response(serializer.data)

@api_view(['PATCH'])
def blog_update(request, pk):
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
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return Response(
        {'message': 'Blog deleted successfully'}, 
        status=status.HTTP_204_NO_CONTENT
    )