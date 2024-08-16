from . import views
from django.urls import path


urlpatterns = [
   # path('admin/', admin.site.urls),
   path('', views.index, name='index'),
   
   #admin urls
   path('admin_login', views.admin_login, name='admin_login'),
   path('dashboard', views.dashboard_view, name='dashboard'),
   path('admin_manage', views.admin_list, name='admin_manage'),
   path('sidebar', views.sidebar, name='sidebar'),
   path('emp_section', views.employee_view, name='emp_section'),
   path('create_admin', views.create_admin, name='create_admin'),
   path('department_section', views.department_section, name='department_section'),
   path('leave-manage', views.leave_manage, name='leave-manage'),
   path('add_emp', views.add_emp, name='add_emp'),
   path('pending', views.pendig_view, name='pending'),
   path('approved', views.approved_view, name='approved'),
   path('leave_history', views.leave_history, name='leave_history'),
   path('declined', views.declined_view, name='declined'),
   path('add_department', views.add_dept, name='add_department'),
   path('add_leave', views.add_leave, name='add_leave'),
   path('leave_types', views.leave_types, name='leave_types'),
   path('admin_logout', views.admin_logout, name='admin_logout'),
   
   path('admin_forget_pass', views.admin_forget_pass, name='admin_forget_pass'),
   path('admin_recovery_pass', views.admin_recovery_pass, name='admin_recovery_pass'),
   
   
   
   
   
   #update
   path('emp_update/<int:id>/', views.emp_update, name='emp_update'),
   path('doupdate_emp/<int:id>/', views.doupdate_emp, name= 'doupdate_emp'),
   
   
   path('emp_delete/<int:id>/', views.emp_delete, name='emp_delete'),
   
   #status
   path('emp_status/<int:id>', views.emp_status, name='emp_status'),
   
   path('emp_leave_details/<int:id>/', views.emp_leave_details, name = 'emp_leave_details'),
   path('admin_remark/<int:id>/', views.admin_remark, name = 'admin_remark'),
   
   path('admin/nav.html', views.nav, name = 'nav'),
   
   
   #employee urls
   path('emp_login', views.emp_login, name='emp_login'),
   path('leave_request', views.leave_request, name='leave_request'),
   path('password', views.password, name='password'),
   path('profile', views.profile, name='profile'),
   path('view_history', views.view_history, name='view_history'),
   path('emp_sidebar', views.emp_sidebar, name= 'emp_sidebar'),
   path('change_password', views.change_password, name= 'change_password'),
   path('emp_logout', views.emp_logout, name='emp_logout'),
   path('forget_pass', views.forget_pass, name='forget_pass'),
   path('recovery_pass', views.recovery_pass, name='recovery_pass'),
   
   
]