# Generated by Django 3.1.5 on 2021-01-28 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210129_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='question', to='quiz.quizzes'),
        ),
    ]