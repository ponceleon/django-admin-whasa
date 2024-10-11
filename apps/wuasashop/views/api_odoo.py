from rest_framework import status, viewsets
from rest_framework.response import Response
from apps.wuasashop.mixins import OdooConnectionMixin
from apps.wuasashop.serializers import (
    CompanyDataSerializer, ProductDataSerializer, CategoryDataSerializer,
    OrderDataSerializer, PaymentDataSerializer
)


class CompanyViewSet(OdooConnectionMixin, viewsets.ViewSet):
    serializer_class = CompanyDataSerializer

    def list(self, request):
        company_data = self.odoo_execute('res.company', 'search_read', [[]], {
            'fields': ['name', 'street', 'city', 'country_id', 'phone', 'email']
        })

        if isinstance(company_data, Response):
            return company_data

        return Response({"company_data": company_data}, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = CompanyDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        company_data = serializer.validated_data
        result = self.odoo_execute('res.company', 'create', [company_data])

        if isinstance(result, dict) and "error" in result:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "message": "Datos de prueba creados exitosamente",
            "company_id": result,
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        company_data = self.odoo_execute('res.company', 'search_read', [[['id', '=', pk]]], {
            'fields': ['name', 'street', 'city', 'country_id', 'phone', 'email']
        })

        if isinstance(company_data, Response):
            return company_data

        if not company_data:
            return Response({"error": "Empresa no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        return Response(company_data[0], status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        serializer = CompanyDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        company_data = serializer.validated_data
        success = self.odoo_execute('res.company', 'write', [[pk], company_data])

        if not success:
            return Response({"message": "Datos de la empresa NO se actualizaron"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "message": "Datos de la empresa actualizados exitosamente",
            "data": request.data,
        }, status=status.HTTP_200_OK)


class ProductViewSet(OdooConnectionMixin, viewsets.ViewSet):
    serializer_class = ProductDataSerializer

    def list(self, request):
        products = self.odoo_execute('product.product', 'search_read', [[]], {
            'fields': ['name', 'description', 'list_price', 'categ_id', 'company_id']
        })

        if isinstance(products, Response):
            return products

        return Response(products, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ProductDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_data = serializer.validated_data
        result = self.odoo_execute('product.product', 'create', [product_data])

        if isinstance(result, dict) and "error" in result:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "message": "Producto creado exitosamente",
            "product_id": result,
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = self.odoo_execute('product.product', 'search_read', [[['id', '=', pk]]], {
            'fields': ['name', 'description', 'list_price', 'categ_id']
        })

        if isinstance(product, Response):
            return product

        if not product:
            return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        return Response(product[0], status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        serializer = ProductDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_data = serializer.validated_data
        success = self.odoo_execute('product.product', 'write', [[pk], product_data])

        if not success:
            return Response({"message": "El producto no se pudo actualizar"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "message": "Producto actualizado exitosamente",
            "data": request.data,
        }, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        success = self.odoo_execute('product.product', 'unlink', [[pk]])

        if not success:
            return Response({"message": "El producto no se pudo eliminar"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "message": "Producto eliminado exitosamente",
        }, status=status.HTTP_204_NO_CONTENT)


class CategoryViewSet(OdooConnectionMixin, viewsets.ViewSet):
    serializer_class = CategoryDataSerializer

    def list(self, request):
        categories = self.odoo_execute('product.public.category', 'search_read', [[]], {
            'fields': ['name', 'parent_id', 'sequence']
        })

        if isinstance(categories, Response):
            return categories

        return Response(categories, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = CategoryDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        category_data = serializer.validated_data
        result = self.odoo_execute('product.public.category', 'create', [category_data])

        if isinstance(result, dict) and "error" in result:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "message": "Categoría creada exitosamente",
            "category_id": result,
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        category = self.odoo_execute('product.public.category', 'search_read', [[['id', '=', pk]]], {
            'fields': ['name', 'parent_id', 'sequence']
        })

        if isinstance(category, Response):
            return category

        if not category:
            return Response({"error": "Categoría no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        return Response(category[0], status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        serializer = CategoryDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        category_data = serializer.validated_data
        success = self.odoo_execute('product.public.category', 'write', [[pk], category_data])

        if not success:
            return Response({"message": "La categoría no se pudo actualizar"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "message": "Categoría actualizada exitosamente",
            "data": request.data,
        }, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        success = self.odoo_execute('product.public.category', 'unlink', [[pk]])

        if not success:
            return Response({"message": "La categoría no se pudo eliminar"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "message": "Categoría eliminada exitosamente",

        }, status=status.HTTP_204_NO_CONTENT)


class OrderViewSet(OdooConnectionMixin, viewsets.ViewSet):
    serializer_class = OrderDataSerializer

    def list(self, request):
        partners = self.odoo_execute('res.partner', 'search_read', [[]], {'fields': ['name', 'email'], 'limit': 5})
        print("Partners:", partners)

        orders = self.odoo_execute('sale.order', 'search_read', [[]], {
            'fields': ['name', 'partner_id', 'date_order', 'state', 'amount_total', 'invoice_status'],
            'order': 'name asc'
        })

        if isinstance(orders, Response):
            return orders

        return Response(orders, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = OrderDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order_data = serializer.validated_data
        result = self.odoo_execute('sale.order', 'create', [order_data])

        if isinstance(result, dict) and "error" in result:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "message": "Orden creada exitosamente",
            "order_id": result,
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        order = self.odoo_execute('sale.order', 'search_read', [[['id', '=', pk]]], {
            'fields': ['name', 'partner_id', 'date_order', 'state', 'amount_total', 'invoice_status', 'order_line']
        })

        if isinstance(order, Response):
            return order

        if not order:
            return Response({"error": "Orden no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        return Response(order[0], status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        serializer = OrderDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order_data = serializer.validated_data
        success = self.odoo_execute('sale.order', 'write', [[pk], order_data])

        if not success:
            return Response({"message": "La orden no se pudo actualizar"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "message": "Orden actualizada exitosamente",
            "data": request.data,
        }, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        success = self.odoo_execute('sale.order', 'unlink', [[pk]])

        if not success:
            return Response({"message": "La orden no se pudo eliminar"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "message": "Orden eliminada exitosamente",
        }, status=status.HTTP_204_NO_CONTENT)


class PaymentViewSet(OdooConnectionMixin, viewsets.ViewSet):
    serializer_class = PaymentDataSerializer

    def list(self, request):
        payments = self.odoo_execute('account.payment', 'search_read', [[['state', '=', 'posted']]], {
            'fields': ['name', 'payment_type', 'partner_id', 'amount', 'currency_id', 'state']
        })

        if isinstance(payments, Response):
            return payments

        return Response(payments, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = PaymentDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        payment_data = serializer.validated_data
        result = self.odoo_execute('account.payment', 'create', [payment_data])

        if isinstance(result, dict) and "error" in result:
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "message": "Pago creado exitosamente",
            "payment_id": result,
        }, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        payment = self.odoo_execute('account.payment', 'search_read', [[['id', '=', pk]]], {
            'fields': ['name', 'payment_type', 'partner_id', 'amount', 'currency_id', 'payment_date', 'state']
        })

        if isinstance(payment, Response):
            return payment

        if not payment:
            return Response({"error": "Pago no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        return Response(payment[0], status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        serializer = PaymentDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        payment_data = serializer.validated_data
        success = self.odoo_execute('account.payment', 'write', [[pk], payment_data])

        if not success:
            return Response({"message": "El pago no se pudo actualizar"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "message": "Pago actualizado exitosamente",
            "data": request.data,
        }, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        success = self.odoo_execute('account.payment', 'unlink', [[pk]])

        if not success:
            return Response({"message": "El pago no se pudo eliminar"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "message": "Pago eliminado exitosamente",
        }, status=status.HTTP_204_NO_CONTENT)
