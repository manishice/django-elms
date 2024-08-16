from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from  .models import *
from django.contrib.auth import authenticate, login, logout
from leave.validation import *
from leave.country import *
from django.utils import timezone
import bcrypt

from django.contrib.auth.decorators import login_required

from django.db.models import Max
from django.contrib import messages, sessions

# Create your views here.

def index(request):
    
    return redirect("emp_login")

def admin_logout(request):
    del request.session['admin_email']
    return redirect("admin_login")

def employee_view(request):
    emp_data = employee.objects.all()
    notification = leave.objects.filter(isRead = 0).count
    notification_data = reversed(leave.objects.filter(isRead = 0))
    admin_email=request.session.get('admin_email')
    admin_details = admin_table.objects.get(email=admin_email)
    context = {
        'employees': emp_data,
        'notification': notification,
        'notification_data': notification_data,
        'admin_details': admin_details
    }
    return render(request, 'admin/emp_section.html', context)

def admin_list(request):
    admins = admin_table.objects.all()
    admin_email=request.session.get('admin_email')
    admin_details = admin_table.objects.get(email=admin_email)
    notification = leave.objects.filter(isRead = 0).count
    notification_data = reversed(leave.objects.filter(isRead = 0))
    context = {
        'admins': admins,
        'notification':notification,
        'notification_data':notification_data,
        'admin_details': admin_details,
    }
    return render(request, 'admin/admin_manage.html', context)


def admin_login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('pass')
        
        if "@" in username:
            try:
                admin_details = admin_table.objects.get(email=username)
                hashed_password = admin_details.passwd
                result = check_password(password, hashed_password)
                if(result):
                    request.session['admin_email']=admin_details.email
                    return redirect("dashboard")
                else:
                    messages.error(request, "username or password is incorrect")
            except:
                messages.error(request, "admin does not exists")
        else:
            try:
                admin_details = admin_table.objects.get(uname=username)
                hashed_password = admin_details.passwd
                result = check_password(password, hashed_password)
                if(result):
                    request.session['admin_email']=admin_details.email
                    return redirect("dashboard")
                else:
                    messages.error(request, "username or password is incorrect")
            except:
                messages.error(request, "admin does not exists")

        
    return render(request, 'admin/admin_login.html')

def pendig_view(request):
    admin_email=request.session.get('admin_email')
    admin_details = admin_table.objects.get(email=admin_email)
    leave_details = reversed(leave.objects.all())
    emp_details = employee.objects.all()
    dept_details = department.objects.all()
    notification = leave.objects.filter(isRead = 0).count
    notification_data = reversed(leave.objects.filter(isRead = 0))
    
    active_emp = employee.objects.filter(status=1)
    inactive_emp = employee.objects.filter(status=0)
    
    pending = reversed(leave.objects.filter(status = 0))
    declined = leave.objects.filter(status = 1)
    approved = leave.objects.filter(status = 2)
    
    context = {
        'leave_details': leave_details,
        'emp_details': emp_details,
        'dept_details': dept_details,
        'active_emp': active_emp,
        'inactive_emp': inactive_emp,
        'pending': pending,
        'declined': declined,
        'approved': approved,
        'admin_details': admin_details,
        'notification': notification,
        'notification_data': notification_data,
        
    }
    return render(request, 'admin/pending.html', context)

def approved_view(request):
    admin_email=request.session.get('admin_email')
    admin_details = admin_table.objects.get(email=admin_email)
    leave_details = reversed(leave.objects.all())
    emp_details = employee.objects.all()
    dept_details = department.objects.all()
    notification = leave.objects.filter(isRead = 0).count
    notification_data = reversed(leave.objects.filter(isRead = 0))
    
    active_emp = employee.objects.filter(status=1)
    inactive_emp = employee.objects.filter(status=0)
    
    pending = leave.objects.filter(status = 0)
    declined = leave.objects.filter(status = 1)
    approved = reversed(leave.objects.filter(status = 2))
    
    context = {
        'leave_details': leave_details,
        'emp_details': emp_details,
        'dept_details': dept_details,
        'active_emp': active_emp,
        'inactive_emp': inactive_emp,
        'pending': pending,
        'declined': declined,
        'approved': approved,
        'admin_details': admin_details,
        'notification': notification,
        'notification_data': notification_data,
        
    }
    return render(request, 'admin/approved.html', context)

