#from rest_framework import generics

from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer

'''
Sin utilizar el GeneralListAPIView
class MeasureUnitListAPIView(generics.ListAPIView):
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return MeasureUnit.objects.filter(state = True)
'''

class MeasureUnitListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer

class IndicatorListAPIView(GeneralListAPIView):
    serializer_class = IndicatorSerializer
    
class CategoryProductListAPIView(GeneralListAPIView):
    serializer_class = CategoryProductSerializer
