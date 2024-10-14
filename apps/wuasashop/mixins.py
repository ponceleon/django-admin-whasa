import xmlrpc.client
from rest_framework.response import Response
from rest_framework import status
import environ

env = environ.Env()

url = env("ODOO_URL") 'https://productos.digital'
db = env("ODOO_DB")'odoo'
username = env("ODOO_USER") 'admin'
password = env("ODOO_PASS") 'admin'


class OdooConnectionMixin:
    def odoo_execute(self, model, method, *args, **kwargs):
        common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
        uid = common.authenticate(db, username, password, {})

        if not uid:
            return Response({"error": "Autenticación fallida"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
            return models.execute_kw(db, uid, password, model, method, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
