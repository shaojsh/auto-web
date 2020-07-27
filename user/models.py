from django.db import models


# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'user'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48, null=False)
    email = models.CharField(max_length=64, null=False, unique=True)
    password = models.CharField(max_length=128, null=False)

    def __repr__(self):
        return "".format(self.id, self.name)

    __str__ = __repr__


# API 任务创建
class ApiTask(models.Model):
    class Meta:
        db_table = 'ApiTask'

    id = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=48, null=True)
    email = models.CharField(max_length=64, null=True)
    projectBlongTo = models.CharField(max_length=48, null=True)
    projectEnvir = models.CharField(max_length=48, null=True)
    projectApiName = models.CharField(max_length=48, null=True)
    projectApiDes = models.CharField(max_length=480, null=True)
    projectApiPath = models.CharField(max_length=480, null=True)
    projectApiReqWay = models.CharField(max_length=48, null=True)
    projectApiPare = models.CharField(max_length=4800, null=True)
    projectCreatDate = models.CharField(max_length=48, null=True)

    def __repr__(self):
        return "".format(self.id, self.name)

    __str__ = __repr__
