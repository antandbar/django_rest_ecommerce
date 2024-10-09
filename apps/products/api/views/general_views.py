#from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response

from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer
from apps.products.models import MeasureUnit

'''
Sin utilizar el GeneralListAPIView
class MeasureUnitListAPIView(generics.ListAPIView):
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return MeasureUnit.objects.filter(state = True)
'''
class MeasureUnitViewSet(viewsets.GenericViewSet):
    """
    Hola desde unidad de medida
    """
    model = MeasureUnit
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def list(self, request):
        """
        Retorna todas las unidades de medidas diponibles

        
        params.
        name ----> nombre de la unidad de medida
        """
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)

class IndicatorViewSet(viewsets.GenericViewSet):
    serializer_class = IndicatorSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def list(self, request):
        """
        Retorna todas las unidades de medidas diponibles

        
        params.
        name ----> nombre de la unidad de medida
        """
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)
    
class CategoryProductViewSet(viewsets.GenericViewSet):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def list(self, request):
        """
        Retorna todas las unidades de medidas diponibles

        
        params.
        name ----> nombre de la unidad de medida
        """
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)

'''
class MeasureUnitListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer

class IndicatorListAPIView(GeneralListAPIView):
    serializer_class = IndicatorSerializer
    
class CategoryProductListAPIView(GeneralListAPIView):
    serializer_class = CategoryProductSerializer
'''