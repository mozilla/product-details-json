#!/usr/bin/env python
import sys
from pathlib import Path

import django
from django.conf import settings
from django.core.management import call_command

from everett.manager import ConfigManager, ConfigEnvFileEnv, ConfigOSEnv


ROOT = Path(__file__).resolve().parent
FIREFOX_VERSION_KEYS = (
    'FIREFOX_NIGHTLY',
    'FIREFOX_AURORA',
    'FIREFOX_ESR',
    'FIREFOX_ESR_NEXT',
    'LATEST_FIREFOX_DEVEL_VERSION',
    'LATEST_FIREFOX_RELEASED_DEVEL_VERSION',
    'LATEST_FIREFOX_VERSION',
)
# so far p-d only lists builds for the latest version
# bedrock uses the locales for the release channel to
# build download pages for the other channels
THUNDERBIRD_VERSION_KEYS = (
    'LATEST_THUNDERBIRD_VERSION',
)


def path(*paths):
    return str(ROOT.joinpath(*paths))


def update_data():
    call_command('update_product_details', force=True)


def count_thunderbird_builds(version_key, min_builds=20):
    version = pd.thunderbird_versions[version_key]
    builds = len([locale for locale, build in pd.thunderbird_primary_builds.items()
                  if version in build])
    if builds < min_builds:
        raise ValueError('Too few builds for {}'.format(version_key))


def count_firefox_builds(version_key, min_builds=20):
    version = pd.firefox_versions[version_key]
    if not version:
        if version_key == 'FIREFOX_ESR_NEXT':
            return
    builds = len([locale for locale, build in pd.firefox_primary_builds.items()
                  if version in build])
    if builds < min_builds:
        raise ValueError('Too few builds for {}'.format(version_key))


def validate_data():
    for key in FIREFOX_VERSION_KEYS:
        count_firefox_builds(key)

    for key in THUNDERBIRD_VERSION_KEYS:
        count_thunderbird_builds(key)


# setup and run

config = ConfigManager([ConfigOSEnv(),
                        ConfigEnvFileEnv(path('.env'))])
settings.configure(
    DEBUG=False,
    PROD_DETAILS_DIR=path('product-details'),
    PROD_DETAILS_URL=config('PROD_DETAILS_URL',
                            default='https://product-details.mozilla.org/1.0/'),
    PROD_DETAILS_STORAGE='product_details.storage.PDFileStorage',
    INSTALLED_APPS=['product_details'],
    # disable cache
    CACHES={'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache'}},
)
django.setup()

from product_details import product_details as pd  # noqa

if __name__ == '__main__':
    update_data()
    try:
        validate_data()
    except Exception as e:
        sys.exit('Product Details data is not valid: {}'.format(e))
