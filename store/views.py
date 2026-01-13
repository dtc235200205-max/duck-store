from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Order, OrderItem, Comment, Notification
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import UserProfileForm
import json

def home(request):
    products = Product.objects.all()[:10]
    return render(request, 'store/home.html', {'products': products})

def product_list(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')
    products = Product.objects.all()
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    if category_id:
        products = products.filter(category_id=category_id)
    categories = Category.objects.all()
    return render(request, 'store/product_list.html', {'products': products, 'categories': categories})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = Comment.objects.filter(product=product)
    if request.method == 'POST' and request.user.is_authenticated:
        text = request.POST.get('comment')
        Comment.objects.create(product=product, user=request.user, text=text)
        return redirect('product_detail', pk=pk)
    return render(request, 'store/product_detail.html', {'product': product, 'comments': comments})

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', {})
    cart[str(pk)] = cart.get(str(pk), 0) + 1
    request.session['cart'] = cart
    messages.success(request, f'{product.name} added to cart.')
    return redirect('product_list')

@login_required
def buy_now(request, pk):
    """Direct checkout for a single product"""
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        # Create a temporary cart with just this product
        request.session['cart'] = {str(pk): 1}
        return redirect('checkout')
    return redirect('product_detail', pk=pk)

@login_required
def cart(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for pk, qty in cart.items():
        product = get_object_or_404(Product, pk=int(pk))
        subtotal = product.price * qty
        total += subtotal
        items.append({'product': product, 'quantity': qty, 'subtotal': subtotal})
    return render(request, 'store/cart.html', {'items': items, 'total': total})

@login_required
def update_cart(request, pk):
    if request.method == 'POST':
        qty = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        if qty > 0:
            cart[str(pk)] = qty
        else:
            cart.pop(str(pk), None)
        request.session['cart'] = cart
    return redirect('cart')

@login_required
def checkout(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, 'Cart is empty.')
            return redirect('cart')
        payment_method = request.POST.get('payment_method')
        discount_code = request.POST.get('discount_code')
        delivery_address = request.POST.get('delivery_address')
        order = Order.objects.create(user=request.user, payment_method=payment_method, discount_code=discount_code, delivery_address=delivery_address)
        total = 0
        for pk, qty in cart.items():
            product = get_object_or_404(Product, pk=int(pk))
            OrderItem.objects.create(order=order, product=product, quantity=qty, price=product.price)
            total += product.price * qty
        order.total_price = total
        order.save()
        request.session['cart'] = {}
        messages.success(request, 'Order placed successfully.')
        return redirect('order_detail', pk=order.pk)
    return render(request, 'store/checkout.html')

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/order_list.html', {'orders': orders})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    items = OrderItem.objects.filter(order=order)
    return render(request, 'store/order_detail.html', {'order': order, 'items': items})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})

# Admin views
@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('home')
    orders = Order.objects.all()
    products = Product.objects.all()
    users = User.objects.all()
    return render(request, 'store/admin_dashboard.html', {'orders': orders, 'products': products, 'users': users})

@login_required
def manage_products(request):
    if not request.user.is_superuser:
        return redirect('home')
    products = Product.objects.all()
    return render(request, 'store/manage_products.html', {'products': products})

@login_required
def manage_users(request):
    if not request.user.is_superuser:
        return redirect('home')
    users = User.objects.all()
    return render(request, 'store/manage_users.html', {'users': users})

@login_required
def statistics(request):
    if not request.user.is_superuser:
        return redirect('home')
    # Simple stats
    total_orders = Order.objects.count()
    total_revenue = sum(order.total_price for order in Order.objects.all())
    top_products = Product.objects.all()[:5]  # Placeholder
    return render(request, 'store/statistics.html', {'total_orders': total_orders, 'total_revenue': total_revenue, 'top_products': top_products})

# Additional features placeholders
def qr_donate(request):
    return render(request, 'store/qr_donate.html')

def ai_consultation(request):
    # Placeholder for AI integration
    return render(request, 'store/ai_consultation.html')

def notifications(request):
    if request.user.is_authenticated:
        notifs = Notification.objects.filter(user=request.user, is_read=False)
        return render(request, 'store/notifications.html', {'notifications': notifs})
    return redirect('login')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thông tin cá nhân đã được cập nhật thành công!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'store/profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Mật khẩu của bạn đã được thay đổi thành công!')
            return redirect('profile')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'store/change_password.html', {'form': form})
