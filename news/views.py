
from rest_framework import viewsets, response, status
from . import serializers, models as AllNews

from rest_framework.generics import get_object_or_404
from helpers.pagination import CustomPagination
from rest_framework import filters


# CRUD operation in REST API 
class NewsViewSets(viewsets.ViewSet):

    serializer_class = serializers.NewsSerializer
    # topshiriq 5 - teskari filterlash by date
    queryset = AllNews.News.objects.order_by('-date_published')
    # topshiriq 6 - pagination qilish, 10 tadan, from helpers.pagination import CustomPagination, pagination.py ga qaralsin  
    pagination_class = CustomPagination 
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
   

    

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        
        return response.Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None):
        latestNews = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(latestNews)
        return response.Response(serializer.data)

    def update(self, request, pk=None):
        latestNews = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(latestNews, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)


    def destroy(self, request, pk=None):
        latestNews = get_object_or_404(self.queryset, pk=pk)
        latestNews.delete()
        return response.Response(status=status.HTTP_200_OK)



