from django.urls import path

from accounts.views import register_view
from contacts.views import ContactAPIView, SearchView, home

urlpatterns = [
    path('newContact', ContactAPIView.as_view(), name='contact'),
    path('search/', SearchView.as_view(), name='search'),
    path('home/', home, name='home'),
]