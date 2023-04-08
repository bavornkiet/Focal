from django.contrib import admin
from .models import Activities, Categories, UserActivities

# run the following to update the built-in database
# python .\manage.py makemigrations Focal_app
# python .\manage.py sqlmigrate Focal_app #(whatever 4-digit number is correct, found in Focal_app/migrations)

# to create a user, you can do it in CMD:
# python .\manage.py createsuperuser


admin.site.register(Activities)
admin.site.register(Categories)
admin.site.register(UserActivities)
