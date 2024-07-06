import datetime
import requests

from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions, status, pagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication

from core import models, serializers, filters

from PIL import Image
from io import BytesIO


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10


class DepotViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelDepots.objects.all()
    serializer_class = serializers.DepotSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = filters.DepotFilter
    search_fields = ('nameKg', 'nameRu', 'nameEn', 'address')
    # pagination_class = CustomPagination
    # ordering_fields = ('active', )

    # def get_queryset(self):
    #     return self.queryset.order_by('-active')

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).order_by('-active', '-id')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.DepotSerializerGet
        else:
            return serializers.DepotSerializer


class PackageViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelPackage.objects.all()
    serializer_class = serializers.PackageSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = filters.PackageFilter
    search_fields = ('pid', 'orderNumber')

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.PackageSerializerGet
        else:
            return serializers.PackageSerializer


class AlaketViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelAlaket.objects.all()
    serializer_class = serializers.AlaketSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = filters.AlaketFilter
    search_fields = ('title', )

    def get_queryset(self):
        return self.queryset.order_by('-dateCreated')

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.AlaketSerializerGet
        else:
            return serializers.AlaketSerializer


class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelImage.objects.all()
    serializer_class = serializers.ImageSerializer


class SavePackageViewSet(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    @swagger_auto_schema(request_body=serializers.SavePackageSerializer())
    def post(self, request):
        package_id = request.data['package']
        package = models.ModelPackage.objects.filter(pk=package_id).first()
        if not package:
           return Response({'status': "error, package with this id does not exist!"})
        client = models.Client.objects.filter(pk=request.data['clients']).first()
        if not client:
            return Response({'status': 'error, client with this id does not exist!'})
        package.clients.add(client)
        return Response({'status': 'ok'})


class RequestViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelRequests.objects.all()
    serializer_class = serializers.RequestSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = filters.RequestFilter
    search_fields = ('client__fullname', 'fromCountry__nameRu', 'fromCity__nameRu')

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.RequestSerializerGet
        else:
            return serializers.RequestSerializer

    def get_queryset(self):
        return self.queryset.order_by('-dateCreated')


class AcceptedRequestViewSet(APIView):
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [JWTAuthentication]
    serializer_class = serializers.AcceptedRequestSerializer

    @swagger_auto_schema(request_body=serializers.AcceptedRequestSerializer())
    def post(self, request, format=None):
        serializer = serializers.AcceptedRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        req = models.ModelRequests.objects.filter(pk=serializer.validated_data['request_id']).first()
        if not req:
            raise ValidationError({'status': "error! Request with this id does not exists!"})
        req.archive = True
        req.save()
        import time
        orderNumber = f'{req.toCountry.code}{req.toCity.code}{round(time.time()*1000)}'
        package = models.ModelPackage.objects.create(client_id=req.client.id, senderCountry_id=req.fromCountry.id,
                                                     senderCity_id=req.fromCity.id, receiverCountry=req.toCountry,
                                                     receiverCity=req.toCity, dateSending=req.dateSending,
                                                     orderNumber=orderNumber, packageData=req.packageData,
                                                     comment=req.comment,
                                                     packageType=req.packageType, clientName=req.client.fullname,
                                                     senderName=req.client.fullname, senderPhone=req.phone,
                                                     receiverName=req.receiverName, receiverPhone=req.receiverPhone,
                                                     length=req.length, height=req.height, width=req.width)
        package.clients.add(req.client.id)
        package.save()
        return Response({'status': "success created!"})


class DepotUserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = models.DepotUser.objects.all()
    serializer_class = serializers.DepotUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PackageDataViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelPackageData.objects.all()
    serializer_class = serializers.PackageDataSerializer

    def get_queryset(self):
        return self.queryset.order_by('order')


class AddressesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelAddresses.objects.all()
    serializer_class = serializers.AddressesSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = filters.AddressesFilter

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.AddressesSerializerGet
        else:
            return serializers.AddressesSerializer


class BannersViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = models.BuyerBanners.objects.all()
    serializer_class = serializers.BannerSerializer
    pagination_class = None

    def get_queryset(self):
        return self.queryset.order_by('-order')


class BuyerRequestViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelBuyerRequest.objects.all()
    serializer_class = serializers.BuyerRequestSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = filters.BuyerRequestFilter

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.BuyerRequestSerializerGet
        else:
            return serializers.BuyerRequestSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        cart_requests = request.data.pop('cart_request', None)
        if cart_requests:
            cart_req_id = []
            for i in cart_requests:
                cart_req = models.CartRequest.objects.create(**i)
                cart_req_id.append(cart_req.id)

            instance.cart_request.set(cart_req_id)
            instance.save()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class ItemViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelItem.objects.all()
    serializer_class = serializers.ItemSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = filters.ItemFilter

    ordering_fields = ('cost', 'priority')
    search_fields = ('name',)

    def get_queryset(self):
        return self.queryset.order_by('-id')

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.ItemSerializerOpen
        else:
            return serializers.ItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelOrder.objects.all()
    serializer_class = serializers.OrderSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = filters.OrderFilter
    search_fields = ('storeName', )

    def get_queryset(self):
        return self.queryset.all().order_by("-id")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.OrderSerializerGet
        return serializers.OrderSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        items = request.data.pop("items", None)
        cart_items_id = []

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if items:
            for i in items:
                cart_item = models.CartItems.objects.create(item_id=i['item'], quantity=i['quantity'])
                cart_items_id.append(cart_item.id)
            instance.items.set(cart_items_id)
        instance.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class GetItemViewSet(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(responses={200: serializers.FiveItemSerializer()})
    def get(self, request, format=None):
        items = models.ModelItem.objects.all()
        categories = models.Category.objects.all()

        data = []
        for category in categories:
            data_items = items.filter(category=category)
            item_data = []
            count = 1
            for i in data_items:
                item_serializer = serializers.ItemSerializerOpen(instance=i, context={'request': request})
                item_data.append(item_serializer.data)
                if count > 5:
                    break
                else:
                    count += 1
            category_serializer = serializers.CategorySerializer(instance=category, context={'request': request})
            loc_data = {
                'category': category_serializer.data,
                'items': item_data
            }
            data.append(loc_data)
        return Response({'data': data})


class ItemByIDViewSet(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(request_body=serializers.GetItemByIDSerializer())
    def post(self, request, format=None):
        serializer = serializers.GetItemByIDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        items_id = serializer.validated_data['items_id']
        data = []
        for i in items_id:
            item = models.ModelItem.objects.filter(pk=i)
            if item is not None:
                item_serializer = serializers.ItemSerializerOpen(item.first(), context={'request': request})
                data.append(item_serializer.data)

        return Response({'data': data})


class ItemSearchRequestViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.ModelItemSearchRequest.objects.all()
    serializer_class = serializers.ItemSearchRequestSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = filters.ItemSearchFilter

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.ItemSearchRequestSerializerGet
        else:
            return serializers.ItemSearchRequestSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        wanted_items = request.data.pop('wantedItems', None)
        wan_items_id = []
        for i in wanted_items:
            wan_item = models.WantedItems.objects.create(**i)
            wan_items_id.append(wan_item.id)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance.wantedItems.set(wan_items_id)
        instance.save()
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class SetPhotoAndSizeViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        items = models.ModelItem.objects.all().filter(supplier_id=40)
        for i in items:
            i.country_id = 19
            i.city_id = 6
            i.save()

        return Response({"message": "success"})


class SetSizeViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = serializers.SetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        items = models.ModelItem.objects.filter(category_id=5)
        sizes = [
            '6/39', '6,5/39', '7/40', '7,5/40-41', '8/41', '8,5/41-42', '9/42', '9,5/42-43', '10/43', '10,5/43-44',
            '11/44', '11,5/44-45', '12/45', '13/46', '14/47', '15/48', '16/49'
        ]
        for item in items:
            item.sizes = sizes
            item.save()

        return Response({'message': 'success'}, status=status.HTTP_200_OK)
