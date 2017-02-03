# This file is part sale_shipments_done module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Sale']
__metaclass__ = PoolMeta


class Sale:
    'Sale'
    __name__ = 'sale.sale'
    shipments_done = fields.Function(fields.Boolean('Delivered'),
        'get_shipments_done')

    @classmethod
    def get_shipments_done(cls, records, name):
        """Get shipments are done"""
        result = {}
        for sale in records:
            done = False
            shipments_done = []
            if sale.shipments:
                for shipment in sale.shipments:
                    if shipment.state == 'done':
                        shipments_done.append(shipment.id)
                if len(shipments_done) == len(sale.shipments):
                    done = True
            result[sale.id] = done
        return result
