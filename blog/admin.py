from django.contrib import admin
from .models import Post

# use this page to register your models so that they come up in the admin panel
# here, I am registering the Post model to the admin panel
# now, it should appear in admin panel
admin.site.register(Post)
