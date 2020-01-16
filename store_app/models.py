from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    manufacturer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img', default='static/img/default.jpg')

    def __str__(self):
        return self.title
