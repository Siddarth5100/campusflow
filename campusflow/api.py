import frappe

# fetch single record
@frappe.whitelist()
def get_student_summary(student):
    student_summary = frappe.get_doc("Student", student)
   
    return {
        "student_name": student_summary.student_name,
        "program": student_summary.program,
        "gender": student_summary.gender,
        "date_of_birth": student_summary.date_of_birth
    }

# admission count
@frappe.whitelist()
def get_admission_status():
    total = frappe.db.count("Admission Application")
    approved = frappe.db.count("Admission Application", {"status": "Approved"})
    rejected = frappe.db.count("Admission Application", {"status": "Rejected"})
    pending = frappe.db.count("Admission Application", {"status": "Awaiting For Approval"})

    return {
        "total": total,
        "approved": approved,
        "rejected": rejected,
        "pending": pending
    }

# fetch fee structure
@frappe.whitelist()
def get_fee_structure_details(name):
    pass