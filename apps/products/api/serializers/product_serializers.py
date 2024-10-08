from rest_framework import serializers

from apps.products.models import Product
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer


class ProductSerializer(serializers.ModelSerializer):
    """ 
    Devuelve un objeto con los id y nombre
    measure_unit = MeasureUnitSerializer()
    category_product = CategoryProductSerializer()
    """
    """
    Devuelve el str del model
    measure_unit = serializers.StringRelatedField()
    category_product = serializers.StringRelatedField()
    """

    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'description': instance.description,
            'image': instance.image.url if instance.image and hasattr(instance.image, 'url') else '',
            'measure_unit': instance.measure_unit.description,
            'category_product': instance.category_product.description
        }