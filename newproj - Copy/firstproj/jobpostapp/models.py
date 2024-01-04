from django.db import models
from django.urls import reverse
from firstapp.models import User

# Create your models here.

class job_posts(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    salary = models.IntegerField()
    Type = models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)
    Experiance = models.IntegerField()
    Description = models.TextField(max_length=1800)
    Roles_Responsibiletes = models.TextField(max_length=700)


    def __str__(self) :
        return self.title

    def get_absolute_url(self):
        return reverse('job_details',kwargs={'pk':self.pk})
    
class job(models.Model):
    jobtitle = models.ForeignKey(job_posts,related_name='jobposts',on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Phone_num = models.BigIntegerField()

    # def __str__(self):
    #     return self.First_Name

class add_job(models.Model):
    Author_name = models.CharField(max_length=200)
    Post_type = models.CharField(max_length=200)
    Post_title = models.CharField(max_length=100)
    Sub_title = models.CharField(max_length=200,blank=True)
    Description = models.TextField(max_length=500)
    img = models.ImageField(upload_to='userimg/',blank=True)
    Time = models.TimeField(auto_now_add=True)
    view_count = models.IntegerField(blank=True,null=True)
    likes = models.ManyToManyField(User,related_name='post_likes',blank=True)
    bookmarks=models.ManyToManyField(User,related_name='bookmarks',blank=True)
     
    # def __str__(self):
    #     return self.Author_name
    def no_of_likes(self):
        return self.likes.count()


class comment(models.Model):
    content = models.TextField(max_length=2000)
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    post = models.ForeignKey(add_job,related_name='add_jobs',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name="replies")

    def __str__(self):
        return self.name
    
class subscribe(models.Model):
    Email = models.EmailField()
    Date= models.DateField(auto_now_add=True)



    
    



