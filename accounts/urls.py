from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

from . import forms

urlpatterns = patterns(
    'accounts.views',
    url(r'^login/$', auth_views.login,
        {'template_name': 'accounts/login.jade',
         'authentication_form': forms.LoginForm},
        name='login'),
    url(r'^logout/$', auth_views.logout,
        {'template_name': 'accounts/logout.jade'},
        name='logout'),
    url(r'^password/change/$', auth_views.password_change,
        name='auth_password_change'),
    url(r'^password/change/done/$', auth_views.password_change_done,
        name='auth_password_change_done'),
    url(r'^password/reset/$', auth_views.password_reset,
        name='auth_password_reset'),
    url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        name='auth_password_reset_confirm'),
    url(r'^password/reset/complete/$', auth_views.password_reset_complete,
        name='auth_password_reset_complete'),
    url(r'^password/reset/done/$', auth_views.password_reset_done,
        name='auth_password_reset_done'),
    url(r'^register/$', 'register', name="register"),
    url(r'^auth/$', 'client_auth', name="client_auth"),
    url(r'^verify/$', 'client_verify'),
    url(r'^associate-steam/', 'associate_steam', name="associate_steam"),
    url(r'^(?P<username>[\w-]+)/library/$', 'library_show',
        name="library_show"),
    url(r'^library/add/(?P<slug>[\w-]+)/$', 'library_add',
        name="add_to_library"),
    url(r'^library/remove/(?P<slug>[\w-]+)/$', 'library_remove',
        name="remove_from_library"),
    url(r'^library/steam-sync/', 'library_steam_sync',
        name="library_steam_sync"),
    url(r'([\w-]+)/edit/$', 'profile_edit', name='profile_edit'),
    url(r'([\w-]+)/$', 'user_account', name="user_account"),
)
