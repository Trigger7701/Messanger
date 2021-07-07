from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
class Profiles(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    def __str__(self):
        return 'Profile: ' + self.user.username
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''
class Chats(models.Model):
    user1 = models.ForeignKey(Profiles,related_name='sender',on_delete=models.SET_NULL,null=True)
    user2 = models.ForeignKey(Profiles,related_name='reciver',on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return 'Chat: '+self.user1.user.username+' and '+self.user2.user.username
class Messages(models.Model):
    chat = models.ForeignKey(Chats,on_delete=models.CASCADE)
    sender =models.ForeignKey(Profiles,on_delete=models.SET_NULL,null=True)
    text = models.CharField(max_length=2000,default='')
    time = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.sender.user.username + ': '+ self.text
    @property
    def mtime(self):
        return self.time.strftime('%H:%M')
    description = models.CharField(max_length=200,null=True)



