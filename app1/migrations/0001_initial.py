# Generated by Django 3.0.5 on 2020-07-09 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=50)),
                ('cfaculty', models.CharField(max_length=100)),
                ('cdate', models.DateField(auto_now_add=True)),
                ('ctime', models.CharField(max_length=30)),
                ('cfee', models.FloatField()),
                ('cduration', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('contact_no', models.IntegerField(unique=True)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('scourses', models.ManyToManyField(to='app1.CourseModel')),
            ],
        ),
    ]