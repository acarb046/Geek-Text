"""
URL configuration for RatingAndComments project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#modify this code

from django.urls import path
from .views import RatingCreateAPIView, CommentCreateAPIView, CommentListAPIView, AverageRatingAPIView

urlpatterns = [
    path('ratings/', RatingCreateAPIView.as_view(), name='rating-create'),
    path('comments/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('comments/<int:book_id>/', CommentListAPIView.as_view(), name='comment-list'),
    path('average-rating/<int:book_id>/', AverageRatingAPIView.as_view(), name='average-rating'),
]
