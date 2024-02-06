# Generated by Django 5.0.1 on 2024-02-06 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0003_alter_course_code_alter_room_name_alter_student_bi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duraction_unit',
            field=models.CharField(choices=[('D', 'DAYS'), ('W', 'WEEKS'), ('M', 'MONTHS'), ('Y', 'YEARS')], default='M', max_length=10),
        ),
    ]
