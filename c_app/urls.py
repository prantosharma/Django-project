from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path("detail/<int:id>/",views.detail, name="detail"),
    path('search/',views.search,name='search'),
    path('contact/create',views.ContactCreateView.as_view(),name='create'),
    path('contact/update/<int:pk>',views.ContactUpdateView.as_view(),name='update'),
    path('contact/delete/<int:pk>',views.ContactDeleteView.as_view(),name='delete'),
    path('signup/',views.SingUpView.as_view(),name='signup')
]