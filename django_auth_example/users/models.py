from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)

    class Meta(AbstractUser.Meta):
        pass


# class MYBOOK(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.FloatField()
#
#     def __str__(self):
#         return self.name+':'+str(self.price)

# class Resulttable(models.Model):
#     # movieId = models.IntegerField(null=True)  # Field name made lowercase.
#     userId = models.IntegerField(null=True)  # Field name made lowercase.
#     rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
#     imdbId = models.IntegerField()  # Field name made lowercase.
#     title = models.CharField(max_length=50, blank=True, null=True)
#
#     # class Meta:
#     #     managed = False
#     #     db_table = 'resulttable'
#
#     def __str__(self):
#         return self.userId+':'+self.rating


class Resulttable(models.Model):
    # movieId = models.IntegerField(null=True)  # Field name made lowercase.
    userId = models.IntegerField(null=True)  # Field name made lowercase.
    imdbId = models.IntegerField()  # Field name made lowercase.
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    # title = models.CharField(max_length=50, blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'resulttable'

    def __str__(self):
        return self.userId+':'+self.rating


class Insertposter(models.Model):
    userId = models.IntegerField(null=True)
    title = models.CharField(max_length=200,blank=True,null = False)
    poster = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.userId + ':' + self.poster

