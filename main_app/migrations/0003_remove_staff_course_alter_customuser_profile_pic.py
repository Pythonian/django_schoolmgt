# Generated by Django 4.0.6 on 2023-07-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_admin_id_alter_attendance_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='course',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
