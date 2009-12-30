from distutils.core import setup
import os

setup(
   name = 'django_avatar_crop',
   packages = ['avatar_crop', 'avatar_crop.templatetags'],
   package_dir = {'avatar_crop': 'avatar_crop'},
   package_data = {'avatar_crop': ['templates/avatar_crop/*.html', 'media/js/*.js']},
   version = '0.1.1a',
   description = 'Custom avatar cropping for django-avatar',
   author = 'Andrii Kurinnyi',
   author_email = 'andrew@zen4ever.com',
   url = 'http://github.com/zen4ever/django-avatar-crop',
   keywords = ['django', 'avatar', 'cropping'],
   classifiers = [
       'Programming Language :: Python',
       'Development Status :: 3 - Alpha',
       'Intended Audience :: Developers',
       'License :: OSI Approved :: MIT License',
       'Operating System :: OS Independent',
       'Framework :: Django',
       'Topic :: Multimedia :: Graphics',
   ],
   long_description = open(
       os.path.join(os.path.dirname(__file__), 'README.md')
   ).read().strip(),
)