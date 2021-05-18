# Generated by Django 3.2.3 on 2021-05-18 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('tid', models.CharField(max_length=50)),
                ('credit', models.CharField(max_length=50)),
                ('cls_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'system_course',
            },
        ),
        migrations.CreateModel(
            name='Select_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=50)),
                ('sid', models.CharField(max_length=50)),
                ('tid', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'system_select_course',
            },
        ),
    ]
