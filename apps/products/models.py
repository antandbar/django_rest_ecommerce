from django.db import models

from apps.base.models import BaseModel

class MeasureUnit(BaseModel):
    description = models.CharField('Descripción', max_length=50, blank=False, null=False, unique=True)
    
    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medida'

    def __str__(self):
        return self.description
    
class CategoryProduct(BaseModel):
    description = models.CharField('Description', max_length=50, unique=True, null=False, blank=False)
    
    class Meta:
        verbose_name = 'Categoría de Producto'
        verbose_name_plural = 'Categorías de Productos'

    def __str__(self):
        return self.description
    
class Indicator(BaseModel):

    descount_value = models.PositiveBigIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de Oferta')


    class Meta:
        verbose_name = "Indicador de Oferta"
        verbose_name_plural = "Indicadores de Ofertas"

    def __str__(self):
        return f'Oferta de la categoria {self.category_product} : {self.descount_value}%'

class Product(BaseModel):

    name = models.CharField('Nombre de Producto', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Descripción de Product', blank=False, null=False)
    image = models.ImageField('Imagen del Producto', upload_to='product/', blank=True, null=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medida', null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoría de Producto', null=True)


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name
    
    @property
    def stock(self):
        from django.db.models import Sum
        from apps.expense_manager.models import Expense

        expenses = Expense.objects.filter(
            product=self,
            state=True
        ).aggregate(Sum('quantity'))

        return expenses

 
