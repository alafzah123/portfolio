from django.db import models

class Client(models.Model):
    image = models.ImageField(upload_to='clients/')

class Project(models.Model):
    title = models.CharField(max_length=50)

class ImageMedia(models.Model):
    image = models.ImageField(upload_to='projects/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')

class Testimonial(models.Model):
    name = models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to='testimonials/')
    position = models.CharField(max_length=30)
    rating = models.DecimalField(max_digits=2, decimal_places=1, choices=[
        (1, '1'), (1.5, '1.5'), (2, '2'), (2.5, '2.5'), 
        (3, '3'), (3.5, '3.5'), (4, '4'), (4.5, '4.5'), (5, '5')
    ])
    review = models.TextField()
class Enquiry(models.Model):
    name  = models.CharField(max_length=30)
    email =models.EmailField(max_length=254)
    subject = models.CharField(max_length=30)
    message = models.TextField()
class Quotation(models.Model):
    name  = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    message = models.TextField()
