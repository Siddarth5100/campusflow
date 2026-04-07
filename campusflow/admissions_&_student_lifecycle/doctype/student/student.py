# Copyright (c) 2026, JC Siddarth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Student(Document):
	def validate(self):
		# check is already student got registered in student doctype
		if frappe.db.exists("Student", 
			{"student_name": self.student_name}
		):
		
			frappe.throw("Student already exist")

		