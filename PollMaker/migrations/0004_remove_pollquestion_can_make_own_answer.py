# Generated by Django 3.1.6 on 2021-02-27 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PollMaker', '0003_pollquestion_can_make_own_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pollquestion',
            name='can_make_own_answer',
        ),
    ]
