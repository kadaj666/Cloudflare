from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class CloudflareConfig(AppConfig):
    name = 'pluginmanager.plugins.cloudflare'

    class PluginMeta:
        name = _("cloudflare")
        author = _("alex")
        version = "0.0.1"
        category = "provider"
        description = _("cloudflare provider plugin")
        api_url = _("https://www.cloudflare.com/api/")
        url = _("https://www.cloudflare.com/")
        logo_letters = _("CF")
        logo_collor = _("amber-10")
        compatibility = []

    