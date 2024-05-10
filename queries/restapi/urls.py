from django.urls import path
from . import views

app_name = 'restapi'
urlpatterns = [
    
    # invoked on GET http://127.0.0.1:8000/restapi/query/list/
    path('query/list/', views.QueryListAPIView.as_view(), name='api_query_list'), #invoked on GET
    
    # invoked on POST http://127.0.0.1:8000/restapi/query/create/
    path('query/create/', views.QueryCreateAPIView.as_view(), name='api_query_create'), 
    
    # invoked on PUT http://127.0.0.1:8000/restapi/query/update/
    path('query/update/<int:pk>', views.QueryUpdateAPIView.as_view(), name='api_query_update'), 
    
]