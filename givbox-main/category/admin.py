from django.contrib import admin

from category import models


class ModelCostsAdmin(admin.ModelAdmin):
    list_display = ('fromCity', 'toCity', 'costPerKg', 'id')


admin.site.register(models.ModelWH)
admin.site.register(models.ModelContact)
admin.site.register(models.ModelCountry)
admin.site.register(models.ModelCity)
admin.site.register(models.ModelPackageType)
admin.site.register(models.ModelNotification)
admin.site.register(models.ModelCosts, ModelCostsAdmin)
admin.site.register(models.ModelTariff)
admin.site.register(models.ModelCurrency)
admin.site.register(models.ModelWebsite)
admin.site.register(models.Category)
admin.site.register(models.SubCategory)
admin.site.register(models.StoreCategory)
admin.site.register(models.ModelFranchiseRequest)
admin.site.register(models.ModelGbBusinessRequest)
admin.site.register(models.ModelFile)
admin.site.register(models.ModelExtraService)
admin.site.register(models.ModelColor)
admin.site.register(models.ModelMemory)
