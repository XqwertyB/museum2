from django.urls import path
from organization import views

urlpatterns = [
    path('organization/', views.OrganizationView.as_view(),),
    path('faq/', views.FaqView.as_view(),),
    path('picture_type/', views.Picture_typeView.as_view(),),
    path('picture/', views.PictureView.as_view(),),
    path('reivew/', views.ContactsView.as_view(),),
    path('contact/',views.Contact.as_view(),),
    path('comtyp/', views.CommodityTypeView.as_view(),),
    path('com/', views.CommodityView.as_view(),)
]