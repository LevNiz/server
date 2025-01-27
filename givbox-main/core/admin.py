from django.contrib import admin
from django.db.models import QuerySet

from core import models
from django.utils.translation import gettext as _

from django.utils.html import format_html, mark_safe
import datetime
import requests
from PIL import Image
from io import BytesIO


def save_photo(data):
    headers = {
        "Content-Type": "application/json, charset=utf-8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*"
    }
    for i in data:
        if i.imagelink:
            image_link = i.imagelink
            response = requests.get(f'{image_link}', headers=headers)
            name_txt = i.name.split()
            name = '_'.join(name_txt)
            current_time = datetime.datetime.now()
            milliseconds = int(current_time.timestamp() * 1000)

            i.image.save(f"{name}_{milliseconds}.jpg", ContentFile(response.content), save=False)
            # i.sizes = ['XXS', 'XS', 'S', 'M', 'L', 'XL']
            i.save()


class DepotUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'login']

    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        (_('Personal info'), {'fields': ('depot', 'user_type')}),
    )
    readonly_fields = ('user_type',)

    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            obj.set_password(form.cleaned_data['password'])
        obj.save()


class CartItemsAdmin(admin.StackedInline):
    model = models.CartItems


class ModelOrderAdmin(admin.ModelAdmin):
    # inlines = [CartItemsAdmin]

    list_display = ('id', 'storeName', 'addresses', 'date', 'status', 'totalCost', 'isoptovik')
    list_filter = ('isoptovik',)
    search_fields = ['storeName']

    fieldsets = (
        (_('Информация о заказе'), {'fields': ('store', 'totalCost', 'client', 'bonus', 'addresses',
                                               'phone', 'comment', 'storeName', 'storeLogo', 'status', 'pay_status')}),
    )


from django.core.files.base import ContentFile


@admin.action(description="Сохранить фото")
def save_image(self, request, qs: QuerySet):
    save_photo(qs)


@admin.action(description="Установить описание")
def set_description(self, request, qs: QuerySet):
    items = models.ModelItem.objects.filter(supplier_id=135, category=5)
    for item in items:
        if item.description == '-' or item.description is None:
            item.description = 'Полное описание товара можете посмотреть на официальном сайте - https://www.underarmour.com/en-us/c/mens/shoes/'
            item.save()


@admin.action(description="Удалить дупликаты")
def delete_duplicate(self, request, qs: QuerySet):
    items = models.ModelItem.objects.filter(category_id=3)
    for item in models.ModelItem.objects.filter(category_id=3):
        name = item.name
        duplicate_items = models.ModelItem.objects.filter(name=name)
        if len(duplicate_items) > 1:
            for i in range(1, len(duplicate_items)):
                duplicate_items[i].delete()


class ItemAdmin(admin.ModelAdmin):

    def image_tag(self, obj):

        try:
            if obj.imagelink:
                return mark_safe('<img src="{}" width="100" height="100" />'.format(obj.imagelink))

            else:
                return mark_safe('<img src="{}" width="100" height="100" />'.format(obj.image.url))

        except:
            pass

    image_tag.short_description = 'Фото товара'
    image_tag.allow_tags = True

    list_display = ('name', 'cost', 'supplier', 'image_tag')
    # list_filter = ('category__id', 'supplier__id')
    readonly_fields = ('image_tag',)
    actions = [save_image, set_description]

    search_fields = ('name',)
    list_filter = (
        ('isoptovik', admin.BooleanFieldListFilter),
        'category', 'supplier'
    )


admin.site.register(models.ModelDepots)
admin.site.register(models.ModelPackage)
admin.site.register(models.ModelAlaket)
admin.site.register(models.ModelImage)
admin.site.register(models.ModelRequests)
admin.site.register(models.ModelPackageData)
admin.site.register(models.DepotUser, DepotUserAdmin)
admin.site.register(models.ModelAddresses)
admin.site.register(models.BuyerBanners)
admin.site.register(models.ModelItem, ItemAdmin)
admin.site.register(models.ModelOrder, ModelOrderAdmin)
admin.site.register(models.ModelVideo)
admin.site.register(models.ModelItemSearchRequest)
admin.site.register(models.ModelBuyerRequest)
