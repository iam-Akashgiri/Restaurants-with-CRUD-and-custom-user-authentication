from django.shortcuts import render

from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Food, Categories
from .forms import FoodForm, CategoriesForm

# Create your views here.

class FoodListView(ListView):
    model = Food
    template_name = ['food_list.html','category/categories_list.html']
    template_name = 'food_list.html'
    def get_context_data(self):
        context = super(FoodListView, self).get_context_data()
        context['food_list'] = Food.objects.all()
        context['categories_list'] = Categories.objects.all()
        return context

class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail.html'


class FoodCreateView(CreateView):
    model = Food
    form_class = FoodForm
    template_name = 'food_form.html'
    success_url = reverse_lazy('food_list')

class FoodUpdateView(UpdateView):
    model = Food
    form_class = FoodForm
    template_name = 'food_form.html'
    success_url = reverse_lazy('food_list')

class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'confirm_delete_food.html'
    success_url = reverse_lazy('food_list')


## CATEGORIES

class CategoriesDetailView(DetailView):
    model = Categories
    template_name = 'category/categories_detail.html'


class CategoriesCreateView(CreateView):
    model = Categories
    form_class = CategoriesForm
    template_name = 'category/categories_form.html'
    success_url = reverse_lazy('food_list')


def categories_filter(request,id):
    cat_id = int(id)
    cat_name = Categories.objects.get(id = cat_id)

    cat_food= Food.objects.filter(category_id = cat_id)
    a = {'cat_food': cat_food, 'cat_name': cat_name}
    return render(request, 'category/categories_list.html', {'data':a})



## Login Form

from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import *
from django.contrib.auth.hashers import make_password,check_password


# Create your views here.

def homePage(request):
 if request.method == 'POST':
        food = request.POST.get('food')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(food)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(food)
                    else:
                        cart[food] = quantity - 1
                else:
                    cart[food] = quantity + 1
            else:
                cart[food] = 1
        else:
            cart = {}
            cart[food] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('food_list')

 else:
   foods=None
   categories=Categories.objects.all()
   category_ids = request.GET.get('category_id')
   if category_ids:
        foods = Food.objects.filter(category_id=category_ids)
   else:
        foods = Food.objects.filter(category_id=1)
   context = {'products':foods , 'categories':categories}
   print("Your Email Address is: ", request.session.get('email'))
   return redirect('login')


def login(request):
   if request.method == "GET":
        return render(request, 'login.html')
   else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_msg = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email
                request.session['first_name'] = customer.first_name
                return redirect("food_list")
            else:
                error_msg = "Email or Password is incorrect."
        else:
            error_msg = "Email or Password is incorrect."
        return render(request, 'login.html', {'error_msg': error_msg})


def signup(request):
   if request.method =='GET':
     return render(request,'signup.html')
   else :
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
        values = {
            'firstname': first_name,
            'lastname': last_name,
            'phone': phone,
            'email': email,
        }
        err_msg = None

        if not first_name:
            err_msg = "First Name Required."
        elif len(first_name) < 3:
            err_msg = "First Name must be 3 characters long."
        elif not last_name:
            err_msg = "Last Name Required."
        elif len(last_name) < 3:
            err_msg = "Last Name must be 3 characters long."
        elif not phone:
            err_msg = "Phone is Required."
        elif len(phone) < 10:
            err_msg = "Phone Number must be 10 characters long."
        elif not email:
            err_msg = "Email is Required."
        if not err_msg:
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('login') 
        else:
            return render(request, 'signup.html', {'error_msg': err_msg,'values':values})
        
def logout(request):
    request.session.clear()
    return redirect('login')

def cart(request):
    cart_food_id = list(request.session.get('cart').keys())
    cart_food = Food.get_foods_by_id(cart_food_id)
    print(cart_food)
    return render(request, 'cart.html',{'cart_food': cart_food})

def checkout(request):

    if request.method == "POST":
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        cart = request.session.get("cart")
        foods = Food.get_foods_by_id(list(cart.keys()))

        for food in foods:
            order = Order( food=food, price=food.price, address=address,
                          phone=phone, quantity=cart.get(str(food.id)))
            order.save()


        request.session['cart'] = {}

        return redirect("food_list")
    else:
        return render(request, 'checkout.html') 