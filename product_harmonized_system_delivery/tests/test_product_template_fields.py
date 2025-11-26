from odoo.addons.product_harmonized_system.tests.test_product_harmonized_system import (
    TestProductHarmonizedSystem,
)


class TestProductTemplateFields(TestProductHarmonizedSystem):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_product_template_field_values(self):
        """Verifies that custom fields overwrite Odoo fields"""
        self.assertEqual(
            self.product_tmpl.hs_code, self.HS1.hs_code, "HS code mismatch"
        )
        self.assertEqual(
            self.product_tmpl.country_of_origin,
            self.country,
            "Country of origin mismatch",
        )
