import frappe
from frappe.utils import today
import time

# send admission notifications using bg job
def send_admission_status(docname):
    admission_app = frappe.get_doc("Admission Application", docname)

    if admission_app.status == "Approved":
        frappe.msgprint(f"Mail function called for {admission_app.status}")
        frappe.sendmail(
            recipients=[admission_app.email],
            subject="School Admission Application Status",
            message=f"Hello, {admission_app.father_name} your son/daughter {admission_app.student_name}'s School Admission status = {admission_app.status}"
        )

    elif admission_app.status == "Rejected":
        frappe.msgprint(f"Mail function called for {admission_app.status}")
        frappe.sendmail(
            recipients=[admission_app.email],
            subject="School Admission Application Status",
            message=f"Hello, {admission_app.father_name} your son/daughter {admission_app.student_name}'s School Admission status = {admission_app.status}"
        )

# scheduler job
def admission_application_status():
    admission_application = frappe.get_all(
        "Admission Application",
        fields=['status', 'email'],
        filters={'status': 'Pending Approval'}
    )

    count = len(admission_application)

    return count