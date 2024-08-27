from django.db import models

# Create your models here.
class Task(models.Model):
    # Add priority choices
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'), ]

    # Status choices
    STATUS_CHOICES = [
        ('N', 'New'),
        ('I', 'In Progress'),
        ('C', 'Completed'), ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    # Add priority field
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='L')
    # Add status field
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')

    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # Foreign key to TaskCategory
    category = models.ForeignKey('TaskCategory', on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Automatically mark completed as True if status is completed
        if self.status == 'C':
            self.completed = True
        # Automatically set status to completed if completed is True
        if self.completed:
            self.status = 'C'

        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class TaskCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
