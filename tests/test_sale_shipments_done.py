# This file is part of the sale_shipments_done module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SaleShipmentsDoneTestCase(ModuleTestCase):
    'Test Sale Shipments Done module'
    module = 'sale_shipments_done'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleShipmentsDoneTestCase))
    return suite
