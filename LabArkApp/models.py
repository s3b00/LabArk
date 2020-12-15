from django.contrib.auth.models import User, AnonymousUser
from django.urls import reverse
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)
    downloads = models.IntegerField(default=0)

    def __str__(self):
        return f"[{self.id}] {self.name}"


class Lab(models.Model):
    name = models.CharField(max_length=50, blank=False)
    course = models.IntegerField()
    year = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default="Без группы")
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=AnonymousUser)
    downloads = models.IntegerField(default=0)
    upload_time = models.DateTimeField()

    def get_absolute_url(self):
        return reverse('people.views.details', args=[str(self.id)])

    class Meta:
        ordering = ["-id"]
