from django.db import models

class Response(models.Model):
    
    text = models.TextField()
    
class Response2(models.Model):
    
    text = models.TextField()

class ResponseGood(models.Model):
    
    text = models.TextField()

class ResponseBad(models.Model):
    
    text = models.TextField()

class ResponseNeutral(models.Model):
    
    text = models.TextField()

class GoodFortune(models.Model):
    
    text = models.TextField()

class NeutralFortune(models.Model):
    
    text = models.TextField()

class BadFortune(models.Model):
    
    text = models.TextField()

class DefaultFortune(models.Model):

    text = models.TextField()

