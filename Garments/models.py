from django.db import models
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

# Create your models here.
class GarmentsProductType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Product Name")
    img = models.ImageField(upload_to='Product_Type_Images/')
    url= models.SlugField(max_length=255, unique=True, blank=True)

    def image(self):
        return mark_safe('<img src="%s" width="50"  />' % (self.img.url))
    def save(self, *args, **kwargs):
        self.url= slugify(self.name)
        super(GarmentsProductType, self).save(*args, **kwargs)    
        
    def __str__(self):
          return self.name
          
class BrandsName(models.Model):
    Type = models.ForeignKey(GarmentsProductType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Brand Name")
    img = models.ImageField(upload_to='BrandsName_Images/')
    url= models.SlugField(max_length=255, unique=True, blank=True)

    def image(self):
        return mark_safe('<img src="%s" width="50"  />' % (self.img.url))

    def __str__(self):
          return self.name + ' / ' + self.Type.name
          
    class Meta:
        db_table = 'BrandsName'
        # Add verbose name
        verbose_name = 'Brand'


class ProductDetail(models.Model):
    Type = models.ForeignKey(GarmentsProductType, on_delete=models.CASCADE)
    brand = models.ForeignKey(BrandsName, on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True)
    img = models.ImageField(upload_to='Garments/Products/')
    img2 = models.ImageField(upload_to='Garments/Products/')
    img3 = models.ImageField(upload_to='Garments/Products/') 

    def image(self):
        return mark_safe('<img src="%s" width="50"  />' % (self.img.url))
   
    def __str__(self):
          return self.brand.name

    class Meta:
        db_table = 'ProductDetail'
        # Add verbose name
        verbose_name = 'Product Detail'

