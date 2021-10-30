from django.urls import path
from .views import QRCodeGeneratorAPIView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('qrcode/', QRCodeGeneratorAPIView.as_view(), name='qrcode'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)