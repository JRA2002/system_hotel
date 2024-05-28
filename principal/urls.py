from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    #3path('date_range/',views.date_range_view,name='date_range')
    path('rooms/',views.RoomListView.as_view(),name='rooms'),
    path('rooms/detail/<int:pk>/', views.RoomDetailView.as_view(), name='detail_room')
]