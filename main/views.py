from django.shortcuts import render
from Electronics.models import ProductType
from Garments.models import GarmentsProductType
from Cosmetics.models import CosmeticsProductType
from DailyNeeds.models import DailyNeedsProductType
from Pharmaceuticals.models import MedicineType
from .models import partner, Quote, Contact, Career, ClientOwnerForm, EmployeeOwnerForm
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

# Create your views here.

#index
def index(request):
    if request.method=="POST":
        name=request.POST['name']
        companyname=request.POST['companyname']
        email=request.POST['email']
        phone=request.POST['phone']
        country=request.POST['country']
        product=request.POST['product']
        quotes =request.POST['quotes']
        

        if len(name)<2 or len(email)<5 or len(phone)<9 or len(product)<2 or len(quotes)<10:
            messages.error(request, "Please fill the form correctly")
        else:
            quote=Quote(name=name, companyname=companyname, email=email, phone=phone, quotes=quotes, country=country, product=product)
            quote.save()
            messages.success(request, "Your quote has been sent successfully")
    

    Electronicsitems= ProductType.objects.all()
    Garmentsitems= GarmentsProductType.objects.all()
    Cosmeticsitems= CosmeticsProductType.objects.all()
    DailyNeedsitems= DailyNeedsProductType.objects.all()
    Pharmaceuticals= MedicineType.objects.all()
    
   
    context= { 
        'Electronicsitems': Electronicsitems,
        'Garmentsitems' : Garmentsitems,
        'Cosmeticsitems' : Cosmeticsitems,
        'DailyNeedsitems' : DailyNeedsitems,
        'Pharmaceuticals': Pharmaceuticals,
        }
    
    return render(request, 'index.html',context) 

#about
def about(request):   
    return render(request, 'about.html',)

#mission
def mission(request):   
    return render(request, 'mission.html',)


#vision
def vision(request):   
    return render(request, 'vision.html',)


