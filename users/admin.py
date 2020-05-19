from django.contrib import admin
from .models import Profile

# register the user profile model here to allow us to see the default images in the admin panel
admin.site.register(Profile)