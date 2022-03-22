from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)  # TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.user_name


class Content(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
