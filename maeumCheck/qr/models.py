from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200)
    people = models.IntegerField()
    linkIn = models.URLField()
    linkOut = models.URLField()
    qrImage = models.ImageField(upload_to='qrcodes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
