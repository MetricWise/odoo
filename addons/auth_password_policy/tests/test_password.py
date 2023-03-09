# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests import BaseCase, new_test_pass


class TestPassword(BaseCase):
    def test_new_test_pass(self):
        password1 = new_test_pass(self.env, 'admin')
        password2 = new_test_pass(self.env, 'admin')
        self.assertEqual(password1, password2)
        self.env['res.users']._check_password_policy([password1])
