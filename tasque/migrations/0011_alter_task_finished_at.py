# Generated by Django 4.0.2 on 2022-03-07 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasque', '0010_rename_updated_at_task_finished_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='finished_at',
            field=models.DateTimeField(verbose_name='完了日時'),
        ),
    ]