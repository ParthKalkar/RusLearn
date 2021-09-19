"""
WSGI config for ruslearn project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os, sys

# # add the hellodjango project path into the sys.path
# sys.path.append('ruslearn')
#
# # add the virtualenv site-packages path to the sys.path
sys.path.append('venv/lib/python3.8/site-packages')



from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruslearn.settings')

application = get_wsgi_application()
