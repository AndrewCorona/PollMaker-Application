# Generated by Django 3.1.6 on 2021-02-24 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PollMaker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pollquestion',
            name='can_make_own_answer',
        ),
    ]