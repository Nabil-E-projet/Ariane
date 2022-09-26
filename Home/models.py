from django.db import models

class Comments(models.Model):
    name = models.CharField(max_length=25000, blank=True, null=True, verbose_name='Name')

    comments = models.CharField(max_length=25000, blank=True, null=True, verbose_name='Comments')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    def __str__(self):
        return self.name



