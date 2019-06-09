from django.contrib import admin
from integration.models import Integration, IntegrationLines, IntegrationModule, IntegrationRepository, IntegrationServer, IntegrationServerDB


@admin.register(Integration)
class IntegrationAdmin(admin.ModelAdmin):
    pass


@admin.register(IntegrationLines)
class IntegrationLinesAdmin(admin.ModelAdmin):
    pass

@admin.register(IntegrationModule)
class IntegrationModuleAdmin(admin.ModelAdmin):
    pass

@admin.register(IntegrationRepository)
class IntegrationRepositoryAdmin(admin.ModelAdmin):
    pass

@admin.register(IntegrationServer)
class IntegrationServerAdmin(admin.ModelAdmin):
    pass

@admin.register(IntegrationServerDB)
class IntegrationServerDBAdmin(admin.ModelAdmin):
    pass