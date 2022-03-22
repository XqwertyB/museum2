from django.urls import path
from organization import views

urlpatterns = [
    path('organization/', views.OrganizationView.as_view(),),
    path('faq/', views.FaqView.as_view(),)
]