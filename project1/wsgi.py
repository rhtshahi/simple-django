"""
WSGI config for project1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

'''
old code: 

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')

application = get_wsgi_application()
'''

import os
import sys

# Path to your virtualenv
virtenv = os.path.expanduser('~') + '/ROOT/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')

# Activate the virtualenv
try:
    if sys.version.split(' ')[0].split('.')[0] == '3':
        exec(compile(open(virtualenv, "rb").read(), virtualenv, 'exec'), dict(__file__=virtualenv))
    else:
        execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

# Add your Django project path
sys.path.append(os.path.expanduser('~') + '/ROOT')
sys.path.append(os.path.expanduser('~') + '/ROOT/project1')

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'project1.settings'

# Import the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
