from django.contrib.auth.models import User
from .models import LADUser, Theme
from django.db.models.signals import post_save
from django.dispatch import receiver



@receiver(post_save, sender = User)
def update_superuser_theme(instance, created, **kwargs):
    if created == True:
        if instance.is_superuser == True:
            lad_user =LADUser(
                user = instance,
                theme = Theme.objects.all().values_list('theme', flat=True)[0]
            )
            lad_user.save()
            print("Assigning theme:{} to superuser by default".format(lad_user.theme))