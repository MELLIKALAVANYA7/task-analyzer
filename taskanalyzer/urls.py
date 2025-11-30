from tasks.views import task_list, task_edit, task_delete, task_toggle_complete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_list),
    path('edit/<int:pk>/', task_edit, name='task_edit'),
    path('delete/<int:pk>/', task_delete, name='task_delete'),
    path('toggle/<int:pk>/', task_toggle_complete, name='task_toggle_complete'),
]

