from django.urls import path
from links.api import views as api_views

urlpatterns = [
    path('links/', api_views.link_list_create_api_view, name='link-list'),
    path('links/<int:pk>', api_views.link_detail_api_view, name='link-detail')
]
