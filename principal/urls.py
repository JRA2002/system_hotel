from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('results/',views.search_results, name='results'),
    path('reservation/',views.CustomerView.as_view(), name='detail_customer'),
]