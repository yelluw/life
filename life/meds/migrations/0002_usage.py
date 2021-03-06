# Generated by Django 3.0.2 on 2020-01-28 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taken', models.DateTimeField()),
                ('note', models.TextField(default='')),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meds.Medication')),
            ],
            options={
                'ordering': ['-taken'],
            },
        ),
    ]
