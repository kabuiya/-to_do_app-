from django.db import models


# Create your models here.
class Activities(models.Model):
    Activity_name = models.CharField(max_length=20)
    completed = models.BooleanField(default=False, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Activity_name


