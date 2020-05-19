from django.db import models
from django.contrib.auth.models import User


# create a model that allows for profile picture upload
# after creating this model, will need to conduct migrations to move it to database
# python manage.py makemigrations (first, pip install Pillow to work with pictures)
# then python manage.py migrate
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # create 1 to 1 relationship with existing user model
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')  # set default picture and directory

    # specify how the object will be described when it is referred in the application
    def __str__(self):
        return f'{self.user.username} Profile'
