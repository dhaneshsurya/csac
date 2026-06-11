from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('committees/', views.committees, name='committees'),
    path('committees/<slug:slug>/', views.committee_detail, name='committee_detail'),
    path('policies/', views.policies, name='policies'),
    path('recognition/', views.recognition, name='recognition'),
    path('staff/teaching/', views.staff_teaching, name='staff_teaching'),
    path('staff/non-teaching/', views.staff_nonteaching, name='staff_nonteaching'),
    path('notices/', views.notices, name='notices'),
    path('contact/', views.contact, name='contact'),
    path('nss/', views.nss, name='nss'),
    path('iic/', views.iic, name='iic'),
    path('ugc/', views.ugc, name='ugc'),
    path('nep/', views.nep, name='nep'),
    path('sports/', views.sports, name='sports'),
    path('co-po/', views.co_po, name='co_po'),
    path('happenings/', views.happenings, name='happenings'),
    path('happenings/<int:pk>/', views.happening_detail, name='happening_detail'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('infrastructure/', views.infrastructure, name='infrastructure'),
    path('products/', views.products, name='products'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('students/library/', views.library, name='library'),
    path('sitemap/', views.sitemap, name='sitemap'),
    # Navbar management URLs
    path('manage-navbar/', views.manage_navbar, name='manage_navbar'),
    path('manage-navbar/add/', views.add_menu_item, name='add_menu_item'),
    path('manage-navbar/edit/<int:pk>/', views.edit_menu_item, name='edit_menu_item'),
    path('manage-navbar/delete/<int:pk>/', views.delete_menu_item, name='delete_menu_item'),
    path('manage-navbar/move/<int:pk>/<str:direction>/', views.move_menu_item, name='move_menu_item'),
]
