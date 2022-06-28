from distutils.command.upload import upload
from django.db import models
from django.forms import IntegerField

# Create your models here.

class HomeBG(models.Model):
    name1 = models.CharField('BG name1', max_length=30)
    name2 = models.CharField('BG name2', max_length=30)
    about = models.TextField('BG about')
    price = models.IntegerField('BG price', null=True, blank=True)
    img = models.ImageField('BG image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeBG'
        verbose_name_plural = 'HomesBG'

    
class TourIdea(models.Model):
    name = models.CharField('TourIdea name', max_length=30)
    about = models.TextField('TourIdea')
    img = models.ImageField('TourIdea image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TourIdea'
        verbose_name_plural = 'TourIdeas'

class OfferGoods(models.Model):
    name = models.CharField('OfferGoods name', max_length=30)
    price = models.IntegerField('Goods price')
    img = models.ImageField('OfferGoods image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'OfferGoods'
        verbose_name_plural = 'OfferGoods'

class SwipeReserve(models.Model):
    name = models.CharField('SwipeReserve name', max_length=30)
    img = models.ImageField('SwipeReserve image', upload_to='media')
    about = models.TextField('SwipeReserve')
    
    def __str__(self):
        return self.name
             
    class Meta:
        verbose_name = 'SwipeReserve'
        verbose_name_plural = 'SwipeReserve'

class Thinks(models.Model):
    name = models.CharField('Thinks name', max_length=30)
    img = models.ImageField('Thinks image', upload_to='media')
    about = models.TextField('Thinks')
    job = models.TextField('Job name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Thinks'
        verbose_name_plural = 'Thinks'

class NextTourPlace(models.Model):
    img = models.ImageField('Place image', upload_to='media')
    name = models.CharField('Place name', max_length=30)
    about = models.TextField('Place about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'NextTourPlace'
        verbose_name_plural = 'NextTourPlace'

class Info1(models.Model):
    img = models.ImageField('Info1 image', upload_to='media')
    text1 = models.CharField('textinfo1', max_length=30)
    text2 = models.TextField('textinfo2')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Info1'
        verbose_name_plural = 'Info1'

class Info2(models.Model):
    img1 = models.ImageField('info2 image1', upload_to='media')
    img2 = models.ImageField('Info2 image2', upload_to='media')
    text1 = models.CharField('textinfo1', max_length=30)
    text2 = models.CharField('textinfo2', max_length=30)
    about1 = models.TextField('about1')
    about2 = models.TextField('about2')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Info2'
        verbose_name_plural = 'Info2'

class CategoryStays(models.Model):
    name = models.TextField('rent')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'CategoryStays'
        verbose_name_plural = 'CategoryStays'

