// Copyright (c) 2026, JC Siddarth and contributors
// For license information, please see license.txt

frappe.ui.form.on("Attendance", {
    setup(frm) {
        frm.set_query("student", "attendance_detail", function(doc, cdt, cdn) {
            return {
                filters: {
                    program: doc.grade
                }
            };
        });
    }
});