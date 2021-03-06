# Generated by Django 3.0.6 on 2020-05-26 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GreetingsData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('from_field', models.CharField(db_column='from', max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('id_column', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'greetings_data',
                'managed': False,
            },
        ),
    ]
