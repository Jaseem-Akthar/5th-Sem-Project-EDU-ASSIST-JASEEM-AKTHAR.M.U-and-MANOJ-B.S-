# Generated by Django 4.1.3 on 2023-02-07 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0008_rename_course_usercontact_user_course_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercontact',
            old_name='user_course',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='usercontact',
            old_name='user_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='usercontact',
            old_name='user_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='usercontact',
            old_name='user_number',
            new_name='number',
        ),
    ]
