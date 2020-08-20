from django.urls import path
from .views import *

app_name = 'todoapp'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_view, name='add'),
    path('detail/<pk>', TaskDetailView.as_view(), name='detail'),
    path('update/<pk>', TaskUpdateView.as_view(), name='update'),
    path('delete/<pk>', TaskDeleteView.as_view(), name='delete'),
    
]
