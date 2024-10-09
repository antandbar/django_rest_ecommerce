from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

#from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.product_serializers import ProductSerializer

"""
Se usa solo para listar
class ProductListAPIView(GeneralListAPIView):
    serializer_class = ProductSerializer
"""
class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.filter(state=True)

    # No es necesio sobreescribir el método al heredar de CreateAPIView
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': ' Producto creado correctamente!'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return super().get_serializer().Meta.model.objects.filter(state = True)
        else:
            return super().get_serializer().Meta.model.objects.filter(id=pk, state = True).first()

    
    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Producto con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,status = status.HTTP_200_OK)
            return Response(product_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # Se sobreescribre el método delete para hacer un borrado lógico 
    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Producto con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)
    
"""    
class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return super().get_serializer().Meta.model.objects.filter(state = True)
    
    # Se sobreescribre el método delete para hacer un borrado lógico 
    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Producto con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)
"""

"""
class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, pk):
        return super().get_serializer().Meta.model.objects.filter(state = True).filter(id = pk).first()
    
    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Producto con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,status = status.HTTP_200_OK)
            return Response(product_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    """