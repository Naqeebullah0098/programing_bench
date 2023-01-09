// Copyright (c) 2022, Naqeeb khan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Client Side Scripting', {
	// this is  how to set the form intro....
// 	refresh: function(frm) {
// 		if(frm.is_new()){frm.set_intro("now you can create your form ")
// 	}
		
// 	},


// 	after_save: function(frm) {
// 		frappe.msgprint(__("The Full name is {0}",[frm.doc.first_name + " " + frm.doc.middle_name + " " + frm.doc.last_name]))
	
// 			for (let row of frm.doc.family_members ){
// 		frappe.msgprint(__("{0} the family member name is {1} and the relation is {2}",[row.idx,row.name1,row.relation]))
// 	}
// 	// 		// for printing simple msg........
// // 		// frappe.msgprint('Helo Frappe user...how are you')


// // 		// for throwing error in page or wants to raise exception.....
// // 		// frappe.throw("Hey Bro i am an error")
// 	}
// ======================thi is how to set values to  child field and parent field======================



	// validate:function(frm) {
	// 	// frm.set_value('full_name',frm.doc.first_name + " " + frm.doc.middle_name + " " + frm.doc.last_name)
	// 	let row = frm.add_child('family_members',{
	// 		name1:'naqeeb',
	// 		age:23,
	// 		relation:'son'
	// 	})
	// }


	// =============this is how to set doctype properties from client side=========================
	
	// enable:function(frm) {
	// 	frm.set_df_property('first_name','reqd',1)
		
	// 	frm.set_df_property('middle_name','read_only',1)

	// 	frm.toggle_reqd('age',true)
	// }



	// ===============adding csustom button via client side scripting====================== using list multiple buttons also
	refresh:function(frm) {

		frm.add_custom_button('Click Me Button',() => {
			frappe.msgprint(__("hey man you click me...!!"));
		})

		frm.add_custom_button('Click Me Button 1',() => {
			frappe.msgprint(__("hey man you click me.1..!!"));
		},'click me')
		frm.add_custom_button('Click Me Button 2',() => {
			frappe.msgprint(__("hey man you click me..2.!!"));
		},'click me')
		frm.add_custom_button('Click Me Button 3',() => {
			frappe.msgprint(__("hey man you click me..3.!!"));
		},'click me')
		
	}


});




// ==============this is child table event ==================

// frappe.ui.form.on('Family Members', {
// 	name1: function(frm) {
// 		frappe.msgprint("helo  i am name event function....")
// 	},
// 	age: function(frm) {
// 		frappe.msgprint("helo  i am name age function....")
// 	}
// 	})
