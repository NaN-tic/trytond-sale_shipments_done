# This file is part sale_shipments_done module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Sale']


class Sale:
    __metaclass__ = PoolMeta
    __name__ = 'sale.sale'
    shipments_done = fields.Function(fields.Boolean('Delivered'),
        'get_shipments_done')

    @classmethod
    def get_shipments_done(cls, records, name):
        """Get shipments are done"""
        result = {}
        done = False
        shipment_done = []
        shipment_total = []
        for sale in records:
            if sale.shipments:
                for shipment in sale.shipments:
                    if shipment.effective_date != 'None':
                        shipment_total.append(shipment.id)
                    if shipment.state == 'done':
                        shipment_done.append(shipment.id)
                if len(shipment_done) == len(shipment_total):
                    done = True
            result[sale.id] = done
        return result

