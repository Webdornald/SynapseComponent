from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from profileapp.models import Profile

has_ownership = [account_ownership_required, login_required]


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('informationapp:index')
    template_name = 'accountapp/create.html'

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user, nickname='default')
        return super().form_valid(form)


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    def get_context_data(self, **kwargs):
        role_list = self.object.profile.role_tag.all()
        object_list = self.object.profile.participants.all()
        return super(AccountDetailView, self).get_context_data(object_list=object_list, role_list=role_list)


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('informationapp:index')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('informationapp:index')
    template_name = 'accountapp/delete.html'


class AccountListView(ListView):
    model = User
    context_object_name = 'account_list'
    template_name = 'accountapp/list.html'
