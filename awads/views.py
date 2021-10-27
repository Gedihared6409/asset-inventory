from django.shortcuts import render,redirect
from .forms import  OrderForm,CreateUserForm,CustomerForm,OrderFormAdmin
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
# Create your views here.
from .filters import OrderFilter
from django.shortcuts import render
from .models import *
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def welcome(request):
     return render(request, 'accounts/index.html')
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm(request.POST)
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
          
            messages.success(request, 'account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'accounts/register.html', context)
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
                messages.info(request,'Username or password is incrorrect')
    context = {}
    return render(request, 'accounts/login.html', context)
def logoutUser(request):
	logout(request)
	return redirect('home')
@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_customers = customers.count()
    
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    Out_for_delivery = orders.filter(status='Out for delivery').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers,
    'total_orders':total_orders,'delivered':delivered,
    'pending':pending ,'Out_for_delivery':Out_for_delivery}
    
    return render(request, 'accounts/dashboard.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles= ['employee'])
def accountSettings(request):
        customer = request.user.customer
        print(customer)
        form = CustomerForm(instance=customer)
        if request.method == 'POST':
            form = CustomerForm(request.POST, request.FILES,instance=customer)
            if form.is_valid():
                form.save()
        context = {'form':form}
        return render(request, 'accounts/acccounts_setting.html',context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles= ['admin'])
# def products(request):
#     products = Product.objects.all()

#     return render(request, 'accounts/products.html',{'products':products})
@login_required(login_url='login')
@allowed_users(allowed_roles= ['admin'])
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    print(customer)

    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs 
    

    # context = {'customer':customer, 'orders':orders, 'order_count':order_count,
    # 'myFilter':myFilter}
    context = {'customer':customer,'orders':orders,'order_count':order_count, 'myFilter':myFilter}
    return render(request, 'accounts/customer.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles= ['employee'])
def userPage(request):
    customer = request.user.customer
   
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    Out_for_delivery = orders.filter(status='Out for delivery').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders':orders, 'Out_for_delivery':Out_for_delivery, 'customer' :customer, 'total_orders':total_orders,'delivered':delivered,
    'pending':pending }
    return render(request,'accounts/user.html',context)

def userPageform(request,pk_test):
    form = OrderForm()
    userr = request.user.customer
    
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
                obj = form.save(commit=False)
                obj.customer = userr
                obj.save()
                return redirect('home')

    context = {'form':form ,'userr':userr}
    
    return render(request,'accounts/new_Asset_form.html',context)

def userrepairPageform(request,pk_test):
    reuserr = request.user.customer
    form = OrderForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = reuserr
            obj.save()
            return redirect('home')

    context = {'form':form}
    
    return render(request,'accounts/repair_Asset_form.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles= ['admin'])
def createOrder(request,pk):
    result = request.user
    
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles= ['admin'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    
    form = OrderFormAdmin(instance=order)
    if request.method == 'POST':
        form = OrderFormAdmin(request.POST, instance=order)
        if form.is_valid():
            ref = form.save()
            print(ref.status)
            return redirect('home')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles= ['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('home')


    context = {'item':order}
    return render(request, 'accounts/delete.html', context)


