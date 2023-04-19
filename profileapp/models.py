from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# 1. Matching 1:1 = Account : Profile
# - By Using 'OneToOneField()', 'Profile' is matched with 'one User object'.
# - 'on_delete=CASACADE' means Profile's objects is deleted when connected
#    object(User's) is deleted.
#
# 2. Upload_to = 'profile/'
# - Under 'media', 'profile' DIR will be created and images will be uploaded
# - at 'media/profile/'.
#
# 3. Model form
# - Converting an Existing Model to a Form.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=32, unique=True, null=True)
    message = models.CharField(max_length=128, null=True)


