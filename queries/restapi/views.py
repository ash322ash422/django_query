from django.shortcuts import render
from  webapp.models import Query
from rest_framework.decorators import api_view
from  rest_framework.response import Response
from  rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from .serializer import QuerySerializer

# Create your views here.
class QueryListAPIView(ListAPIView):
    #permission_classes = (IsAuthenticated,)
    serializer_class = QuerySerializer
    
    def get_queryset(self):
        #title = self.request.query_params.get('title', None)
        
        queryset = Query.objects.all()
        return queryset

class QueryCreateAPIView(CreateAPIView):
    #queryset = Query.objects.all()
    serializer_class = QuerySerializer
    

class QueryUpdateAPIView(UpdateAPIView):
    #queryset = Query.objects.all()
    serializer_class = QuerySerializer
    
    def get_queryset(self):
        queryset = Query.objects.all()
        return queryset
    
    def update(self, request, *args, **kwargs):
        data_to_change = {'qry_name': request.data.get("qry_name")}
        # Partial update of the data
        serializer = self.serializer_class(request.user, data=data_to_change, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)

        return Response(serializer.data)
    