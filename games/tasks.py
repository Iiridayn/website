import logging
from celery import task
from reversion.models import Version
from django.contrib.contenttypes.models import ContentType
from games import models

LOGGER = logging.getLogger(__name__)

@task
def delete_unchanged_forks():
    """Periodically delete forked installers that haven't received any changes"""
    for installer in models.Installer.objects.abandoned():
        installer.delete()

@task
def clear_orphan_revisions():
    """Deletes revisions that are no longer associated with an installer"""
    content_type = ContentType.objects.get_for_model(models.Installer)
    for version in Version.objects.filter(content_type=content_type):
        if version.object:
            continue
        LOGGER.warning("Deleting orphan version %s", version)
        version.delete()