def declined_view(request):
    admin_email=request.session.get('admin_email')
    admin_details = admin_table.objects.get(email=admin_email)
    leave_details = reversed(leave.objects.all())
    emp_details = employee.objects.all()
    dept_details = department.objects.all()
    notification = leave.objects.filter(isRead = 0).count
    notification_data = reversed(leave.objects.filter(isRead = 0))
    
    active_emp = employee.objects.filter(status=1)
    inactive_emp = employee.objects.filter(status=0)
    
    pending = leave.objects.filter(status = 0)
    declined = reversed(leave.objects.filter(status = 1))
    approved = leave.objects.filter(status = 2)
    
    context = {
        'leave_details': leave_details,
        'emp_details': emp_details,
        'dept_details': dept_details,
        'active_emp': active_emp,
        'inactive_emp': inactive_emp,
        'pending': pending,
        'declined': declined,
        'approved': approved,
        'admin_details': admin_details,
        'notification':notification,
        'notification_data': notification_data,
        
    }
    return render(request, 'admin/declined.html', context)

def department_section(request):
    admin_email=request.session.get('admin_email')
    admin_details = admin_table.objects.get(email=admin_email)
    
    notification = leave.objects.filter(isRead = 0).count
    notification_data = reversed(leave.objects.filter(isRead = 0))
    dept_data = department.objects.all()
    context = {
        'departments': dept_data,
        'admin_details':admin_details,
        'notification':notification,
        'notification_data':notification_data,
    }
    return render(request, 'admin/department.html', context)


def dashboard_view(request):
    admin_email=request.session.get('admin_email')
    admin_details = admin_table.objects.get(email=admin_email)
    leave_details = reversed(leave.objects.all())
    emp_details = employee.objects.all()
    dept_details = department.objects.all()
    leave_count = leave_type.objects.all()
    
    active_emp = employee.objects.filter(status=1)
    inactive_emp = employee.objects.filter(status=0)
    
    pending = leave.objects.filter(status = 0)
    declined = leave.objects.filter(status = 1)
    approved = leave.objects.filter(status = 2)
    notification = leave.objects.filter(isRead = 0).count
    notification_data = reversed(leave.objects.filter(isRead = 0))
    
    context = {
        'leave_details': leave_details,
        'emp_details': emp_details,
        'dept_details': dept_details,
        'active_emp': active_emp,
        'inactive_emp': inactive_emp,
        'pending': pending,
        'declined': declined,
        'approved': approved,
        'leave_count': leave_count,
        'notification': notification,
        'notification_data': notification_data,
        'admin_details': admin_details
        
    }
    return render(request, 'admin/dashboard.html', context)

def sidebar(request):
    return render(request, 'sidebar.html')

def emp_sidebar(request):
    return render(request, 'emp_sidebar.html')

def add_emp(request):
    
    admin_email=request.session.get('admin_email')
    admin_details = admin_table.objects.get(email=admin_email)
    notification = leave.objects.filter(isRead = 0).count
    notification_data = reversed(leave.objects.filter(isRead = 0))
    
    values = {}
    
    if employee.objects.count() == 0:
        eid = "EMP1"
        
    else:
        eid = "EMP"+str(employee.objects.aggregate(max=Max('id'))["max"]+1)
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dept = request.POST.get('department')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        city = request.POST.get('city')
        address = request.POST.get('address')
        password = request.POST.get('passwd')
        password2 = request.POST.get('passwd2')
        
        values ={
            'fname': fname,
            'lname': lname,
            'email': email,
            'phone': phone,
            'dept': dept,
            'gender': gender,
            'country': country,
            'city': city,
            'address': address,
        }
        
        
        
        
        if not fname:
            messages.error(request, 'first name is required')
        elif str(fname).isdigit():
            messages.error(request, 'invalid first name')
        elif not lname:
            messages.error(request, 'last name is required')
        elif str(lname).isdigit():
            messages.error(request, 'invalid last name')
        
        elif employee.objects.filter(email = email).exists():
            messages.error(request, "email already exits")
        
        elif validate_phone(phone) == False:
            messages.error(request, "invalid phone number")
            
        elif employee.objects.filter(phone = phone).exists():
            messages.error(request, "email already exits!")
        
        elif validate_password(password) != True:
            messages.error(request, "password must be 8 characters, 1 Uppercase, 1 Lowercase, 1 special character")
        
        elif password != password2:
            messages.error(request, "password does not match")
            
        
        else:
            user_password = password
            hashed_password=hash_password(user_password)
            
            
              
            emp_data = employee(eid=eid, fname=fname, lname=lname, email=email, phone=phone, department=dept, gender=gender, country=country, city=city, address=address, password=hashed_password)
            emp_data.save()
            messages.success(request, "employee added successfully")
    
    country_list = country_names
    india_list = india
        
    dept_data = department.objects.all()
    context = locals()
    context.update({
            'departments': dept_data,
            'country_list': country_list,
            'india_list': india_list,
            'notification': notification,
            'notification_data': notification_data,
            'admin_details': admin_details,
            'values': values,
        })

        
    return render(request, 'admin/add_emp.html', context)

