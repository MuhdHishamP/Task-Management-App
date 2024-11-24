from django.urls import path
from .views import *

urlpatterns = [
    path("login", home, name="login"),
    path("logout", logout_view, name="logout"),
    path("task", TaskList.as_view(), name="tasks"),
    path("task-create/", TaskCreate.as_view(), name="task-create"),
    path("task-update/<int:pk>/", TaskUpdate.as_view(), name="task-update"),
    path("task-delete/<int:pk>/", DeleteView.as_view(), name="task-delete"),
]
