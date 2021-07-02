from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api.views import StocksList

router = SimpleRouter()
router.register(r'stocks', StocksList)

urlpatterns = [
    path('', include(router.urls)),
]