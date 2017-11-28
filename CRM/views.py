from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, FormView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import NewCompanyForm
from .models import Company


def index(request):
    return render(request, 'CRM/home.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.is_active = False
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'CRM/signup.html', {'form': form})


class CompaniesListView(LoginRequiredMixin, ListView, FormView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_denied_message = "You don't have an acess to view companies list"

    model = Company
    template_name = "CRM/companies.html"

    form_class = NewCompanyForm
    success_url = '/companies'



    def get_queryset(self):
        return Company.objects.all()

    def form_valid(self, form):
        form.save()
        return super(CompaniesListView, self).form_valid(form)


class CompanyUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_denied_message = "You don't have an acess to edit companies"

    model = Company
    fields = ['name']
    template_name = "CRM/edit-company.html"

    def get_success_url(self):
        return "/companies/"


class CompanyDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_denied_message = "You don't have an acess to edit companies"

    model = Company
    success_url = '/companies'
    template_name = "CRM/delete-company.html"


class UsersListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_denied_message = "You don't have an acess to view users list"

    model = User
    template_name = "CRM/users.html"

    def get_queryset(self):
        """Return the last five published questions."""
        return User.objects.order_by('is_active').reverse()


class UserUpdate(UserPassesTestMixin, UpdateView):

    def test_func(self):
        return self.request.user.is_staff

    model = User
    fields = ['id',
              'is_superuser',
              'username', 'first_name',
              'last_name',
              'email',
              'is_staff',
              'is_active',
              'user_permissions'
              ]
    success_url = '/companies'


    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_denied_message = "You don't have an acess to edit users list"

    template_name = "CRM/edit-user.html"


