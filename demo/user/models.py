from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile_no = models.IntegerField()

    def __str__(self):
        return self.first_name


class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,)
    profile_number = models.IntegerField(default=123)
    #profile_number = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile_number
