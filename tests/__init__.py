# This file is part sale_shipments_done module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
try:
    from trytond.modules.sale_shipments_done.tests.test_sale_shipments_done import suite
except ImportError:
    from .test_sale_shipments_done import suite

__all__ = ['suite']
