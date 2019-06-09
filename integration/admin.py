from django.contrib import admin
from integration.models import Integration


@admin.register(Integration)
class IntegrationAdmin(admin.ModelAdmin):
    pass


