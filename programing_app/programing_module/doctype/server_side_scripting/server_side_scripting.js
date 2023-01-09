// Copyright (c) 2022, Naqeeb khan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Server Side Scripting', {

	enable: function(frm) {
		frappe.call({
			
			method: "programing_app.programing_module.doctype.client_side_scripting.client_side_scripting.frappe_call",
			args: {
				msg: "hello"
			},
			freeze: true,
			freeze_message: __('Calling frappe_call Method'),
			callback: function(r) {
				frappe.msgprint(r.message)
			}
		});
	}

	// refresh: function(frm) {
		// this is how wwe call function using from serverside of cliets side function/////
	// enable: function(frm){
	// 	frm.call({
	// 		doc: frm.doc,
	// 		method: 'frm_call',
	// 		args: {
	// 			msg: 'hello'
	// 		},
	// 		freeze: true,
	// 		freeze_message: __('Calling frm _call Method'),
	// 		callback: function(r) {
	// 			frappe.msgprint(r.message)
	// 		}
	// 	});
	// }
	// }


});
