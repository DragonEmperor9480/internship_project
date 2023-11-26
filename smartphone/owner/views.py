from django.shortcuts import render

# Create your views here.

def showindex(request):
    return render(request, "index.html")


def showcontact(request):
    return render(request, "contact.html")


def showlogin(request):
    return render(request, "login.html")


def showbilling(request):
    return render(request, "billing.html")


def showpayments(request):
    return render(request, "payments.html")


def shopdetails(request):
    return render(request, "shopdetails.html")


def showphones(request):
    return render(request, "phones.html")


def smartphonedetails(request):
    return render(request, "smartphonedetails.html")


def cuostmerdetails(request):
    return render(request, "cuostmerdetails.html")


def viewsmartphonedetails(request):
    return render(request, "viewsmartphonedetails.html")


def viewcuostmerdetails(request):
    return render(request, "viewcuostmerdetails.html")


def viewspd(request):
    return render(request, "viewspd.html")


def viewshopd(request):
    return render(request, "viewshopd.html")


def viewcustd(request):
    return render(request, "viewcustd.html")


def viewsaled(request):
    return render(request, "viewsaled.html")


def viewbilling(request):
    return render(request, "viewbilling.html")


def viewoffers(request):
    return render(request, "viewoffers.html")


def logcheck(request):
    return render(request, "customer_menu.html")


def insertowner(request):
    return render(request, "owner_menu.html")


def shop_details(request, b1=None, b2=None, b3=None, b6=None):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        shop_details.objects.create(shop_id=s1, name=s2, owner_name=s3, shop_address=s4, land_mark=s5, contact_no=s6)
        return render(request, "shopdetails.html")

    return render(request, "shopdetails.html")


def viewshop_details(request):
    shop_details.objects.all()
    return render(request, "viewshopd.html")


def insert_mobile_details(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")

        mobile_details.objects.create(brand_name=s1, mobile_name=s2, series=s3, features=s4, cost=s5, photo=s6,
                                      serial_no=s7)
        return render(request, "smartphone_details.html")

    return render(request, "smartphone_details.html")


def viewmobile_details(request):
    userdict=viewmobile_details.objects.all()
    return render(request, "viewspd.html",{"user_dict":userdict})


def customer_details(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")

        customer_details.objects.create(customer_name=s1, email_id=s2, address=s3, mobile_no=s4, aadhar_no=s5)
        return render(request, "cuostmerdetails.html")

    return render(request, "cuostmerdetails.html")


def viewcustomer_details(request):
    viewcustomer_details.objects.all()
    return render(request, "viewcustd.html")


def sales_details(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")

        sales_details.objects.create(customer_name=s1, sales_id=s2, mobile=s3, mobile_no=s4, serial_no=s5, date=s6,
                                     offers=s7, payment_method=s8)
        return render(request, "salesdetails.html")

    return render(request, "salesdetails.html")


def viewsales_details(request):
    viewsales_details.objects.all()
    return render(request, "viewsalesd.html")


def offers(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")

        offers.objects.create(brand_name=s1, mobile_name=s2, offer_details=s3, start_date=s4, end_date=s5)
        return render(request, "offers.html")

    return render(request, "offers.html")


def viewoffers(request):
    viewoffers.objects.all()
    return render(request, "viewoffers.html")


def billing(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")

        billing.objects.create(shop_id=s1, customer_name=s2, mobile_name=s3, serial_no=s4, offer=s5, date=s6,
                              total_amt=s7)
        return render(request, "billing.html")

    return render(request, "billing.html")


def viewbilling(request):
    viewbilling.objects.all()
    return render(request, "viewbilling.html")


def finance(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")

        finance.objects.create(finance_name=s1, rate_of_interest=s2, details=s3, documents_req=s4, min_amt=s5,
                              max_amt=s6, duration=s7)
        return render(request, "finance.html")

    return render(request, "finance.html")


def viewfinance(request):
    viewfinance().objects.all()
    return render(request, "viewfinance.html")
