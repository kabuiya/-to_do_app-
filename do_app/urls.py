from . import views
from django.urls import path

urlpatterns = [
    path('my_activity/', views.to_do),
    path('my_activity/<int:pk>', views.to_do_update),
]
