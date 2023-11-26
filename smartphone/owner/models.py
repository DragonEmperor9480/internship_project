from django.db import models

# Create your models here.
class shop_details(models.Model):
    shop_id=models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    owner_name = models.CharField(max_length=20)
    shop_address = models.CharField(max_length=50)
    land_mark = models.CharField(max_length=30)
    Contact_no = models.CharField(max_length=20)

class mobile_details(models.Model):
    brand_name=models.CharField(max_length=20)
    mobile_name = models.CharField(max_length=20)
    owner_name = models.CharField(max_length=20)
    series = models.CharField(max_length=50)
    features = models.CharField(max_length=30)
    cost = models.CharField(max_length=20)
    photo = models.CharField(max_length=30)
    serial_no = models.CharField(max_length=20)

class customer_details(models.Model):
    customer_name=models.CharField(max_length=20)
    email_id = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=50)
    aadhar_no = models.CharField(max_length=30)

class sale_details(models.Model):
    customer_name=models.CharField(max_length=20)
    sales_id = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=50)
    serial_no = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    offers = models.CharField(max_length=30)
    payment_method = models.CharField(max_length=30)

class offers(models.Model):
    brand_name=models.CharField(max_length=20)
    mobile_name = models.CharField(max_length=20)
    offer_details = models.CharField(max_length=20)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=30)

class finance_details(models.Model):
    finance_name=models.CharField(max_length=20)
    rate_of_interest=models.CharField(max_length=20)
    details = models.CharField(max_length=20)
    documents_req = models.CharField(max_length=20)
    min_amt = models.CharField(max_length=50)
    max_amt = models.CharField(max_length=30)
    duration = models.CharField(max_length=30)

class billing(models.Model):
    shop_id=models.CharField(max_length=20)
    customer_name = models.CharField(max_length=20)
    mobile_name = models.CharField(max_length=20)
    serial_no = models.CharField(max_length=50)
    offer = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    total_amt = models.CharField(max_length=30)


