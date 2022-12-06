from django.db import models
from random import choices


# Create your models here.


STATUS = (
    ("SELLING", "Selling"),
    ("RENTING", "Renting")
)

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=1500,)
    price = models.FloatField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    image = models.ImageField(upload_to='static/myapp', blank=True, null=True)
    status = models.CharField(choices=STATUS, max_length=100)
    date_posted = models.DateField(auto_now= True)

    def __str__(self):
        return self.title



