from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

# Todo Categories
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_category_user')
    name = models.CharField(max_length=25)
    color = models.CharField(max_length= 64, null=True, blank=True)
    icon = models.CharField(max_length= 64, null=True, blank=True)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name_plural = 'Categories'

# Todo
class TodoManager(models.Manager):
    def not_completed(self, user):
        categories = Category.objects.filter(Q(user=user) | Q (user__id=1))
        not_completed = {}
        for category in categories:
            not_completed[category] = self.filter(user=user, completed=False, category=category).order_by('-date_added')
        return not_completed

    def all_todos(self, user):
        return self.filter(user=user)


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now=False, auto_now_add=True, )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='todo_category')
    task = models.CharField(max_length=140)
    completed = models.BooleanField(default=False)
    date_updated = models.DateField(auto_now=True)
    objects = TodoManager()
    def __str__(self):
        return f"{self.category} , {self.task}"