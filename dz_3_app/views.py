from datetime import datetime, timedelta
from django.shortcuts import render
from dz_3_app.models import Order, User, Goods


def index(request):
    return render(request, 'base.html')


def user_orders(request, user_id, days):
    point = datetime.today() - timedelta(days=days)
    user = User.objects.filter(pk=user_id).first()
    if user:
        orders = Order.objects.filter(user_ID=user, creation_date__gte=point)
        orders_list = {}
        for order in orders:
            item = order.goods_ID
            order_dict = {'Creation_date': order.creation_date,
                          'Goods': item.title,
                          'Quantity': order.quantity,
                          'Amount': order.amount}
            orders_list[f'Order_{order.id}'] = order_dict

            # orders_list += [f'Товар: {item.title}, Дата заказа: {order.creation_date}, '
            #                 f'Количество:{order.quantity}, Сумма: {order.amount}']

        context = {'User': user.name,
                   'Orders': orders_list}

        return render(request, 'user_orders.html', context)
    context = {'Error': 'Заказчик не найден'}
    return render(request, 'error.html', context)
