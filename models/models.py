# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
	_inherit = 'sale.order'

	is_read = fields.Boolean('Is Read', copy=False, default=False)

	def read(self, fields=None, load='_classic_read'):
		result = super(SaleOrder, self).read(fields, load=load)
		if self and len(self) == 1 and 'is_read' in fields:
			self.is_read = True
		return result
