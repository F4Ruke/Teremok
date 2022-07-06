from django.urls import path
from apps.core.views.indexview import IndexView
from apps.core.views.aboutview import AboutView
from apps.core.views.contactsview import ContactsView
from apps.core.views.advertsview import AdvertsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('adverts/', AdvertsView.as_view(), name='adverts'),
]
