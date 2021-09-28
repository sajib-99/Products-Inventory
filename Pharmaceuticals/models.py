from django.db import models
from django.template.defaultfilters import slugify
from django.utils.html import mark_safe

# Create your models here.
class MedicineType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Medicine Name")
    img = models.ImageField(upload_to='Product_Type_Images/')
    url= models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.url= slugify(self.name)
        super(MedicineType, self).save(*args, **kwargs) 
       
    def __str__(self):
          return self.name

    class Meta:
        db_table = 'MedicineType'
        # Add verbose name
        verbose_name = 'Medicine Type'

class pBrands(models.Model):
    Type = models.ForeignKey(MedicineType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Brand Name")
    img = models.ImageField(upload_to='Medicine/BrandName_Images/')
    url= models.SlugField(max_length=255, unique=True, blank=True)

    def image(self):
        return mark_safe('<img src="%s" width="50"  />' % (self.img.url))

    def __str__(self):
          return self.name + ' / ' + self.Type.name
          
    class Meta:
        db_table = 'pBrands'
        # Add verbose name
        verbose_name = 'Brand'

class medicine(models.Model):
    Type = models.ForeignKey(MedicineType, on_delete=models.CASCADE)
    brand = models.ForeignKey(pBrands, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Medicines")
    
   
    def __str__(self):
          return self.brand.name

    class Meta:
        db_table = 'medicine'
        # Add verbose name
        verbose_name = 'Medicine'
