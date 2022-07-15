from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="users")
    profile_pic=models.ImageField(upload_to="profilepic",null=True)
    bio=models.CharField(max_length=160)
    option=(
        ("male","male"),
        ("female","female"),
        ("others","others")
    )

    gender=models.CharField(max_length=15,choices=option,default="male")
    DOB=models.DateField(null=True)

class Blogs(models.Model):
    image=models.ImageField(upload_to="blogimage",null=True)
    tile=models.CharField(max_length=160)
    description=models.CharField(max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="authors")
    posted_date=models.DateTimeField(auto_now_add=True)
    liked_by=models.ManyToManyField(User)

    def __str__(self):
        return self.tile

class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog=models.ForeignKey(Blogs,on_delete=models.CASCADE)
    comments=models.CharField(max_length=160)

    def __str__(self):
        return self.comments

