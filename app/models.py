from django.db import models

# Create your models here.
class dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)

    def __str__(self):
        return self.deptno
    

class emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    sal=models.IntegerField()
    dept=models.ForeignKey(dept,on_delete=models.CASCADE)



class bonus(models.Model):
    ename=models.IntegerField(primary_key=True)
    job=models.CharField(max_length=100)
    sal=models.IntegerField()
    comm=models.IntegerField()

class salgrade(models.Model):
    grade=models.IntegerField()
    losal=models.IntegerField()
    hisal=models.IntegerField()

