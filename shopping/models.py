from django.db import models
from django.contrib.auth.models import User

# Shopping Categories
class Category(models.Model):
    name = models.CharField(max_length=25)
    color = models.CharField(max_length= 64, null=True, blank=True)
    icon = models.CharField(max_length= 64, null=True, blank=True)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name_plural = 'Categories'

# Shopping item
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now=False, auto_now_add=True, )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item = models.CharField(max_length=140)
    bought = models.BooleanField(default=False)
    date_updated = models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.category} , {self.item}"