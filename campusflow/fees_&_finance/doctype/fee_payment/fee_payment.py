# Copyright (c) 2026, JC Siddarth and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FeePayment(Document):
	def validate(self):
		total = 0

		for row in self.payment_breakdown:
			total += row.amount

		self.total_amount = total

	