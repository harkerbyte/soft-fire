from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import os
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.db.models.signals import pre_delete

def validate_image_view(self):
    _,exts = os.path.splitext(self.name)
    extd = str(exts)
    valid_extension = ('.jpeg','.jpg','.png','.svd','.jfif','.jpg','.tif','.webp','.gif')
    if not extd.endswith(valid_extension):
        raise ValidationError('Unsupported image file')

def validate_html(self):
    _, html = os.path.splitext(self.name)
    _html = str(html)
    valid_extension = ('.html')
    if not _html.endswith(valid_extension):
        raise ValidationError('That wasn\'t an html file')
    
def validate_js(self):
    _, file = os.path.splitext(self.name)
    _file = str(file)
    valid_extension = ('.js')
    if not _file.endswith(valid_extension):
        raise ValidationError('That wasn\'t a javascript file')
    
def validate_css(self):
    valid_extension = '.css'
    _, file_extension = os.path.splitext(self.name)
    if not str(file_extension).endswith(valid_extension):
        raise ValidationError('That doesn\'t look like a \'.css\' file')

class Supports(models.TextChoices):
    Mobile_And_Pc = "Mobile And Pc"
    Pc_only = "Pc only"
    Mobile_only = "Mobile only"
    
    
class BaseStorage(models.Model):
    class Meta:
        abstract = True
        
    def delete_related_files(self, field_name):
            file_field = getattr(self, field_name)
            storage, path = file_field.storage, file_field.path
            storage.delete(path)

class game(BaseStorage):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,
                               related_name = 'games',
                               on_delete = models.CASCADE,
                               default = 3)
    
    description = models.TextField(max_length= 300,
                                   default = 'Enjoy the game 🎮')
    
    supports = models.CharField(max_length=14,
                                choices= Supports.choices,
                                default=Supports.Mobile_And_Pc)
    
    url = models.SlugField(max_length=90)
    Image_View = models.ImageField(upload_to='media_files/',
                                 validators = [validate_image_view])

    active = models.BooleanField(default=True)
    
    HTML_file = models.FileField(upload_to='html_files/',
                                 validators = [validate_html])
        
    JS_file = models.FileField(upload_to='js_files/',
                               validators =[validate_js])
    
    CSS_file = models.FileField(upload_to='css_files/',
                                validators = [validate_css])
    created = models.DateField(default=timezone.now)
    tweaked = models.DateField(auto_now=True)
    
    
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]
    
    def get_absolute_url(self):
        return reverse("game:gaming",
                       args = [self.url])
    
    
    def __str__(self):
        return f'{self.title} by {self.author}'

