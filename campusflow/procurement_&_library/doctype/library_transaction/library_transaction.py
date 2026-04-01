# Copyright (c) 2026, JC Siddarth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibraryTransaction(Document):
	def validate(self):
		frappe.msgprint("Testing")

		# validate books already issued or not
		if self.transaction_type == "Issue":
			count = frappe.db.count("Library Transaction", {
				"student": self.student,
				"transaction_type": "Issue"
			})

			print("-------------------",self.student)

			if count >= 3:
				frappe.throw("User already holding books")

				