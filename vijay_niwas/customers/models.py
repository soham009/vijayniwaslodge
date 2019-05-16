from django.db import models
from django_countries.fields import CountryField
import datetime
# Create your models here.
class passengers(models.Model):
    name = models.CharField(max_length=344)
    Address = models.CharField(max_length=50,default="")
    Gender = models.CharField(max_length=50,default="")
    Age = models.CharField(max_length=50,default="")
    Identity_Proof = models.CharField(max_length=50,default="")
    Identity_Proof_No = models.CharField(max_length=50,default="")
    mobile= models.CharField(max_length=264,default="")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Customer List for Police Record"
        verbose_name = "New Customers"
class NewEntry(models.Model):

    def number():
        no = NewEntry.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    MULTIPLICITY = (
        ("11", "11"),
        ("12", "12"),
        ("13", "13"),
        ("14", "14"),
        ("15", "15"),
        ("21", "21"),
        ("22", "22"),
        ("23", "23"),
        ("24", "24"),
        ("25", "25"),
        ("26", "26"),
        ("27", "27"),
        ("28", "28"),
        ("29", "29"),

    )
    
    PROOF = (
        ("aadhar card", "aadhar card"),
        ("pan card", "pan card"),
        ("driving license", "driving license"),
        ("passbook", "passbook"),
        ("insurance", "insurance"),

    )
    STAT = (
        ("PAID", "PAID"),
        ("UNPAID", "UNPAID"),

    )

    Entry_No = models.IntegerField( unique=True, default=number)
    bill_date = models.DateField()
    Name_of_Visitor = models.CharField(max_length=50)
    No_of_visitors = models.CharField(max_length=50)
    Age = models.CharField(max_length=50)
    Citizenship = CountryField()
    Address = models.TextField()
    Arrived_from = models.CharField(max_length=50)
    Departure_to = models.CharField(max_length=50)
    Identity_Proof = models.CharField(max_length=50, choices= PROOF,)
    Identity_Proof_No = models.CharField(max_length=50)
    Purpose_of_Visit = models.CharField(max_length=50)
    Occupation = models.CharField(max_length=50)
    check_in = models.DateTimeField(default=datetime.datetime.now)
    Room_No = models.CharField(max_length=264,choices=MULTIPLICITY,default="")
    Total_Amount= models.CharField(max_length=50)
    Advance = models.CharField(max_length=50)
    Remark = models.CharField(max_length=50, blank=True)
    Date_of_bill = models.DateTimeField(auto_now=True)
    Details_of_Other_Visitors = models.ManyToManyField(passengers)
    Payment_Status = models.CharField(max_length= 264,choices=STAT,default = "" )
    images = models.FileField(blank=True)
    check_out = models.DateTimeField(default=datetime.datetime.now)
 
    def __str__(self):
        return self.Name_of_Visitor

    class Meta:
        verbose_name_plural = "Fill Form For New Entry"
        verbose_name = "Customers"