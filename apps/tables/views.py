from django.shortcuts import render, redirect
from django.db.models import F, ExpressionWrapper, DecimalField, Sum
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import json

from apps.settings.models import Setting
from apps.tables.models import Table, TableOrder, TableOrderItem
from apps.tables.forms import AddToOrderForm
from apps.products.models import Product
from apps.categories.models import Category

# Create your views here.
def menu(request, table_uuid):
    table = Table.objects.get(number=table_uuid)
    setting = Setting.objects.latest('id')
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'menu/index.html', locals())

def category_menu_detail(request, table_uuid, category_slug):
    table = Table.objects.get(number=table_uuid)
    setting = Setting.objects.latest('id')
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'menu/category.html', locals())

def add_to_order(request):
    print("add to order")
    print(request.method)
    if request.method == 'POST':
        form = AddToOrderForm(request.POST)
        if form.is_valid():
            table_uuid = form.cleaned_data['table_uuid']
            product_id = form.cleaned_data['product_id']
            print("WORK",product_id)
            quantity = form.cleaned_data['quantity']
            price = form.cleaned_data['price']
            print(type(price))
            product = Product.objects.get(id=product_id)

            # Получаем или создаем корзину для текущей сессии
            session_key = request.session.session_key
            if not session_key:
                request.session.save()
                session_key = request.session.session_key

            table_instance = Table.objects.get(number=table_uuid)
            table, _ = TableOrder.objects.get_or_create(session_key=session_key, menu_table=table_instance)

            # Получаем объект CartItem по cart и product
            table_item = TableOrderItem.objects.filter(table=table, product=product).first()

            # Если CartItem существует, обновляем его количество, иначе создаем новый объект
            if table_item:
                print(table_item.total + price)
                table_item.total += price * quantity
                table_item.quantity += quantity
                table_item.save()
            else:
                table_item = TableOrderItem.objects.create(table=table, product=product, quantity=quantity, total=price * quantity)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
    return redirect('order')

def order(request, table_uuid):
    setting = Setting.objects.latest('id')
    table = Table.objects.get(number=table_uuid)
    session_key = request.session.session_key
    order = TableOrder.objects.filter(session_key=session_key).first()
    cart_items = []
    if order:
        cart_items = TableOrderItem.objects.filter(table=order).annotate(
            total_price=ExpressionWrapper(F('product__price') * F('quantity'), output_field=DecimalField())
        )
        total_price = cart_items.aggregate(total=Sum('total_price'))['total'] or 0
    else:
        cart_items = []
        total_price = 0
    form = AddToOrderForm()
    return render(request, 'menu/order.html', locals())

def table_update_cart_item(request):
    try:
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']

        cart = TableOrder.objects.filter(session_key=request.session.session_key).first()
        if not cart:
            return JsonResponse({'error': 'Cart not found'}, status=404)

        cartItem = TableOrderItem.objects.get(table=cart, product_id=productId)

        if action == "increase":
            cartItem.quantity += 1
        elif action == "decrease" and cartItem.quantity > 1:
            cartItem.quantity -= 1

        cartItem.save()
        return JsonResponse({'success': True})

    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Item not found in cart'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def table_clear_cart(request):
    session_key = request.session.session_key
    if session_key:
        TableOrderItem.objects.filter(table__session_key=session_key).delete()

    return redirect('cart')

def table_remove_from_cart(request, product_id, table_uuid):
    session_key = request.session.session_key
    if session_key:
        TableOrderItem.objects.filter(table__session_key=session_key, product__id=product_id).delete()

    return redirect('order', table_uuid)

def table_cart_items_count_processor(request):
    session_key = request.session.session_key
    if not session_key:
        return {'cart_items_count': 0}

    count = TableOrderItem.objects.filter(table__session_key=session_key).count()
    return {'cart_items_count': count}