from django.contrib import admin

from .models import admin_table, department, employee, leave_type, leave

# Register your models here.

class admin_tableAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'uname', 'passwd', 'creation_date')
    
class departmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'shortform')
    
class employeeAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'phone', 'department', 'gender', 'country', 'city', 'address', 'password','status', 'regdate')

class leave_typeAdmin(admin.ModelAdmin):
    list_display = ('leavetype', 'description', 'createdAt')
    
class leaveAdmin(admin.ModelAdmin):
    list_display = ('leavetype', 'toDate', 'fromDate', 'description', 'request_date', 'adminRemark', 'adminRemarkDate', 'status', 'isRead', 'emp_id')

admin.site.register(admin_table)
admin.site.register(department)
admin.site.register(employee)
admin.site.register(leave_type)
admin.site.register(leave)