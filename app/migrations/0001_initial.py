# Generated by Django 4.2.6 on 2023-12-08 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=100)),
                ('loc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Salgrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('losal', models.IntegerField()),
                ('hisal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.IntegerField(primary_key=100, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('mgr', models.IntegerField()),
                ('hiredate', models.DateField()),
                ('sal', models.IntegerField()),
                ('comm', models.IntegerField()),
                ('deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]
