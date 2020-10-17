from django.db import models
class Hero(models.Model):
    Name=models.CharField(max_length=60)
    Alias=models.CharField(max_length=50)
    img=models.ImageField(upload_to="pics")

    def __str__(self):
        return self.Name