from django.db import models


class WUser(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    data = models.JSONField(default=dict, blank=True)
    status_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.lastname}"


class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class WUserRole(models.Model):
    wuser = models.ForeignKey(WUser, on_delete=models.CASCADE, related_name="roles")
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    status_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Odoo(models.Model):
    url = models.URLField(max_length=255)
    dbname = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dbname


class WUserOdoo(models.Model):
    wuser = models.ForeignKey(WUser, on_delete=models.CASCADE, related_name="odoos")
    odoo = models.ForeignKey(Odoo, on_delete=models.CASCADE)
    status_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Commerce(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    has_sedes = models.BooleanField(default=False)
    odoos = models.ForeignKey(Odoo, on_delete=models.SET_NULL, null=True, related_name="associated_commerces")
    data = models.JSONField(default=dict, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class WUserCommerce(models.Model):
    wuser = models.ForeignKey(WUser, on_delete=models.CASCADE, related_name="user_commerces")
    commerce = models.ForeignKey(Commerce, on_delete=models.CASCADE)
    status_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    wuser = models.ForeignKey(WUser, on_delete=models.CASCADE, related_name="company_carts")
    companie = models.ForeignKey(Commerce, on_delete=models.SET_NULL, null=True, related_name="company_carts")
    cart = models.JSONField(default=dict, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.uid} for {self.wuser}"
