# Generated by Django 5.0.1 on 2024-01-27 18:43

import django.db.models.deletion
import games.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_rename_game_temp_game_image_view'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.TextField(default='Enjoy the game 😁', max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='CSS_file',
            field=models.FileField(upload_to='css_files/', validators=[games.models.validate_css]),
        ),
        migrations.AlterField(
            model_name='game',
            name='HTML_file',
            field=models.FileField(upload_to='html_files/', validators=[games.models.validate_html]),
        ),
        migrations.AlterField(
            model_name='game',
            name='Image_View',
            field=models.FileField(default='media_file/game.jpeg', upload_to='media_files/', validators=[games.models.validate_image_view]),
        ),
        migrations.AlterField(
            model_name='game',
            name='JS_file',
            field=models.FileField(upload_to='js_files/', validators=[games.models.validate_js]),
        ),
        migrations.AlterField(
            model_name='game',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='games', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='game',
            index=models.Index(fields=['-created'], name='games_game_created_9187a0_idx'),
        ),
    ]