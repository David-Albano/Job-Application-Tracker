from django.urls import path
from .views import index, show_applications, add_application, show_job_info, show_comment, edit_application, delete_application, confirm_delete

urlpatterns = [
    path('', index, name='index'),
    path('applications', show_applications, name='show_applications'),
    path('add_application', add_application, name='add_application'),
    path('show_job_info/<str:id_application>', show_job_info, name='show_job_info'),
    path('show_comment/<str:id_application>', show_comment, name='show_comment'),
    path('edit_application/<str:id_application>', edit_application, name='edit_application'),
    path('delete_application/<str:id_application>', delete_application, name='delete_application'),
    path('confirm_delete/<str:id_application>', confirm_delete, name='confirm_delete')
]