from django.contrib import admin

from hello.models import Animal, Owner, Types

admin.site.register(Animal)
admin.site.register(Owner)
admin.site.register(Types)
