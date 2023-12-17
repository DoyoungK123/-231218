from django.db import models

class Eggtart(models.Model):
    shop = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    thumbnail = models.ImageField("이미지", upload_to="post", blank=True)

    def __str__(self):
        return self.shop





