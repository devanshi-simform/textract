# Generated by Django 4.0.5 on 2022-06-20 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_storage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file_upload',
            name='file',
        ),
        migrations.AddField(
            model_name='file_upload',
            name='profile_image',
            field=models.ImageField(blank=True, default='profiles/user-default.png', null=True, upload_to='profiles/'),
        ),
        migrations.AlterField(
            model_name='file_upload',
            name='choice',
            field=models.CharField(blank=True, choices=[('Form', 'Form'), ('Table', 'Table(key-value)'), ('Text', 'Text(line-by-line)')], max_length=10, null=True),
        ),
    ]
