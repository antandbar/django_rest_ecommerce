from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

#from apps.base.api import GeneralListAPIView
from apps.users.authentication_mixins import Authentication
from apps.products.api.serializers.product_serializers import ProductSerializer
from apps.base.utils import validate_files

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    # Se define simpletoken de manera específica
    #permission_classes = (IsAuthenticated,)

    queryset = ProductSerializer.Meta.model.objects.filter(state=True)

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state = True).first()
        
    def list(self,request):
        product_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(product_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        data = validate_files(request.data, 'image')
        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': ' Producto creado correctamente!'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            data = validate_files(request.data, "image", True)
            product_serializer = self.serializer_class(self.get_queryset(pk),data = data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,status = status.HTTP_200_OK)
            return Response(product_serializer.errors, status = status.HTTP_400_BAD_REQUEST)   

    # Se sobreescribre el método delete para hacer un borrado lógico 
    def destroy(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Producto con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)
