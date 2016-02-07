from django.db import models
from django.contrib.auth.models import User
class Post (models.Model):

    POST_TYPE = (
        ('R', 'Regular'),
        ('V', 'Special'),
    )
    POST_AREA = (
        (1, 'Walking'),
        (2, 'Running'),
        (3, 'Teninis'),
        (4, 'Swimming'),
        (5, 'Personal Coach'),
        (6, 'Bicycle'),
    )
    #post_id = models.IntegerField(max_length=11, primary_key=True)
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    post_type = models.CharField(max_length=1, choices=POST_TYPE)
    post_area = models.IntegerField(max_length=1, choices=POST_AREA)
    post_title = models.CharField(max_length=50)
    post_desc = models.CharField(max_length=1000)
    post_date = models.DateField(auto_now_add=True)
    #user_pic =
    def __unicode__(self):
        return self.post_id