#career
def career(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        phone=request.POST['phone']
        city=request.POST['city']
        position=request.POST['position']
        message =request.POST['message']
        cv =request.FILES['cv']
        
        if len(firstname)<2 or len(lastname)<2 or len(email)<5 or len(phone)<9 or len(position)<2 or len(message)<10:
            messages.error(request, "Please fill the form correctly")
        else:
            career=Career(firstname=firstname, lastname=lastname, email=email, phone=phone, message=message, city=city, position=position, cv=cv)
            career.save()
            messages.success(request, "Your application has been submitted successfully")
          
    return render(request, 'career.html',)

#policy
def policy(request):   
    return render(request, 'PrivacyPolicy.html',)


#partners
def partners(request):
    partners = partner.objects.all()
    contex = {'partners': partners}

    return render(request, 'partners.html', contex)

#faq
def faq(request):   
    return render(request, 'faq.html',)

#clientform
def clientform(request):
    # owner form
    if request.method=="POST":
        if 'ownerform' in request.POST:
            ownerName = request.POST['ownerName']
            ownerCompanyname = request.POST['ownerCompanyname']
            ownerDesignation = request.POST['ownerDesignation']
            ownerBusinessLocation = request.POST['ownerBusinessLocation']
            ownerBusinessType = request.POST['ownerBusinessType']
            ownerAddress = request.POST['ownerAddress']
            ownerCity = request.POST['ownerCity']
            ownerState = request.POST['ownerState']
            ownerZip = request.POST['ownerZip']
            ownerEmail = request.POST['ownerEmail']
            ownerPhone =request.POST['ownerPhone']
            ownerFax = request.POST['ownerFax']
            ownerWebsite = request.POST['ownerWebsite']
            ownerMessage = request.POST['ownerMessage']

            if len(ownerName)<2 or len(ownerCompanyname)<2 or len(ownerEmail)<5 or len(ownerPhone)<9 or len(ownerAddress)<2 or len(ownerMessage)<10:
                messages.error(request, "Please fill the form correctly")
            else:
                clientform=ClientOwnerForm(ownerName=ownerName, ownerCompanyname=ownerCompanyname, ownerDesignation=ownerDesignation, ownerBusinessLocation=ownerBusinessLocation, ownerBusinessType=ownerBusinessType, ownerAddress=ownerAddress, ownerCity=ownerCity, ownerState=ownerState, ownerZip=ownerZip, ownerEmail=ownerEmail, ownerPhone=ownerPhone, ownerFax=ownerFax, ownerWebsite=ownerWebsite, ownerMessage=ownerMessage)
                clientform.save()
                messages.success(request, "Your message has been sent successfully")    

    # employee form
        elif 'employeeform' in request.POST:
            EmployeeName = request.POST['EmployeeName']
            EmployeeCompanyname = request.POST['EmployeeCompanyname']
            EmployeeDesignation = request.POST['EmployeeDesignation']
            EmployeeBusinessLocation = request.POST['EmployeeBusinessLocation']
            EmployeeBusinessType = request.POST['EmployeeBusinessType']
            EmployeeAddress = request.POST['EmployeeAddress']
            EmployeeCity = request.POST['EmployeeCity']
            EmployeeState = request.POST['EmployeeState']
            EmployeeZip = request.POST['EmployeeZip']
            EmployeeEmail = request.POST['EmployeeEmail']
            EmployeePhone =request.POST['EmployeePhone']
            EmployeeFax = request.POST['EmployeeFax']
            EmployeeWebsite = request.POST['EmployeeWebsite']

            OwnerName = request.POST['OwnerName']
            OwnerDesignation = request.POST['OwnerDesignation']
            OwnerAddress = request.POST['OwnerAddress']
            OwnerCity = request.POST['OwnerCity']
            OwnerState = request.POST['OwnerState']
            OwnerZip = request.POST['OwnerZip']
            OwnerEmail = request.POST['OwnerEmail']
            OwnerPhone =request.POST['OwnerPhone']

            EmployeeMessage = request.POST['EmployeeMessage']

            if len(EmployeeName)<2 or len(EmployeeCompanyname)<2 or len(EmployeeEmail)<5 or len(EmployeePhone)<9 or len(EmployeeAddress)<2 or len(EmployeeMessage)<10:
                messages.error(request, "Please fill the form correctly")
            else:
                employeeform=EmployeeOwnerForm(EmployeeName=EmployeeName, EmployeeCompanyname=EmployeeCompanyname, EmployeeDesignation=EmployeeDesignation, EmployeeBusinessLocation=EmployeeBusinessLocation, EmployeeBusinessType=EmployeeBusinessType, EmployeeAddress=EmployeeAddress, EmployeeCity=EmployeeCity, EmployeeState=EmployeeState, EmployeeZip=EmployeeZip, EmployeeEmail=EmployeeEmail, EmployeePhone=EmployeePhone, EmployeeFax=EmployeeFax, EmployeeWebsite=EmployeeWebsite, EmployeeMessage=EmployeeMessage, 
                OwnerName=OwnerName, OwnerDesignation=OwnerDesignation, OwnerAddress=OwnerAddress, OwnerCity=OwnerCity, OwnerState=OwnerState, OwnerZip=OwnerZip, OwnerEmail=OwnerEmail, OwnerPhone=OwnerPhone)
                employeeform.save()
                messages.success(request, "Your message has been sent successfully")        
        

    return render(request, 'clientform.html',)

#contact
def contact(request):
    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        companyname = request.POST['companyname']
        email = request.POST['email']
        phoneno = request.POST['phoneno']
        address = request.POST['address']
        address2 = request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        message = request.POST['message']
        if len(firstname)<2 or len(lastname)<2 or len(email)<5 or len(phoneno)<9 or len(address)<2 or len(message)<10:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(firstname=firstname, lastname=lastname, companyname=companyname, email=email, phoneno=phoneno, city=city, state=state, zipcode=zipcode, address=address, address2=address2, message=message)
            contact.save()
            messages.success(request, "Your message has been sent successfully")

    return render(request, 'contact.html',)

#quote
def quote(request):   
    if request.method=="POST":
        name=request.POST['name']
        companyname=request.POST['companyname']
        email=request.POST['email']
        phone=request.POST['phone']
        country=request.POST['country']
        product=request.POST['product']
        quotes =request.POST['quotes']
        

        if len(name)<2 or len(email)<5 or len(phone)<9 or len(product)<2 or len(quotes)<10:
            messages.error(request, "Please fill the form correctly")
        else:
            quote=Quote(name=name, companyname=companyname, email=email, phone=phone, quotes=quotes, country=country, product=product)
            quote.save()
            messages.success(request, "Your quote has been sent successfully")
    return render(request, 'quote.html',)