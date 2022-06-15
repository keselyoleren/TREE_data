from os import replace
from rest_framework import (
    generics,
    serializers,
    viewsets,
    status,
    response,
    permissions
)
from app.models import Orang
from app.serializers.orang import OrangSerialize
from helper.pagination import ResponsePagination
from rest_framework.response import Response


from app.models import Orang

class OrangApiView(generics.ListAPIView,
            generics.RetrieveAPIView, 
            generics.CreateAPIView, 
            generics.UpdateAPIView, 
            generics.DestroyAPIView, 
            viewsets.ModelViewSet
        ):
    serializer_class = OrangSerialize
    queryset  = Orang.objects.all()
    pagination_class = ResponsePagination

    def _response(self, request, instance):
        page = self.paginate_queryset(instance)        
        serialize = self.get_paginated_response(
            self.serializer_class(page, many=True, context={"request":request}).data
        )
        response = serialize.data
        return Response(response)

    def list(self, request, *args, **kwargs):
        instance = self.queryset.filter(parent=None)
        for x in Orang.objects.filter(parent__id=1):
            queryset = Orang.objects.filter(parent__nama=x.nama)
            print(queryset.query)
        
        return self._response(request, instance)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)        

    def create(self, request, *args, **kwargs):
        serialize = self.serializer_class(data=request.data, context={"request":request})
        serialize.is_valid(raise_exception=True)
        self.perform_create(serialize)
        return Response(serialize.data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        x = generics.get_object_or_404(Orang, id=kwargs['pk']).delete()
        return Response({
            "message":"success"
        }, status=status.HTTP_200_OK)


        