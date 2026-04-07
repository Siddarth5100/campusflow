# Copyright (c) 2026, JC Siddarth and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AdmissionApplication(Document):
	def validate(self):
		# mobile num validation, father field
		if self.father_number:
			if len(self.father_number) != 10:
				frappe.throw("Enter exactly 10 numbers")
				
		# check is it only number, father field
		if self.father_number:
			for num in self.father_number:
				if not num.isdigit():
					frappe.throw("Enter only numbers")

		# mobile num validation, mother field
		if self.mother_number:
			if len(self.mother_number) != 10:
				frappe.throw("Enter exactly 10 numbers")
		
		# check is it only number, mother field
		if self.mother_number:
			for num in self.mother_number:
				if not num.isdigit():
					frappe.throw("Enter only numbers")

		# mobile num, validation, guardian
		if self.guardian_mobile_number:
			if len(self.guardian_mobile_number) != 10:
				frappe.throw("Enter exactly 10 numbers")

		# admission type
		if self.admission_type == "Boarder":
			if not self.guardian_name:
				frappe.throw("If Boarder, Guardian details mandatory")
			
	def on_update(self):
		if self.status in ["Approved", "Rejected"]:
			frappe.enqueue(
				"campusflow.utils.send_admission_status",
				docname=self.name,
				queue="short"
			)
			