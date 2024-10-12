#from rest_framework import generics
from rest_framework import status
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
    
    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'],state = True)
    
    def list(self, request):
        """
        Retorna todas las unidades de medidas diponibles

        
        params.
        name ----> nombre de la unidad de medida
        """
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)
    
    def retrieve(self, request, pk=None):
        """
        Retorna una categoría específica por su ID.
        """
        obj = self.get_object().get()
        if obj:
            serializer = self.serializer_class(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'Categoría no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request):
        serrializer = self.serializer_class(data=request.data)
        if serrializer.is_valid():
            serrializer.save()
            return Response({'message': 'Categoría registrada correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'message':'','error':serrializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_object().exists():    
            serializer = self.serializer_class(isinstance=self.get_object().get(), data=request.data) 
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Categoría actualizada correctamente'}, status=status.HTTP_200_OK)
        return Response({'message':'','error':serrializer.errors},status=status.HTTP_400_BAD_REQUEST)       

    def destroy(self, request, pk=None):
        if self.get_object.exist():
            self.get_object().get().delete()
            return Response({'message': 'Categoría actualizada correctamente'}, status=status.HTTP_200_OK)
        return Response({'message':'','error':'Categoría no encontada'},status=status.HTTP_400_BAD_REQUEST)       


'''
class MeasureUnitListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer

class IndicatorListAPIView(GeneralListAPIView):
    serializer_class = IndicatorSerializer
    
class CategoryProductListAPIView(GeneralListAPIView):
    serializer_class = CategoryProductSerializer
'''