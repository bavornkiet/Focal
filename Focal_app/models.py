from django.db import models
from django.contrib.auth.models import User

# run the following commands in cmd to update the built-in database
# python .\manage.py makemigrations Focal_app
# python .\manage.py sqlmigrate Focal_app (whatever 4-digit number is correct, found in Focal_app/migrations)
# python .\manage.py migrate --run-syncdb

# categories table
class Categories(models.Model):
    categoryId = models.IntegerField(name='categoryId', primary_key=True, null=False)
    name = models.CharField(name='name', max_length=30)
    description = models.CharField(name='description', max_length=200)

    def __str__(self):
        return '%s' % self.name


# activities table
class Activities(models.Model):
    activityId = models.IntegerField(name='activityId', primary_key=True, null=False)
    name = models.CharField(name='name', null=False, max_length=30)
    description = models.CharField(name='description', max_length=200)
    categoryId = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.name

# user activities table
class UserActivities(models.Model):
    useractivityId = models.IntegerField(name='useractivityId', primary_key=True, null=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE, max_length=30)
    activityId = models.ForeignKey(Activities, on_delete=models.CASCADE)
    time = models.DateTimeField(name="Date")

    def __str__(self):
        return ""
