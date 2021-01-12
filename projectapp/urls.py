from django.urls import path

from projectapp.views import ProjectCreateView, ProjectListView, ProjectDetailView, ProjectDeleteView

app_name = 'projectapp'

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('list/', ProjectListView.as_view(), name='list'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', ProjectDeleteView.as_view(), name='delete'),

]