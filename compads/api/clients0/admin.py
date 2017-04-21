from django.contrib import admin

import api.clients.models as models

admin.site.register(models.Client)
admin.site.register(models.ClientType)
admin.site.register(models.Phone)
admin.site.register(models.PhoneType)
admin.site.register(models.Email)
admin.site.register(models.EmailType)
admin.site.register(models.Address)
admin.site.register(models.AddressType)
admin.site.register(models.BirthDate)
