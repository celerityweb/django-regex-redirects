# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def migrate_data(apps, schema_editor):
    OldRedirect = apps.get_model("redirects", "Redirect")
    Redirect = apps.get_model("regex_redirects", "Redirect")
    for old_redirect in OldRedirect.objects.all():
        redirect = Redirect()
        redirect.old_path = old_redirect.old_path
        redirect.new_path = old_redirect.new_path
        redirect.save()

class Migration(migrations.Migration):

    dependencies = [
        ('regex_redirects', '0004_auto_20170512_1349'),
    ]

    operations = [
        migrations.RunPython(migrate_data),
    ]
