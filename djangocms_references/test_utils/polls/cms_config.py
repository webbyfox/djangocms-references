from cms.app_base import CMSAppConfig

from .models import PollContent


class PollsCMSConfig(CMSAppConfig):
    djangocms_references = True
    reference_fields = {PollContent.poll}