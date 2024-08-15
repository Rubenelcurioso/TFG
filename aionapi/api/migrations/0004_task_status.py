# Generated by Django 5.0.7 on 2024-08-15 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('TODO', 'To do'), ('IN_PROGRESS', 'In progress'), ('DONE', 'Done')], default='TODO', max_length=20),
        ),
    ]
