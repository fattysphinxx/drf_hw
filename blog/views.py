from ast import IsNot
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from .models import Article,Category
from homework.permissions import IsAdminOrIsAuthenticatedReadOnly
from django.utils import timezone

class ArticleView(APIView):
    # 로그인 한 사용자의 게시글 목록 return
    permission_classes = [IsAdminOrIsAuthenticatedReadOnly]

    def get(self, request):
        time = timezone.now()
        articles = Article.objects.filter(user=request.user, start_date__lt=time, end_date__gt=time).order_by('-create_date')
        titles = [ article.title for article in articles ]
        return Response({'titles': titles})
    
    def post(self, request):
        user = request.user
        title = request.data.get('title', '')
        category_name = request.data.get('category', '')
        content = request.data.get('content', '')

        if len(title) <= 5:
            return Response({'message': '제목은 5글자를 넘아야 합니다.'})
        
        if len(content) <= 20:
            return Response({'message': '내용은 20글자를 넘어야 합니다.'})
        
        if category_name:
            category = [ Category.objects.get(name=name) for name in category_name.split(',') ]
        else:
            return Response({'message': '카테고리를 지정해야 합니다.'})

        new_article = Article.objects.create(user=user, title=title, content=content)
        new_article.category.set(category)

        return Response({'message': '업로드 성공!'})