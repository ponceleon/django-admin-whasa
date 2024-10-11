from rest_framework.routers import DefaultRouter
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import path, include
from apps.wuasashop.views.api_django import (
    WUserViewSet,
    RoleViewSet,
    WUserRoleViewSet,
    OdooViewSet,
    WUserOdooViewSet,
    CommerceViewSet,
    WUserCommerceViewSet,
    CartViewSet
)

from apps.wuasashop.views.api_odoo import (
    CompanyViewSet, ProductViewSet, CategoryViewSet,
    OrderViewSet, PaymentViewSet
)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'wusers': reverse('wuser-list', request=request, format=format),
        'roles': reverse('role-list', request=request, format=format),
        'wuserroles': reverse('wuserrole-list', request=request, format=format),
        'odoos': reverse('odoo-list', request=request, format=format),
        'wuserodoos': reverse('wuserodoo-list', request=request, format=format),
        'commerces': reverse('commerce-list', request=request, format=format),
        'wusercommerces': reverse('wusercommerce-list', request=request, format=format),
        'carts': reverse('cart-list', request=request, format=format),
    })


@api_view(['GET'])
def odoo_root(request, format=None):
    return Response({
        'get_company': reverse('get_company', request=request, format=format),
        'get_product': reverse('get_product', request=request, format=format),
        'get_category': reverse('get_category', request=request, format=format),
        'get_order': reverse('get_order', request=request, format=format),
        'get_payment': reverse('get_payment', request=request, format=format),
    })


router = DefaultRouter()
router.register(r'wusers', WUserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'wuserroles', WUserRoleViewSet)
router.register(r'odoos', OdooViewSet)
router.register(r'wuserodoos', WUserOdooViewSet)
router.register(r'commerces', CommerceViewSet)
router.register(r'wusercommerces', WUserCommerceViewSet)
router.register(r'carts', CartViewSet)


urlpatterns_odoo = [
    path('company/', CompanyViewSet.as_view({'get': 'list', 'post': 'create'}), name='get_company'),
    path('company/<int:pk>/', CompanyViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='detail_company'),
    path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='get_product'),
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='detail_product'),
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='get_category'),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='detail_category'),
    path('orders/', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='get_order'),
    path('orders/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='detail_order'),
    path('payments/', PaymentViewSet.as_view({'get': 'list', 'post': 'create'}), name='get_payment'),
    path('payments/<int:pk>/', PaymentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='detail_payment'),
]

urlpatterns = [
    path('', api_root, name='api-root'),
    path('odoo/', odoo_root, name='api-root'),
    path('odoo/', include(urlpatterns_odoo)),
    path('', include(router.urls)),
]
