from django.contrib import admin
from integration.models import Integration, IntegrationLines


@admin.register(Integration)
class IntegrationAdmin(admin.ModelAdmin):
    pass


@admin.register(IntegrationLines)
class IntegrationLines(admin.ModelAdmin):
    pass