def leave_history(request):
    request.session.get('admin_email')
    leave_details = reversed(leave.objects.all())
    emp_details = employee.objects.all()
    dept_details = department.objects.all()
    
    admin_email=request.session.get('admin_email')
    admin_details = admin_table.objects.get(email=admin_email)
    
    notification = leave.objects.filter(isRead = 0).count
    notification_data = reversed(leave.objects.filter(isRead = 0))
    
    active_emp = employee.objects.filter(status=1)
    inactive_emp = employee.objects.filter(status=0)
    
    pending = leave.objects.filter(status = 0)
    declined = leave.objects.filter(status = 1)
    approved = leave.objects.filter(status = 2)
    
    context = {
        'leave_details': leave_details,
        'emp_details': emp_details,
        'dept_details': dept_details,
        'active_emp': active_emp,
        'inactive_emp': inactive_emp,
        'pending': pending,
        'declined': declined,
        'approved': approved,
        'notification': notification,
        'notification_data': notification_data,
        'admin_details': admin_details,
        
    }
    return render(request, 'admin/leave_history.html', context)

def department_view(request):
    dept_data = department.objects.all()
    notification = leave.objects.filter(isRead = 0).count
    notification_data = reversed(leave.objects.filter(isRead = 0))
    context = {
        'departments': dept_data,
        'notification': notification,
        'notification_data': notification_data,
    }
    return render(request, 'admin/department.html', context)

def leave_types(request):
    leave_data = leave_type.objects.all()
    notification = leave.objects.filter(isRead = 0).count
    notification_data = reversed(leave.objects.filter(isRead = 0))
    admin_email=request.session.get('admin_email')
    admin_details = admin_table.objects.get(email=admin_email)
    context = {
        'leave_types': leave_data,
        'notification': notification,
        'notification_data': notification_data,
        'admin_details': admin_details,
    }
    return render(request, 'admin/leave_types.html', context)

def add_leave(request):
    admin_email=request.session.get('admin_email')
    admin_details = admin_table.objects.get(email=admin_email)
    notification = leave.objects.filter(isRead = 0).count
    notification_data = reversed(leave.objects.filter(isRead = 0))
    if request.method == 'POST':
        leavetype = request.POST.get('leavetype')
        description = request.POST.get('description')
        
        
        if str(leavetype).isdigit():
            messages.error(request, 'invalid leave type')
        elif str(description).isdigit():
            messages.error(request, "invalid description")
        elif leave_type.objects.filter(leavetype = leavetype).exists():
            messages.error(request, "leave already exits")
        
        else:
            leave_data = leave_type(leavetype = leavetype, description = description)
            leave_data.save()
            messages.success(request, "data created successfully")
    context ={
            'notification': notification,
            'notification_data': notification_data,
            'admin_details': admin_details,
            }
    return render(request, 'admin/add_leave.html', context)

def add_dept(request):
    notification = leave.objects.filter(isRead = 0).count
    notification_data = reversed(leave.objects.filter(isRead = 0))
    admin_email=request.session.get('admin_email')
    admin_details = admin_table.objects.get(email=admin_email)
    if request.method == 'POST':
        title = request.POST.get('title')
        shortform = request.POST.get('sf')
        
        
        
        if str(title).isdigit() or str(shortform).isdigit():
            messages.error(request, 'invalid input')
        elif department.objects.filter(title= title).exists():
            messages.error(request, "department already exits")
            
        else:
            dept_data= department(title=title, shortform = shortform)
            dept_data.save()
            messages.success(request, "department added successfully")
    context = {
        'notification': notification,
        'notification_data': notification_data,
        'admin_details': admin_details,
        }
    return render(request, 'admin/add_dept.html', context)

def leave_manage(request):
    return render(request, 'admin/leave_manage.html')

