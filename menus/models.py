from django.db import models


class PageModel(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    position = models.IntegerField()
    visible = models.BooleanField()

    def __str__(self):
        return self.name


class MenuModel(models.Model):
    name = models.CharField(max_length=255)
    position = models.IntegerField()
    visible = models.BooleanField()
    page = models.ForeignKey(PageModel, related_name='page_id')

    def __str__(self):
        return self.name
