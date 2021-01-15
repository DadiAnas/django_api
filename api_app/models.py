from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Customer(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, null=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=50, choices=[('ml', 'male'), ('fm', 'female')])
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return '<Customer %s >' % self.email