def create_admin(request):
    admin_email=request.session.get('admin_email')
    admin_details = admin_table.objects.get(email=admin_email)
        
    notification = leave.objects.filter(isRead = 0).count
    notification_data = reversed(leave.objects.filter(isRead = 0))
    
    values = {}
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('passwd')
        password2 = request.POST.get('passwd2')
        
        values= {
            'fullname': fullname,
            'uname': uname,
            'email': email,
        }
        


        #for validation
        if not fullname:
            messages.error(request, "fullname is required")
        
        elif len(fullname)< 4:
            messages.error(request, "invalid name")
        elif str(fullname).isdigit(): 
            messages.error(request, "invalid name")

            
        elif not uname:
            messages.error(request, "username is required")
        elif len(uname)< 4:
            messages.error(request, "username must be at least 4 characters")
        elif str(uname).isdigit() or str(fullname).isspace():
            messages.error(request, "invalid username")
        elif admin_table.objects.filter(uname = uname).exists():
            messages.error(request, "username already exits")
            
        elif not email:
            messages.error(request, "email is required")
            
        elif admin_table.objects.filter(email = email).exists():
            messages.error(request, "email already exits")
            
        elif not password:
            messages.error(request, "password is required")

        # elif validate_password(password) != True:
        #     messages.error(request, "password must be 8 characters, 1 Uppercase, 1 Lowercase, 1 special character")
        
        elif password != password2:
            messages.error(request, "password does not match")
        
        else:
            admin_password = password
            hashed_password = hash_password(admin_password)
            admin_data = admin_table(fullname=fullname, uname=uname, email=email, passwd = hashed_password, user_id=1)   
            admin_data.save()
            messages.success(request, "successfully")
        
    context ={
        'notification': notification,
        'notification_data': notification_data,
        'admin_details': admin_details,
        'values': values,
        }
    return render(request, 'admin/create_admin.html', context)


#employee

def emp_login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        
        if not email or not password:
            messages.error(request, "Please enter all fields")
        else:
            try:
                # Fetch the employee by email
                emp_details = employee.objects.get(email=email)
                hashed_password = emp_details.password
                result = check_password(password, hashed_password)
                if (result):
                    if(emp_details.status == 0):
                        messages.error(request, "your account is inacive! please contact your manager")
                    else:
                        request.session['employee_email']= emp_details.email
                        return redirect("leave_request")
                else:
                    messages.error(request, "email or password is incorrect")
                
            except:
                messages.error(request, "employee does not exists")
        
    return render(request, 'employee/emp_login.html')

def leave_request(request):
    email = request.session.get('employee_email')
    emp_details = employee.objects.get(email=email)
    leave_data = leave_type.objects.all()
    
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        leave_types = request.POST.get('leave_type')
        condition = request.POST.get('condition')
        
        if str(condition).isdigit():
            messages.error(request, "invalid condition")
        else:
            apply_leave = leave(leavetype=leave_types, fromDate=start_date, toDate=end_date, description=condition, status=0, isRead=0, eid_id = emp_details.id)
            apply_leave.save()
            messages.success(request, "leave applied successfully")
    
    context = {
        'emp_details' : emp_details,
        'leave_types': leave_data
    }
    
    return render(request, 'employee/leave_request.html', context)

def password(request):
    email = request.session.get('employee_email')
    emp_details = employee.objects.get(email=email)
    print(email)
    context = {
        'emp_details' : emp_details
    }
    
    return render(request, 'employee/password.html', context)

def profile(request):
   
    email = request.session.get('employee_email')
    emp_details = employee.objects.get(email=email)
    country_list = country_names
    india_list = india
    
    context = {
        'emp_details' : emp_details,
        'country_list': country_list,
        'india_list': india_list
    }
    
    return render(request, 'employee/profile.html', context)

def view_history(request):
    email = request.session.get('employee_email')
    emp_details = employee.objects.get(email=email)
    
    leave_request = reversed(leave.objects.filter(eid_id=emp_details.id))
    context = {
        'leave_details' : leave_request,
        'emp_details' : emp_details
    }
    
    return render(request, 'employee/view_history.html', context)

#update views

def emp_update(request, id):
    empid = employee.objects.get(id=id)
    dept_data = department.objects.all()
    country_list = country_names
    india_list = india
    
    admin_email=request.session.get('admin_email')
    admin_details = admin_table.objects.get(email=admin_email)
        
    notification = leave.objects.filter(isRead = 0).count
    notification_data = reversed(leave.objects.filter(isRead = 0))
    context= {
        'emp_update': empid,
        'departments': dept_data,
        'country_list': country_list,
        'india_list': india_list,
        'notification': notification,
        'notification_data': notification_data,
        'admin_details': admin_details,
    }
    return render(request, 'admin/emp_update.html', context)


