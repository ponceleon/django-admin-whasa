from django.contrib import admin
from .models import WUser, Role, WUserRole, Odoo, WUserOdoo, Commerce, WUserCommerce, Cart


@admin.register(WUser)
class WUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'phone', 'status_id', 'created', )
    search_fields = ('name', 'lastname', 'email', )
    list_filter = ('status_id', 'created', )
    ordering = ('-created', )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(WUserRole)
class WUserRoleAdmin(admin.ModelAdmin):
    list_display = ('wuser', 'role', 'status_id', 'created', 'modified', )
    search_fields = ('wuser__name', 'role__name', )
    list_filter = ('status_id', 'created', 'modified', )


@admin.register(Odoo)
class OdooAdmin(admin.ModelAdmin):
    list_display = ('url', 'dbname', 'created', )
    search_fields = ('url', 'dbname', )
    ordering = ('-created', )


@admin.register(WUserOdoo)
class WUserOdooAdmin(admin.ModelAdmin):
    list_display = ('wuser', 'odoo', 'status_id', 'created', 'updated', )
    search_fields = ('wuser__name', 'odoo__dbname', )
    list_filter = ('status_id', 'created', 'updated', )


@admin.register(Commerce)
class CommerceAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'has_sedes', 'odoos', 'created', 'updated', )
    search_fields = ('name', 'country', )
    list_filter = ('has_sedes', 'country', 'created', 'updated', )


@admin.register(WUserCommerce)
class WUserCommerceAdmin(admin.ModelAdmin):
    list_display = ('wuser', 'commerce', 'status_id', 'created', 'updated', )
    search_fields = ('wuser__name', 'commerce__name', )
    list_filter = ('status_id', 'created', 'updated', )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('wuser', 'companie', 'updated', )
    search_fields = ('wuser__name', )
    list_filter = ('updated',)
    ordering = ('-updated',)
