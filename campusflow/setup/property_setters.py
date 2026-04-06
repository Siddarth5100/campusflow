import frappe

def create_property_setters():
    # admission doctype override status to read_only
    frappe.make_property_setter({
        "doctype": "Admission Application",
        "fieldname": "status",
        "property": "read_only",
        "value": "1",
        "property_type": "Check"
    }),

    # student doctype override
    frappe.make_property_setter({
        "doctype": "Student",
        "fieldname": "program",
        "property": "label",
        "value": "Grade"
    })