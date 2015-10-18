from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
import os
from django.template.defaultfilters import slugify

CHOICES = [(i,i) for i in range(6)]
def upload_image_to(instance, filename):
        from django.utils.timezone import now
        filename_base, filename_ext = os.path.splitext(filename)
        return 'images/%s%s%s' % (
            filename_base,
            now().strftime("%Y%m%d%H%M%S"),
            filename_ext.lower(),)

class Horchata(models.Model):
    order       = models.IntegerField(_('Order'), default=0)
    publish     = models.BooleanField(_('Publicado'), default=False)
    credit_card = models.BooleanField(_('Aceptan Tarjeta'), default=False)
    name        = models.CharField(_('Nombre'), max_length=140)
    slug        = models.SlugField(_('Slug'), editable=False)
    price       = models.IntegerField(_('Precio'), default=0)
    grade       = models.IntegerField(_('Calificacion'),choices=CHOICES, default=0) 
    address     = models.CharField(_('Direccion'), max_length=300)
    map_url     = models.URLField(_('URL mapa'))
    description = RichTextField(_('Descripcion'))
    image       = models.ImageField(_('Imagen'), upload_to=upload_image_to)
    date        = models.DateField(_('Fecha agregada'), auto_now_add=True)
    updated     = models.DateField(_('Fecha editado'), auto_now=True)
    tags        = TaggableManager(blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Horchata, self).save(*args, **kwargs)
    class Meta:
        ordering  = ['order', 'date', 'name']
    def __unicode__(self):
        return u'%s' % (self.name)
    def __str__(self):
        return u'%s' % (self.name)
    def AdminImage(self):
        return '<img style="height:100px;width:auto;display:block;" src="%s"&>' % self.image.url
    AdminImage.allow_tags = True
