from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# the best thing about django is that it allows you to switch between databases
# can build your app in sqlite then switch to mysql, for example

# this is a model that will describe the columns in a table in the django app
# to make changes to db with this model in mind: python manage.py makemigrations -> then python manage.py migrate
# can see the sql code that will be made for us in cmd line: python manage.py sqlmigrate [project name] [number 0001]
# can query db via cmd line using shell -> python manage.py shell
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()  # there is no restriction on the size
    date_posted = models.DateTimeField(auto_now_add=True)  # time is set to time at creation (auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # author is a foreign key coming from other table.
                                                                # if user is deleted, it will delete their posts.

    # this function is used to provide more descriptive information to describe table
    def __str__(self):
        return self.title

    # this function is used to set the url of the post
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
