from django.db import models


class Company(models.Model):
    class Meta:
        db_table = 'companies'
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=511, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

