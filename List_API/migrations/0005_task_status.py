# Generated by Django 4.2.15 on 2024-08-27 12:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('List_API', '0004_taskcategory_task_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('N', 'New'), ('I', 'In Progress'), ('C', 'Completed')], default='N',
                                   max_length=1),
        ),
    ]
