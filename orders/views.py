from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save() # Сохраняем сам заказ (имя, адрес)
            
            # Перебираем товары в корзине и добавляем их в заказ
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            
            # Очищаем корзину
            cart.clear()
            print(f"ЗАКАЗ СОЗДАН: {order.id}") 
            return render(request, 'orders/order/created.html',
                          {'order': order})
        else:
            # ВОТ ЭТО ПОМОЖЕТ НАЙТИ ОШИБКУ
            print("ОШИБКА ФОРМЫ:", form.errors)        
            
            # Показываем страницу успеха
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
        
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})