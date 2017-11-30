from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from . import views

auth_urls = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'CRM/auth/login.html', 'redirect_authenticated_user': True}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

]

app_urls = [
    url(r'^$',
        TemplateView.as_view(template_name='CRM/home.html'),
        name='home'),
    url(r'^companies/$',
        views.CompaniesListView.as_view(),
        name='companies_list_views'),
    url(r'^users/$',
        views.UsersListView.as_view(),
        name='users_list_views'),
    url(r'^users/edit/(?P<pk>\d+)$',
        views.UserUpdate.as_view(),
        name='edit_user'),
    url(r'^companies/delete/(?P<pk>\d+)$',
        views.CompanyDelete.as_view(),
        name='delete_company'),
    url(r'^companies/edit/(?P<pk>\d+)$',
        views.CompanyUpdate.as_view(),
        name='edit_company')
]

urlpatterns = app_urls + auth_urls
