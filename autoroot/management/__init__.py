from django.db.models.signals import post_syncdb

from django.contrib.auth.models import User


def create_superuser(app, created_models, **kwargs):
        from django.conf import settings
        if getattr(settings, 'AUTOROOT_DEBUG_ONLY', True) and not settings.DEBUG:
            return
        su_name = getattr(settings, 'AUTOROOT_USER', 'root')
        su_email = getattr(settings, 'AUTOROOT_EMAIL', 'root@example.com')
        su_pass = getattr(settings, 'AUTOROOT_PASSWORD', 'qqq')
        try:
            User.objects.get(username=su_name)
        except User.DoesNotExist:
            User.objects.create_superuser(su_name, su_email, su_pass)
            print "Superuser created (%s:%s:%s)" % (su_name, su_email, su_pass)

post_syncdb.connect(create_superuser, sender=None)
