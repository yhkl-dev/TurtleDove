from rest_framework.routers import DefaultRouter
from .views import TasksViewset, AdHocTasksViewset

tasks_router = DefaultRouter()
tasks_router.register(r'task', TasksViewset, base_name="task")
tasks_router.register(r'adhoc_task', AdHocTasksViewset, base_name="adhoc_task")

