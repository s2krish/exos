from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    random_number = models.IntegerField()
    birthday = models.DateField(help_text=_("In YYYY-MM-DD format"))

    def delete(self):
        '''Deletes user when profile deleting
        '''
        user = self.user
        super(UserProfile, self).delete()
        user.delete()
