// Copyright (c) 2022, Naqeeb khan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Child Doc', {

	get_all_parent_docs: function(frm) {
		frm.call({
			method:'list_all_parent_docs',
			doc: frm.doc,
			args: {
				doctype:"Parent Doc"
			},
			callback: function(r) {
				frappe.msgprint(__("Successfully Updated"))
				frm.refresh_field('parent_list');
			}
		});
	}
});
