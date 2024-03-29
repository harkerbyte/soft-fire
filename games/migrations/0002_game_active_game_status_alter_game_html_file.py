# Generated by Django 5.0.1 on 2024-01-22 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('pb', 'publish'), ('df', 'draft')], default='df', max_length=2),
        ),
        migrations.AlterField(
            model_name='game',
            name='html_file',
            field=models.FileField(upload_to='html_files/'),
        ),
    ]
