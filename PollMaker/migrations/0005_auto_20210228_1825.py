# Generated by Django 3.1.6 on 2021-02-28 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PollMaker', '0004_remove_pollquestion_can_make_own_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answerone', models.CharField(max_length=50)),
                ('answertwo', models.CharField(max_length=50)),
                ('answerthree', models.CharField(max_length=50)),
                ('answeronevotes', models.IntegerField(default=0)),
                ('answertwovotes', models.IntegerField(default=0)),
                ('answerthreevotes', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='PollAnswer',
        ),
        migrations.DeleteModel(
            name='PollQuestion',
        ),
    ]
