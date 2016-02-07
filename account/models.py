from django.db import models
from django.conf import settings

class Profile (models.Model):

    USER_TYPE = (
        ('R', 'Regular'),
        ('V', 'Special'),
    )
    GENDER = (
        ('M' , 'MALE'),
        ('F' , 'FEMALE'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_type = models.CharField(max_length=1, choices=USER_TYPE)
    gender = models.CharField(max_length=1, choices=GENDER)
    #country
    #city
    #תתתregistration_date  = models.DateField()
    user_email = models.EmailField()
    user_facebook = models.CharField(max_length=70,null=True)
    user_twitter  = models.CharField(max_length=70,null=True)
    #user_pic =
    def __unicode__(self):
        return self.user_email