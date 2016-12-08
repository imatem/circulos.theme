# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from circulos.theme.testing import CIRCULOS_THEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that circulos.theme is properly installed."""

    layer = CIRCULOS_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if circulos.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'circulos.theme'))

    def test_browserlayer(self):
        """Test that ICirculosThemeLayer is registered."""
        from circulos.theme.interfaces import (
            ICirculosThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(ICirculosThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = CIRCULOS_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['circulos.theme'])

    def test_product_uninstalled(self):
        """Test if circulos.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'circulos.theme'))

    def test_browserlayer_removed(self):
        """Test that ICirculosThemeLayer is removed."""
        from circulos.theme.interfaces import \
            ICirculosThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICirculosThemeLayer, utils.registered_layers())
