from django.db import models
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField

class Post(models.Model):
    
    CHOISEFILD = (
        ('d', 'draft'),
        ('p', 'publish'),
    )
    title = TranslatedField(models.CharField(_('title'), max_length=255) )
    image = models.ImageField(_('image'),upload_to='media/%Y/%M/%D')
    text = TranslatedField(models.TextField(_('text')))
    date_publish = models.DateTimeField(_('date_publish'), )
    update = models.DateTimeField(_('update'))
    status = models.CharField(_('status'), max_length=1, choices=CHOISEFILD)
    show = models.BooleanField(_('show'), default=True)
    
    class Meta:
        ordering = ['-update']
        verbose_name = _('post')
        verbose_name_plural = _('posts')
    
    def __str__(self) -> str:
        return self.title