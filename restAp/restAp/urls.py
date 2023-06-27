
from django.contrib import admin
from django.urls import path
from API import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Student/<int:pk>', views.student_detail),
    path('student_list/', views.student_list),
]
