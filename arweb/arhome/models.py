from django.db import models

# Email for only set up. 
# More models will need to be added after our template is completed.

class Email(models.Model):
    email = models.CharField(max_length=500)

class Password(models.Model):
    password = models.CharField(max_length=70)

class Videos(models.Model):
    videoID = models.SmallIntegerField()
    title = models.CharField(max_length=250)
    timestamp = models.DateTimeField()
    
class Member(models.Model):
    phone = models.BigIntegerField()
    memberID = models.UUIDField(null=True)
    name = models.CharField(max_length=200)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    password = models.ForeignKey(Password, on_delete=models.CASCADE)
    videos_subscribe = models.ManyToManyField(Videos,symmetrical=False)
