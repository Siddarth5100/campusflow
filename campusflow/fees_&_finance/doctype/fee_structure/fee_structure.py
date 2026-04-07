# Copyright (c) 2026, JC Siddarth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FeeStructure(Document):
	def validate(self):
		# calculate fees
		amount = 0

		for fee in self.fee_component:
			amount += fee.amount
		
		self.total_amount = amount
		
		# negative value
		for value in self.fee_component:
			if value.amount < 0:
				frappe.throw("Amount value should not be in negative")