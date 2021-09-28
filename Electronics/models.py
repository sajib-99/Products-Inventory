from django.db import models
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify



# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Product Name")
    img = models.ImageField(upload_to='Product_Type_Images/')
    url= models.SlugField(max_length=255, unique=True, blank=True)

    def image(self):
        return mark_safe('<img src="%s" width="50"  />' % (self.img.url))
    def save(self, *args, **kwargs):
        self.url= slugify(self.name)
        super(ProductType, self).save(*args, **kwargs)    
        
    def __str__(self):
          return self.name
          
class Brands(models.Model):
    Type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Brand Name")
    img = models.ImageField(upload_to='Brands_Images/')
    url= models.SlugField(max_length=255, unique=True, blank=True)

    def image(self):
        return mark_safe('<img src="%s" width="50"  />' % (self.img.url))

    def __str__(self):
          return self.name + ' / ' + self.Type.name
          
    class Meta:
        db_table = 'Brands'
        # Add verbose name
        verbose_name = 'Brand'

class ModelNo(models.Model):
    Type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Model Name")
    
    uid= models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.uid= slugify(self.name)
        super(ModelNo, self).save(*args, **kwargs)   
    
    def __str__(self):
          return self.name

class ProductDetails(models.Model):
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    ModelNo = models.ForeignKey(ModelNo, on_delete=models.CASCADE, verbose_name="Model No")
    description = RichTextField(blank=True, null=True)
    img = models.ImageField(upload_to='Electronic/Products/')
    img2 = models.ImageField(upload_to='Electronic/Products/')
    img3 = models.ImageField(upload_to='Electronic/Products/') 

    def image(self):
        return mark_safe('<img src="%s" width="50"  />' % (self.img.url))
   
    def __str__(self):
          return self.ModelNo.name

    class Meta:
        db_table = 'ProductDetails'
        # Add verbose name
        verbose_name = 'Product Detail'

