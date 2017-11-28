from django.db import models


class Company(models.Model):
    class Meta:
        db_table = 'companies'
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    #fields
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

