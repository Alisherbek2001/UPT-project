from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel

class Member(BaseModel):
    fullname = models.CharField(_("fullname"),max_length=255)
    photo = models.ImageField(_("photo"),upload_to='members/')
    position = models.CharField(_("position"),max_length=255)
    
    def __str__(self) -> str:
        return self.fullname
    
    class Meta:
        verbose_name = _('Member')
        verbose_name_plural = _('Members')
        
class Category(BaseModel):
    title = models.CharField(_("title"),max_length=255)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Project(BaseModel):
    title = models.CharField(_('title'),max_length=255)
    photo = models.ImageField(upload_to="project/")
    category = models.ForeignKey(Category,models.CASCADE,verbose_name=_('Category'))
    link = models.CharField(_('link'),max_length=255)
    is_main = models.BooleanField(_('is main'),default=False)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')


class Feedback(BaseModel):
    text = models.TextField(_("text"))
    author = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.author