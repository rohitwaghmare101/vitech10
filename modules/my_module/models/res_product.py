# -*- coding: utf-8 -*-
from os.path import join
import logging
from odoo import models,api,exceptions
EXPORTS_DIR = '/srv/exports'

_logger = logging.getLogger(__name__)

class ProductProduct(models.Model):
	_name = 'product.product'

	@api.model
	def stock_in_location(self,location):
		product_in_loc = self.with_context(
			location=location.id,
			active_test=False
		)

		all_products = product_in_loc.search([])
		stock_levels = []
		for product in all_products:
			if product.qty_available:
				stock_levels.append((product.name,product.qty_available))
		return stock_levels

	@api.model
	def export_stock(self,stock_location):
		products = self.with_context(
			location = stock_location.id
		).search([])
		products = products.filtered('qty_available')
		_logger.debug('%d products in the location',
					  len(products))
		fname = join(EXPORTS_DIR, 'stock_level.txt')
		try:
			with open(fname, 'w') as fobj:
				for prod in products:
					fobj.write('%s\t%f\n' % (prod.name,
											 prod.qty_available))
		except IOError:
			_logger.exception(
				'Error while writing to %s in %s',
				'stock_level.txt', EXPORTS_DIR)
			raise exceptions.UserError('unable to save file')






