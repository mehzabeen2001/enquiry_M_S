from django.contrib import admin
from . models import adminDatabase,userDatabase,queryDatabase

# Register your models here.
admin.site.register(adminDatabase)
admin.site.register(userDatabase)
admin.site.register(queryDatabase)