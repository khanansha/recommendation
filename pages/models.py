from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

# Create your models here.
Cuisine = (
    ('American', 'American'),
    ('Chinese', 'Chinese'),
    ('European', 'European'),
    ('Greek', 'Greek'),
    ('Indian', 'Indian'),
    ('Italian', 'Italian'),
    ('Spanish', 'Spanish'),
    ('Thai', 'Thai'),
    ('Lebanese', 'Lebanese'),

)

Lifestyle = (
    ('Fashion', 'Fashion'),
    ('Car Rental', 'Car Rental'),
    ('Nightlife', 'Nightlife'),
    ('Luxury Purchase', 'Luxury Purchase'),
    ('Business & Corporate', 'Business & Corporate'),
    ('Gastronomy', 'Gastronomy'),
    ('Career Counseling for Kids', 'Career Counseling for Kids'),

)

Travel = (
    ('Nature & Outdoors', 'Nature & Outdoors'),
    ('Family', 'Family'),
    ('Weekend Getaways', 'Weekend Getaways'),
    ('Desert Safari', 'Desert Safari'),
    ('Safari', 'Safari'),
    ('Historical & Heritage', 'Historical & Heritage'),
    ('Romantic Getaways', 'Romantic Getaways'),

)


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    Cuisine = models.CharField(max_length=100, default=False, null=True)
    Lifestyle = models.CharField(max_length=100, default=False, null=True)
    Travel = models.CharField(max_length=100, default=False, null=True)
    Hotel = models.CharField(
        max_length=100, default=False, null=True)

    # def __str__(self):
    #     return self.user.username
