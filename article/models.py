import os
import os.path
from django.db import models
from time import time
from django.db.models import signals
from django.conf import settings
from django_test import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from approvals.models import Approval
from approvals.signals import article_approved

import logging
logr = logging.getLogger(__name__)

def get_upload_file_name(instance, filename):
    return settings.UPLOAD_FILE_PATTERN % (str(time()).replace('.','_'), filename)
    
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
    thumbnail = models.FileField(upload_to=get_upload_file_name)
    approved = models.BooleanField(default=False)

    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/articles/get/%i/" % self.id  
    
    def get_thumbnail(self):
        thumb = str(self.thumbnail)
        if not settings.DEBUG:
            thumb = thumb.replace('assets/', '')
            
        return thumb            
    
@receiver(post_save, sender=Article)
def create_approval_on_new_article(sender, **kwargs):
    if kwargs.get('created', False):
        approval = Approval.objects.create(article_id=kwargs.get('instance').id)
        logr.debug("Approval created: %s" % approval)
        

@receiver(article_approved)
def approve_article(sender, **kwargs):
    a = Article.objects.get(id=kwargs.get('article_id'))
    a.approved = True
    a.save()
    logr.debug("Approval recieved")
        

    
class Comment(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    article = models.ForeignKey(Article)
    
    

