from django.urls import path
from .views import TablUpd, UsdUpd, telegram_send, web_request, canserv_index

urlpatterns = [
    path('', canserv_index, name='index'),
    path('tabupd/', TablUpd, name='TablUpd'),
    path('usdupd/', UsdUpd, name='UsdUpd'),
    path('tgmsg/', telegram_send, name='telegram_send'),
    path('wr/', web_request, name='web_request'),
]