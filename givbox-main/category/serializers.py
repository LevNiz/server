from rest_framework import serializers

from category import models
# from user.serializers import StoreSerializerOpen


class HourWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelWH
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelContact
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelCountry
        fields = ('id', 'nameKg', 'nameEn', 'nameRu', 'icon', 'code', 'phoneCode')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelCity
        fields = ('id', 'nameKg', 'nameEn', 'nameRu', 'country', 'code')


class CitySerializerGet(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = models.ModelCity
        fields = ('id', 'nameKg', 'nameEn', 'nameRu', 'country', 'code')


class PackageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelPackageType
        fields = ('id', 'nameKg', 'nameEn', 'nameRu', 'icon')


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelNotification
        fields = ('id', 'title', 'date', 'text', 'photo', 'read')


class CostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelCosts
        fields = ('id', 'fromCity', 'toCity', 'costPerKg', 'costPerKgMy', 'costPerVW')


class CostsSerializerGet(serializers.ModelSerializer):
    fromCity = CitySerializerGet()
    toCity = CitySerializerGet()

    class Meta:
        model = models.ModelCosts
        fields = ('id', 'fromCity', 'toCity', 'costPerKg', 'costPerKgMy', 'costPerVW')


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelTariff
        fields = ('id', 'nameKg', 'nameEn', 'nameRu', 'icon', 'extraCost')


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelCurrency
        fields = ('id', 'currency', 'oneGBIn', 'icon')


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelWebsite
        fields = ('id', 'name', 'icon', 'link')


class StoreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StoreCategory
        fields = ('id', 'nameEn', 'nameRus', 'nameKg', 'icon', 'priority')


# class CategorySerializerGet(serializers.ModelSerializer):
#     icon = serializers.SerializerMethodField(allow_null=True, )
#     # store = StoreSerializerOpen(many=True, required=False, allow_null=True)
#
#     class Meta:
#         model = models.Category
#         fields = ('id', 'nameEn', 'nameRus', 'nameKg', 'icon', 'priority', 'isoptovik', 'store')
#
#     def get_icon(self, category):
#         request = self.context.get('request')
#         if request is not None:
#             try:
#                 icon = category.icon.url
#                 return request.build_absolute_uri(icon)
#             except:
#                 return ""
#         return category.icon


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'nameEn', 'nameRus', 'nameKg', 'icon', 'priority', 'isoptovik', 'store')


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubCategory
        fields = ('id', 'nameEn', 'nameRus', 'nameKg', 'category')


class FranchiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelFranchiseRequest
        fields = ('id', 'name', 'email', 'phone', 'archive')


class BusinessRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelGbBusinessRequest
        fields = ('id', 'name', 'email', 'phone', 'info', 'file', 'archive')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelFile
        fields = ('id', 'title', 'file')


class ExtraServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelExtraService
        fields = ('id', 'nameRu', 'nameEn', 'nameKg', 'icon', 'infoRu', 'infoEn', 'infoKg', 'cost')


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelColor
        fields = ('id', 'nameRu', 'nameEn', 'nameKg', 'color', 'image')


class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelMemory
        fields = ('id', 'ram', 'storage', 'addCost')


class CurrencyFromUsdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelCurrencyFromUsd
        fields = ('id', 'som', 'rub', 'tenge', 'euro', 'sum', 'yuan')
