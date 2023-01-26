from django.db import models


# Create your models here.
class Gender(models.Model):
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.gender


class Course(models.Model):

    
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name 


class Batch(models.Model):
    
    Batch_name = models.CharField(max_length=30)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.Batch_name

class userdetails(models.Model):
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Gender = models.ForeignKey(Gender,on_delete=models.CASCADE,null=True)
    Email = models.EmailField()
    Phone = models.IntegerField()
    Course = models.ForeignKey(Course,on_delete=models.CASCADE)
    Batch = models.ForeignKey(Batch,on_delete=models.CASCADE)
    Status = models.CharField(max_length=20,default='pending')


    def __str__(self):
        return self.First_name



    
