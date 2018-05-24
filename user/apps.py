from django.apps import AppConfig
from django.contrib.auth.models import User, Group, Permission

new_group, created = Group.objects.get_or_create(name='non_staff')
assistant, created = Group.objects.get_or_create(name='assistant')
doctor, created = Group.objects.get_or_create(name='doctor')

def add_to_default_group(sender, **kwargs):
    user = kwargs["instance"]


    if kwargs["created"]:
        group = Group.objects.get(name='non_staff')
        user.groups.add(group)

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

class UserConfig(AppConfig):
    name = 'user'
    post_save.connect(add_to_default_group, sender=User)
    post_save.connect(init_groups, sender=User)

