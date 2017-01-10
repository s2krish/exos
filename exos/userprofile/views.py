from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.utils.translation import ugettext as _


from .forms import UserProfileCreationForm
from .models import UserProfile


class SuccessMessage(object):
    def get_success_url(self):
        if getattr(self, 'initial', None):
            messages.success(self.request, _('User updated'))
        else:
            messages.success(self.request, _('User added'))
        return reverse_lazy('list')


class UserProfileCreateView(SuccessMessage, CreateView):
    form_class = UserProfileCreationForm
    template_name = 'user_profile/form.html'


class UserProfileListView(ListView):
    model = UserProfile
    template_name = 'user_profile/list.html'
    context_object_name = 'profile_list'


class UserProfileUpdateView(SuccessMessage, UpdateView):
    '''Can change birthday
    '''
    model = UserProfile
    template_name = 'user_profile/form.html'

    fields = ['birthday']


class UserProfileDeleteView(DeleteView):
    '''Can change birthday
    '''
    model = UserProfile

    def get_success_url(self):
        messages.success(self.request, _('User deleted'))
        return reverse_lazy('list')
