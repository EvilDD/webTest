from django.db import models

# Create your models here.


class apiProject(models.Model):
    project_name = models.CharField(max_length=30)
    doc_path = models.CharField(max_length=30)
    descripts = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name


class apiName(models.Model):
    project = models.ForeignKey(apiProject)
    api_name = models.CharField(max_length=30)
    post_url = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.api_name


class apiData(models.Model):
    apiName = models.ForeignKey(apiName)
    dataName = models.CharField(max_length=30, default='')
    api_data = models.CharField(max_length=30)
    isWrite = models.BooleanField(default=False)

    def __str__(self):
        return self.dataName
