# Generated by Django 2.0.4 on 2018-04-12 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matrix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=80, verbose_name='Task Name')),
                ('importance', models.IntegerField(default=50, verbose_name='Importance')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matrix.Topic')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]