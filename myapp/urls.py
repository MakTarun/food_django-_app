from django.contrib import admin
from django.urls import path
from .import views
from django.views.decorators.cache import cache_page

app_name='myapp'
urlpatterns = [
    # urls of DRF
    path('api/items',views.item_list_api,name='item_list_api'),
    #url of api-single-item_read
    path("api/items/<int:pk>",views.item_detail_api,name='item_detail_api'),
    # urls for django app
    path('',views.index,name='index'),
    path('<int:id>/',views.detail,name='detail'),
    path('add/',views.create_Item,name='create_item'),
    path('update/<int:pk>/',views.ItemUpdateView.as_view(),name='update_form'),
    path('delete/<int:pk>/',views.ItemDeleteView.as_view(), name='delete_item'),
    
]