def doupdate_emp(request, id):
    
    updated_fname = request.POST.get('fname')
    updated_lname = request.POST.get('lname')
    updated_email = request.POST.get('email')
    updated_phone = request.POST.get('phone')
    updated_dept = request.POST.get('department')
    updated_country = request.POST.get('country')
    updated_city = request.POST.get('city')
    updated_address = request.POST.get('address')
    
    emp_data = employee.objects.get(id=id)
    #saving updated data
    emp_data.fname = updated_fname
    emp_data.lname = updated_lname
    emp_data.email = updated_email
    emp_data.phone = updated_phone
    emp_data.department = updated_dept
    emp_data.country = updated_country
    emp_data.city = updated_city
    emp_data.address = updated_address
    
    
    emp_data.save()
    
    return redirect("emp_section")


def emp_delete(request, id):
    emp = employee.objects.get(id=id)
    emp.delete()
    return redirect("emp_section")

#status update
def emp_status(request, id):
    updated_status = request.POST.get('status')
    emp = employee.objects.get(id=id)
    
    emp.status = updated_status
    emp.save()
    return redirect("emp_section")
    
def emp_leave_details(request, id):
    request.session.get('admin_email')
    leave_details = leave.objects.get(id=id)
    emp_details = employee.objects.all()
    dept_details = department.objects.all()
    leave_details.isRead = 1
    leave_details.save()
    
    admin_email=request.session.get('admin_email')
    admin_details = admin_table.objects.get(email=admin_email)
    notification = leave.objects.filter(isRead = 0).count
    notification_data = reversed(leave.objects.filter(isRead = 0))
    
    active_emp = employee.objects.filter(status=1)
    inactive_emp = employee.objects.filter(status=0)
    
    pending = leave.objects.filter(status = 0)
    declined = leave.objects.filter(status = 1)
    approved = leave.objects.filter(status = 2)

    
    context = {
        'leave_details': leave_details,
        'emp_details': emp_details,
        'dept_details': dept_details,
        'active_emp': active_emp,
        'inactive_emp': inactive_emp,
        'pending': pending,
        'declined': declined,
        'approved': approved,
        'notification': notification,
        'notification_data': notification_data,
        'admin_details': admin_details,
    }
    
    return render(request, 'admin/emp_leave_details.html', context)

def change_password(request):
    email = request.session.get('employee_email')
    emp_details = employee.objects.get(email=email)
    leave_data = leave_type.objects.all()
    
    if request.method == 'POST':
        current_pass = request.POST.get('current_pass')
        new_pass = request.POST.get('new_pass')
        confirm_new_pass = request.POST.get('confirm_new_pass')
        
        hashed_password = emp_details.password
        result = check_password(current_pass, hashed_password)
    
        if (result):

            if validate_password(new_pass) != True:
                messages.error(request, "password must be 8 characters, 1 Uppercase, 1 Lowercase, 1 special character")
        
            elif new_pass != confirm_new_pass and new_pass:
                messages.error(request, "password does not match")
            else:
                user_password = new_pass
                hashed_password = hash_password(user_password)
                emp_details.password = hashed_password
                emp_details.save()
                messages.success(request, 'password changed successfully')
        else:
            messages.error(request, "current password is wront")
            
    
    context = {
        'emp_details' : emp_details,
        'leave_types': leave_data
    }
    return render(request, 'employee/password.html', context)



def emp_logout(request):
    del request.session['employee_email']
    return redirect("emp_login")


def admin_remark(request, id):
    if request.method== 'POST':
        action = request.POST.get('action')
        admin_remark = request.POST.get('admin_remark')
        remark_date = timezone.now().strftime('%d-%m-%Y, %H:%M:%S')
        
        admin_remark_data = leave.objects.get(id=id)
        admin_remark_data.status = action
        admin_remark_data.adminRemark = admin_remark
        admin_remark_data.adminRemarkDate = remark_date
        
        admin_remark_data.save()
        messages.success(request, "leave updated successfully")
        
        return redirect("emp_leave_details", id=admin_remark_data.pk)
        

