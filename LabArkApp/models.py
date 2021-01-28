from datetime import datetime

from django.contrib.auth.models import User, AnonymousUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.db import models
import os
from django.db.models.aggregates import Sum


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reputation = models.IntegerField(default=0)
    uploads = models.IntegerField(default=0)
    userpic = models.ImageField(upload_to="userpics", default="default.png")
    status = models.TextField(max_length=100, default="Мой первый статус!")

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    downloads = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
         return reverse('category_labs', args=[self.id])
    
    def get_views(self):
        return Lab.objects.filter(category__pk=self.pk).aggregate(Sum('views'))['views__sum']


class Lab(models.Model):
    name = models.CharField(max_length=50, blank=False)
    course = models.IntegerField()
    variant = models.CharField(default="Без варианта", max_length=20)
    year = models.IntegerField(default=datetime.now().year)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    upload_time = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="files")
    rating = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('people.views.details', args=[str(self.id)])

    def __str__(self):
        return f"<{self.author.username}> {self.name}"

    def extension(self):
            name, extension = os.path.splitext(self.file.name)
            return extension

    class Meta:
        ordering = ["-id"]
