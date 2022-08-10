from django.db import models

# Create your models here

class Visitors(models.Model):
    visitor = models.IntegerField(default=1)
    def __str__(self):
        return 'Visitors'



class Me(models.Model):
    name = models.CharField(max_length=5000,verbose_name='Ismni kiritish',help_text="Ismni kiritish")
    age = models.IntegerField(verbose_name='Yoshni kiritish',help_text="Yoshni kiritish")
    technologies = models.TextField(verbose_name='Technologies',help_text='Technolgies')
    profession = models.CharField(max_length=5000,verbose_name='Kasbni kiritish',help_text="Kasbni kiritish")
    language = models.CharField(max_length=5000,verbose_name='Tilni kiritish',help_text="Tilni kiritish")
    image = models.ImageField(upload_to='profile-images',verbose_name='Profil rasmi',help_text='Profil rasmi')
    cv = models.FileField(upload_to='cvs',verbose_name='CV',help_text='cv')
    def __str__(self):
        db_table = 'Me'
        return self.name
class SocialLinks(models.Model):
    telegram = models.URLField(default='behzodasliddinov.uz')
    instagram = models.URLField(default='behzodasliddinov.uz')
    facebook= models.URLField(default='behzodasliddinov.uz')
    github = models.URLField(default='behzodasliddinov.uz')
    youtube = models.URLField(default='behzodasliddinov.uz')
    linkedin= models.URLField(default='behzodasliddinov.uz')
    phone = models.CharField(max_length=500,default='+998 99 116-04-34')
    def __str__(self):
        return 'Social Links'

class Portfolio(models.Model):
    name = models.CharField(max_length=500,verbose_name="Loyiha nomi")
    image = models.ImageField(upload_to='portfolio',verbose_name='Loyiha rasmi')
    url = models.URLField(verbose_name='Loyiha manzili')
    def __str__(self):
        return self.name