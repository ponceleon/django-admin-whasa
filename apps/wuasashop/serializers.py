from rest_framework import serializers
from .models import WUser, Role, WUserRole, Odoo, WUserOdoo, Commerce, WUserCommerce, Cart


class WUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WUser
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class WUserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WUserRole
        fields = '__all__'


class OdooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Odoo
        fields = '__all__'


class WUserOdooSerializer(serializers.ModelSerializer):
    class Meta:
        model = WUserOdoo
        fields = '__all__'


class CommerceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commerce
        fields = '__all__'


class WUserCommerceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WUserCommerce
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CompanyDataSerializer(serializers.Serializer):
    name = serializers.CharField(default=serializers.CurrentUserDefault())
    street = serializers.CharField()
    city = serializers.CharField()
    country_id = serializers.IntegerField()
    phone = serializers.CharField()
    email = serializers.EmailField()


class ProductDataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True, required=False)
    list_price = serializers.FloatField()
    categ_id = serializers.IntegerField()


class CategoryDataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    parent_id = serializers.IntegerField(required=False, allow_null=True)
    sequence = serializers.CharField(max_length=255)


class OrderDataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, read_only=True)
    partner_id = serializers.IntegerField()
    date_order = serializers.DateTimeField()
    state = serializers.CharField(read_only=True)
    amount_total = serializers.FloatField(read_only=True)
    order_line = serializers.ListField(child=serializers.JSONField())


class PaymentDataSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    payment_type = serializers.CharField()
    partner_id = serializers.IntegerField()
    amount = serializers.FloatField()
    currency_id = serializers.IntegerField()
    payment_date = serializers.DateField()
    state = serializers.CharField(read_only=True)
