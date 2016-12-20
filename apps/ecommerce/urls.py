from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product$', views.product, name='product'),
    url(r'^admin$', views.admin, name="admin"),
    url(r'^orders$', views.orders, name="orders"),
    url(r'^products$', views.products, name='products'),
    url(r'^show$', views.show, name='show'),
    url(r'^test$', views.test, name='test'),
    url(r'^add_product$', views.add_product, name='add_product')

]
