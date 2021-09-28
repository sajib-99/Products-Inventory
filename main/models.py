from django.db import models
from django.utils.html import mark_safe
# Create your models here.



class partner(models.Model):
    name = models.CharField(max_length=255, verbose_name="Partners Name")
    img = models.ImageField(upload_to='Product_Type_Images/')
    
    def image(self):
        return mark_safe('<img src="%s" width="50"  />' % (self.img.url))

    def __str__(self):
          return self.name

class Quote(models.Model):
    name = models.CharField(max_length=100)
    companyname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    country = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    quotes = models.TextField()
    
    def __str__(self):
          return "Quote from: " + self.name

class Career(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    city = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    message = models.TextField()
    cv = models.FileField(upload_to='cv/')

    
    def __str__(self):
          return "Candidate: " + self.firstname + self.lastname

class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    companyname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    message = models.TextField()
    
    def __str__(self):
          return "Message from: " + self.firstname

class ClientOwnerForm(models.Model):
    ownerName = models.CharField(max_length=100)
    ownerCompanyname = models.CharField(max_length=100)
    ownerDesignation = models.CharField(max_length=100)
    ownerBusinessLocation = models.CharField(max_length=100)
    ownerBusinessType = models.CharField(max_length=11)
    ownerAddress = models.CharField(max_length=100)
    ownerCity = models.CharField(max_length=100)
    ownerState = models.CharField(max_length=100)
    ownerZip = models.IntegerField()
    ownerEmail = models.CharField(max_length=100)
    ownerPhone = models.CharField(max_length=100)
    ownerFax = models.CharField(max_length=100)
    ownerWebsite = models.CharField(max_length=100)
    ownerMessage = models.TextField()
    
    def __str__(self):
          return "Client Requirement Message from: " + self.ownerName

class EmployeeOwnerForm(models.Model):
    EmployeeName = models.CharField(max_length=100)
    EmployeeCompanyname = models.CharField(max_length=100)
    EmployeeDesignation = models.CharField(max_length=100)
    EmployeeBusinessLocation = models.CharField(max_length=100)
    EmployeeBusinessType = models.CharField(max_length=11)
    EmployeeAddress = models.CharField(max_length=100)
    EmployeeCity = models.CharField(max_length=100)
    EmployeeState = models.CharField(max_length=100)
    EmployeeZip = models.IntegerField()
    EmployeeEmail = models.CharField(max_length=100)
    EmployeePhone = models.CharField(max_length=100)
    EmployeeFax = models.CharField(max_length=100)
    EmployeeWebsite = models.CharField(max_length=100)
    OwnerName = models.CharField(max_length=100)
    OwnerDesignation = models.CharField(max_length=100)
    OwnerAddress = models.CharField(max_length=100)
    OwnerCity = models.CharField(max_length=100)
    OwnerState = models.CharField(max_length=100)
    OwnerZip = models.IntegerField()
    OwnerEmail = models.CharField(max_length=100)
    OwnerPhone = models.CharField(max_length=100)
    EmployeeMessage = models.TextField()
    
    def __str__(self):
          return "Client Requirement Message from: " + self.EmployeeName