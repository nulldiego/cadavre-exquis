from django.db import models
from django.urls import reverse
from django.utils.html import linebreaks
from django.utils.safestring import mark_safe

# Create your models here.

class Cadavre(models.Model):
    """Model representing a cadavre exquis game."""
    title = models.CharField(max_length=200, help_text='Introduce un título', verbose_name='Título')
    code = models.SlugField(max_length=200, help_text='Introduce un código secreto', verbose_name='Código', unique=True, null=False)

    def display_cadavre(self):
        """Create a string for the cadavre content. This is required to display full cadavre exquis in Admin."""
        return mark_safe('\n'.join(linebreaks(cadavrePart.content) for cadavrePart in CadavrePart.objects.filter(cadavre=self.id)))
    
    display_cadavre.short_description = 'Cadavre Exquis'
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title

class CadavrePart(models.Model):
    """Model representing a cadavre exquis part."""
    cadavre = models.ForeignKey(Cadavre, on_delete=models.CASCADE)
    content = models.TextField(help_text='Introduce la continuación', verbose_name='Continuación')
    author = models.CharField(max_length=200, help_text='Introduce tu nombre', verbose_name='Autor')

    def display_content(self):
        """Create a string for the cadavre part content. This is required to display cadavre part multiline in Admin."""
        return mark_safe(linebreaks(self.content))
    
    display_content.short_description = 'Continuación'

    class Meta:
        ordering = ['cadavre', 'id']
    
    def __str__(self):
        """String for representing the Model object."""
        return self.content