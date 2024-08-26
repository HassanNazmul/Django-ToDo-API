from django.db import models

# Create your models here.
class Task(models.Model):
    # Add priority choices
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'), ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    # Add priority field
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='L')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title