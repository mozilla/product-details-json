#!/usr/bin/env python
from pathlib import Path

import django
from django.conf import settings
from django.core.management import call_command

from everett.manager import ConfigManager, ConfigEnvFileEnv, ConfigOSEnv


ROOT = Path(__file__).resolve().parent


def path(*paths):
    return str(ROOT.joinpath(*paths))


config = ConfigManager([
    ConfigOSEnv(),
    ConfigEnvFileEnv(path('.env')),
])
settings.configure(
    DEBUG=False,
    PROD_DETAILS_DIR=path('product-details'),
    PROD_DETAILS_URL=config('PROD_DETAILS_URL',
                            default='https://product-details.mozilla.org/1.0/'),
    INSTALLED_APPS=['product_details']
)
django.setup()
call_command('update_product_details')
