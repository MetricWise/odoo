from odoo.modules.module import get_module_resource
from odoo.tests import BaseCase
from odoo.tools.config import configmanager


class TestConfigManager(BaseCase):
    def test_defaults(self):
        config = configmanager()
        self.assertEqual(config['limit_memory_hard'], 2684354560)
        self.assertEqual(config['limit_memory_soft'], 2147483648)

    def test_limit_memory_old(self):
        config = configmanager(fname=get_module_resource('base', 'tests', 'data', 'limit_memory_old.conf'))
        self.assertEqual(config['limit_memory_hard'], 4294967296)
        self.assertEqual(config['limit_memory_soft'], 1073741824)
