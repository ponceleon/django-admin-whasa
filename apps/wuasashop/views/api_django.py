from rest_framework import viewsets
from apps.wuasashop.models import WUser, Role, WUserRole, Odoo, WUserOdoo, Commerce, WUserCommerce, Cart
from apps.wuasashop.serializers import (
    WUserSerializer,
    RoleSerializer,
    WUserRoleSerializer,
    OdooSerializer,
    WUserOdooSerializer,
    CommerceSerializer,
    WUserCommerceSerializer,
    CartSerializer
)


class WUserViewSet(viewsets.ModelViewSet):
    queryset = WUser.objects.all()
    serializer_class = WUserSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class WUserRoleViewSet(viewsets.ModelViewSet):
    queryset = WUserRole.objects.all()
    serializer_class = WUserRoleSerializer


class OdooViewSet(viewsets.ModelViewSet):
    queryset = Odoo.objects.all()
    serializer_class = OdooSerializer


class WUserOdooViewSet(viewsets.ModelViewSet):
    queryset = WUserOdoo.objects.all()
    serializer_class = WUserOdooSerializer


class CommerceViewSet(viewsets.ModelViewSet):
    queryset = Commerce.objects.all()
    serializer_class = CommerceSerializer


class WUserCommerceViewSet(viewsets.ModelViewSet):
    queryset = WUserCommerce.objects.all()
    serializer_class = WUserCommerceSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