def nav(request):
    request.session.get('admin_email')
    leave_details = reversed(leave.objects.all())
    
    admin_email=request.session.get('admin_email')
    admin_details = admin_table.objects.get(email=admin_email)
    emp_details = employee.objects.all()
    dept_details = department.objects.all()
    leave_count = leave_type.objects.all()
    
    active_emp = employee.objects.filter(status=1)
    inactive_emp = employee.objects.filter(status=0)
    
    pending = leave.objects.filter(status = 0)
    declined = leave.objects.filter(status = 1)
    approved = leave.objects.filter(status = 2)
    notification = leave.objects.filter(isRead = 0).count
    notification_data = reversed(leave.objects.filter(isRead = 0))
    
    context = {
        'leave_details': leave_details,
        'emp_details': emp_details,
        'dept_details': dept_details,
        'active_emp': active_emp,
        'inactive_emp': inactive_emp,
        'pending': pending,
        'declined': declined,
        'approved': approved,
        'leave_count': leave_count,
        'notification': notification,
        'notification_data': notification_data,
        'admin_details': admin_details,
        
    }
    return render(request, 'admin/nav.html', context)


def forget_pass(request):
    
    if request.method == 'POST':
        
        email = request.POST.get('email')
        eid = request.POST.get('eid')
        
        if not email or not eid:
            messages.error(request, 'please enter all fields')
        elif not email:
            messages.error(request, 'please enter your email')
        elif len(email)< 10:
            messages.error(request, "email must be at least 10 characters")
        elif not eid:
            messages.error(request, 'please enter your eid')
        elif "EMP" not in eid:
            messages.error(request, 'please enter valid eid')
        
        else:
            try:
                
                emp_details = employee.objects.get(email=email)
                if emp_details.email != email and emp_details.eid != eid:
                    messages.error(request, 'email and emp id mismatch')
                else:
                    emp_email = request.session['recovery_email'] = emp_details.email
                    return redirect('recovery_pass')
                
            except:
                messages.error(request, 'employee does not exists !!')
                
   
    return render(request, 'employee/forget_pass.html')

def recovery_pass(request):
    email = request.session.get('recovery_email')
    emp_details = employee.objects.get(email=email)
    
    if request.method == 'POST':
        new_pass = request.POST.get('passwd')
        confirm_new_pass = request.POST.get('passwd2')
        
        if validate_password(new_pass) != True:
            messages.error(request, "password must be 8 characters, 1 Uppercase, 1 Lowercase, 1 special character")
        
        elif new_pass != confirm_new_pass and new_pass:
            messages.error(request, "password does not match")
        else:
            user_password = new_pass
            hashed_password= hash_password(user_password)
            emp_details.password = hashed_password
            emp_details.save()
            del request.session['recovery_email']
            return redirect('emp_login')
        
    return render(request, 'employee/recovery_pass.html')

        
def admin_forget_pass(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        uname = request.POST.get('uname')
    
        if not email or not uname:
                messages.error(request, 'please enter all fields')
        elif not email:
                messages.error(request, 'please enter your email')
        elif len(email)< 10:
                messages.error(request, "email must be at least 10 characters")
        elif not uname:
                messages.error(request, 'please enter your eid')
        else:
            try:
                admin_details = admin_table.objects.get(email=email)
                if admin_details.email != email or admin_details.uname != uname:
                    messages.error(request, "email and username do not match")
                else: 
                    request.session['admin_recovery_email']=admin_details.email
                
                    return redirect('admin_recovery_pass')
            except:
                messages.error(request, "admin does not exists")
            
            

    return render(request, 'admin/admin_forget_pass.html')

def admin_recovery_pass(request):
    admin_recovery_email = request.session.get('admin_recovery_email')
    
    admin_details = admin_table.objects.get(email=admin_recovery_email)
    
    if request.method == 'POST':
        new_pass = request.POST.get('passwd')
        confirm_new_pass = request.POST.get('passwd2')
        
        if not new_pass or not confirm_new_pass:
            messages.error(request, 'please fill up the password fields')
        else:
            if validate_password(new_pass) != True:
                messages.error(request, "password must be 8 characters, 1 Uppercase, 1 Lowercase, 1 special character")
        
            elif new_pass != confirm_new_pass and new_pass:
                messages.error(request, "password does not match")
            else:
                user_password = new_pass
                hashed_password = hash_password(user_password)
                admin_details.passwd = hashed_password
                admin_details.save()
                del request.session['admin_recovery_email']
                return redirect('admin_login')
            
            
    return render(request, 'admin/admin_recovery_pass.html')
    
    