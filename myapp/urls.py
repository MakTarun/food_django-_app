from django.contrib import admin
from django.urls import path
from .import views
from django.views.decorators.cache import cache_page

app_name='myapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/',views.detail,name='detail'),
    path('add/',views.create_Item,name='create_item'),
    path('update/<int:pk>/',views.ItemUpdateView.as_view(),name='update_form'),
    path('delete/<int:pk>/',views.ItemDeleteView.as_view(), name='delete_item'),
    
]
