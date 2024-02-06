# Generated by Django 5.0.1 on 2024-02-06 20:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=255)),
                ('duraction', models.IntegerField()),
                ('duraction_unit', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('MARKED', 'MARKED'), ('STARTED', 'STARTED'), ('FINISHED', 'FINISHED')], max_length=50)),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='center.course')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='center.room')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bi', models.CharField(max_length=14)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='M', max_length=1)),
                ('race', models.CharField(choices=[('B', 'BLACK'), ('W', 'WHITE')], default='B', max_length=1)),
                ('civil_status', models.CharField(choices=[('S', 'SINGLE'), ('M', 'MARRIED'), ('D', 'DIVORCED'), ('W', 'WIDOWER')], default='S', max_length=1)),
                ('natianality', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('class_room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='center.classroom')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='center.student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bi', models.CharField(max_length=14)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='M', max_length=1)),
                ('race', models.CharField(choices=[('B', 'BLACK'), ('W', 'WHITE')], default='B', max_length=1)),
                ('civil_status', models.CharField(choices=[('S', 'SINGLE'), ('M', 'MARRIED'), ('D', 'DIVORCED'), ('W', 'WIDOWER')], default='S', max_length=1)),
                ('natianality', models.CharField(max_length=100)),
                ('formation_area', models.CharField(max_length=100)),
                ('formation_title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0)),
                ('unit', models.CharField(default='', max_length=10)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('class_room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='center.classroom')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='center.student')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='center.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='center.teacher'),
        ),
    ]
