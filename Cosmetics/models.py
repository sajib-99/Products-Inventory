from django.db import models
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

# Create your models here.
class CosmeticsProductType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Product Name")
    img = models.ImageField(upload_to='Cosmetics/Product_Type_Images/')
    url= models.SlugField(max_length=255, unique=True, blank=True)

    def image(self):
        return mark_safe('<img src="%s" width="50"  />' % (self.img.url))
    def save(self, *args, **kwargs):
        self.url= slugify(self.name)
        super(CosmeticsProductType, self).save(*args, **kwargs)    
        
    def __str__(self):
          return self.name
          
class BrandName(models.Model):
    Type = models.ForeignKey(CosmeticsProductType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Brand Name")
    img = models.ImageField(upload_to='Cosmetics/BrandName_Images/')
    url= models.SlugField(max_length=255, unique=True, blank=True)

    def image(self):
        return mark_safe('<img src="%s" width="50"  />' % (self.img.url))

    def __str__(self):
          return self.name + ' / ' + self.Type.name
          
    class Meta:
        db_table = 'BrandName'
        # Add verbose name
        verbose_name = 'Brand'


class ProductsDetail(models.Model):
    Type = models.ForeignKey(CosmeticsProductType, on_delete=models.CASCADE)
    brand = models.ForeignKey(BrandName, on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True)
    img = models.ImageField(upload_to='Cosmetics/Products/')
    img2 = models.ImageField(upload_to='Cosmetics/Products/')
    img3 = models.ImageField(upload_to='Cosmetics/Products/') 

    def image(self):
        return mark_safe('<img src="%s" width="50"  />' % (self.img.url))
   
    def __str__(self):
          return self.brand.name

    class Meta:
        db_table = 'ProductsDetail'
        # Add verbose name
        verbose_name = 'Product Detail'

