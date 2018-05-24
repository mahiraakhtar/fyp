from django.contrib.auth.models import Group, Permission

non_staff, created = Group.objects.get_or_create(name='non_staff')

#permission = Permission.objects.get('patientdetails.view_patient')

#non_staff.permissions.add('patientdetails.view_patient')