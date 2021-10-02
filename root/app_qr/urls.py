from django.urls import path
from app_qr import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('pmps/', views.PmpModel.as_view()),

    path('site-info/', views.SiteInfo.as_view()), 
    path('site-info/<str:id>/', views.SiteInfo.as_view()),

    path('site-info/<str:id>/pmps/', views.SitePmp.as_view()),
    path('site-info/<str:id>/pmps/<str:pmp_id>/', views.SitePmp.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
