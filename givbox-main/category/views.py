from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter

from category import models, serializers, filters
from user.serializers import CategorySerializerGet


class HourWorkViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelWH.objects.all()
    serializer_class = serializers.HourWorkSerializer


class ContactsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelContact.objects.all()
    serializer_class = serializers.ContactsSerializer


class CountryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = models.ModelCountry.objects.all()
    serializer_class = serializers.CountrySerializer
    pagination_class = None


class CityViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelCity.objects.all()
    serializer_class = serializers.CitySerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = filters.CityFilter
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.CitySerializerGet
        else:
            return serializers.CitySerializer


class PackageTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelPackageType.objects.all()
    serializer_class = serializers.PackageTypeSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelNotification.objects.all()
    serializer_class = serializers.NotificationSerializer


class CostsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelCosts.objects.all()
    serializer_class = serializers.CostsSerializer
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.CostsSerializerGet
        else:
            return serializers.CostsSerializer


class TariffViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelTariff.objects.all()
    serializer_class = serializers.TariffSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelCurrency.objects.all()
    serializer_class = serializers.CurrencySerializer


class WebsiteViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelWebsite.objects.all()
    serializer_class = serializers.WebsiteSerializer


class StoreCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.StoreCategory.objects.all()
    serializer_class = serializers.StoreCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializerGet

    ordering = ('id', 'priority')
    ordering_fields = ('id', 'priority')
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = filters.CategoryFilter
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CategorySerializerGet
        return serializers.CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.SubCategory.objects.all()
    serializer_class = serializers.SubCategorySerializer

    filter_backends = (DjangoFilterBackend,)
    filter_class = filters.SubCategoryFilter
    pagination_class = None


class FranchiseViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelFranchiseRequest.objects.all()
    serializer_class = serializers.FranchiseSerializer
    pagination_class = None


class BusinessRequestViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelGbBusinessRequest.objects.all()
    serializer_class = serializers.BusinessRequestSerializer
    pagination_class = None


class FileViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelFile.objects.all()
    serializer_class = serializers.FileSerializer
    pagination_class = None


class ExtraServiceViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelExtraService.objects.all()
    serializer_class = serializers.ExtraServiceSerializer


class ColorViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelColor.objects.all()
    serializer_class = serializers.ColorSerializer
    pagination_class = None


class MemoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelMemory.objects.all()
    serializer_class = serializers.MemorySerializer


class CurrencyFromUSDViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelCurrencyFromUsd.objects.all()
    serializer_class = serializers.CurrencyFromUsdSerializer
