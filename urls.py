from django.conf.urls.defaults import *
from django.contrib import admin
import dbindexer

handler500 = 'djangotoolbox.errorviews.server_error'

# django admin
admin.autodiscover()

# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    ('^d/.*$', 'django.views.generic.simple.direct_to_template', {'template': 'viewdoc.html'}),
    ('^v/.*$', 'django.views.generic.simple.direct_to_template', {'template': 'verifyid.html'}),

    # Phone
    (r'^sms/(.*)$', 'views.phone.sms'),
    (r'^call/(.*)$', 'views.phone.call'),
    (r'^twiml/(.*)$', 'views.phone.twiml'),
    # Mail
    (r'^mail/(.*)$', 'views.mail.send'),

    ('^admin/', include(admin.site.urls)),
    ('^author/create', 'views.author.create'),
    ('^supporter/create', 'views.supporter.create'),
    ('^link/create', 'views.link.create'),
    (r'^author/(.*)$', 'views.author.get'),
    (r'^supporter/(.*)$', 'views.supporter.get'),
    (r'^link/(.*)$', 'views.link.get')
)
