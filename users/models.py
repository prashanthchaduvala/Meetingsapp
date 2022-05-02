from django.db import models

# Create your models here.

class UserProfile(models.Model):
    email = models.EmailField(verbose_name="email", max_length=60,unique=True,null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    user_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return str(self.user) + ': ' + str(self.login_time)
