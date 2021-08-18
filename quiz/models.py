from django.db import models

class Stages(models.Model):
     stages = models.CharField(max_length=100)
     def __str__(self):
         return self.stages


class Questions(models.Model):
         question = models.CharField(max_length=300)
         stage = models.ForeignKey(Stages,on_delete=models.CASCADE,default="#1")
         option_1 =  models.CharField(max_length=150)
         option_2 =  models.CharField(max_length=150)
         option_3 =  models.CharField(max_length=150,null=True,blank=True)
         option_4 =  models.CharField(max_length=150,null=True,blank=True )
         answer =   models.CharField(max_length=150)

         def __str__(self):
             return self.question