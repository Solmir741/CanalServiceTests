import re
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order_table, Auxiliary_table
import datetime
from django.db.models import Sum
# Create your views here.
PKEY = '1bRT3njCRVcLayIqkMS0nCE_p_gw1ea6f5P_sLwOl9o8'


def canserv_index(request):
    return render (request, 'index_cs.html')

# Получаем обновленные данные из гугл таблицы 
@api_view(['POST'])
def TablUpd(request):
    gtdata = []
    for d in request.data:
        gtdata.append(d.split(','))
    # минимальная защита от сторонних post запросов
    if gtdata[0][0]!= PKEY:
        print('pkey error')
        return Response({})
    gtdata = gtdata[1:]
    # проверка и выравнивание данных в таблице
    try:
        for f in gtdata:
            f[2] = f[2] if f[2].isdigit() else 0
            try:
                f.append(datetime.datetime.strptime(f[3], "%d.%m.%Y"))
            except:
                f.append(None)
        # обновляем таблицу
        usd = float(Auxiliary_table.objects.get(id = 1).exchange_rate)
        fields = ('serial', 'order', 'cost_usd', 'delivery_time', 'delivery_time_format')
        for row in gtdata:
            update_values = {}
            for i, val in enumerate(fields):
                update_values[val] = row[i]
            update_values['exist'] = True
            # пересчёт по существующему курсу
            try:
                update_values['cost_rub'] = float(update_values.get('cost_usd')) * usd
            except:
                update_values['cost_rub'] = 0
            # обновляем данные в БД
            Order_table.objects.update_or_create(order = update_values.get('order'), defaults = update_values)
            # убираем удаленные из таблицы строки
        Order_table.objects.filter(exist=False).delete()
        Order_table.objects.all().update(exist=False)
    except:
        pass
    return Response({})

# Получаем обновленные данные курса доллара
@api_view(['POST'])
def UsdUpd(request):
    update_values = {}
    try:
        # минимальная защита от сторонних post запросов
        if request.data.get('passkey') != PKEY:
            print('pkey error')
            return Response({})
        update_values['exchange_rate'] = request.data.get('usd')
        Auxiliary_table.objects.update_or_create(id = 1, defaults = update_values)
    except:
        print('usd update error!')
        pass
    return Response({})

# Получаем запрос и возвращаем ответ о просроченных заказах
@api_view(['GET'])
def telegram_send(request):
    pkey = re.sub(r'\s+', ' ', request.GET['pk'].strip())
    # минимальная защита от сторонних get запросов
    if pkey != PKEY:
        print('pkey error')
        return Response({})
    now = datetime.datetime.now()
    OverdueObj = Order_table.objects.filter(delivery_time_format__lt=now).values('order')
    return Response({OverdueObj})

# Получаем запрос и возвращаем данные таблицы и общая сумма заказов Frond-end (React)
@api_view(['GET'])
def web_request(request):
    pkey = re.sub(r'\s+', ' ', request.GET['pk'].strip())
    # минимальная защита от сторонних get запросов
    if pkey != PKEY:
        print('pkey error')
        return Response({})
    total = (Order_table.objects.all().aggregate(Sum('cost_rub'))).get('cost_rub__sum')
    print(total)
    return Response({'values': Order_table.objects.all().values().order_by('id'), 'total': total})