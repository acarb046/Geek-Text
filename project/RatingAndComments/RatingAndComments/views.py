# views.py
#modify this code

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rating, Comment
from .serializers import RatingSerializer, CommentSerializer

class RatingCreateAPIView(APIView):
    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentCreateAPIView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentListAPIView(APIView):
    def get(self, request, book_id):
        comments = Comment.objects.filter(book_id=book_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class AverageRatingAPIView(APIView):
    def get(self, request, book_id):
        ratings = Rating.objects.filter(book_id=book_id)
        if ratings.exists():
            average_rating = ratings.aggregate(models.Avg('rating'))['rating__avg']
            return Response({'average_rating': average_rating})
        return Response({'average_rating': None})
