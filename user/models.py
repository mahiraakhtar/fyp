

from django.db import models, migrations
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User


@receiver(post_save)
def init_groups(sender, **kwargs):
    # non staff
    group, created = Group.objects.get_or_create(name='non_staff')
    if created:
        # group.permissions.add(can_read_campaign)
        logger.info('non_staff Group created')
        group.save()


        # assistant
        group, created = Group.objects.get_or_create(name='assistant')
        if created:
            # group.permissions.add(can_edit_users)
            logger.info('assistant Group created')
            group.save()

        # doctor
        group, created = Group.objects.get_or_create(name='doctor')
        if created:
            # group.permissions.add('pateintdetails.view_patient', 'pateintdetails.add_patient', 'pateintdetails.change_patient', 'pateintdetails.delete_patient')
            logger.info('doctor Group created')
            group.save()
