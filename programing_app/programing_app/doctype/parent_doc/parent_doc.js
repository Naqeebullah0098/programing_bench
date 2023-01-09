// Copyright (c) 2022, Naqeeb khan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Parent Doc', {
	// refresh: function(frm) {
	// 	frappe.msgprint(("Helo How Are You..! You Are In Parent Doc Right Now with refresh function"))

	// },
	// onload: function(frm) {
	// 	frappe.msgprint(("Helo How Are You..! You Are In Parent Doc Right Now  with onload function"))

	// },
	// validate: function(frm) {
	// 	frappe.msgprint(("Helo How Are You..! You Are In Parent Doc Right Now with validate function"))

	// },
	// age: function(frm) {
	// // 	frappe.msgprint(("Helo How Are You..! You Are In Parent Doc Right Now with age function"))
		

	// },
	// last_name: function(frm) {
	// 	frappe.msgprint(("Helo How Are You..! You Are In Parent Doc Right Now with email function"))

	// },
	// before_save: function(frm) {
	// 	frappe.msgprint(("Helo How Are You..! You Are In Parent Doc Right Now with before save function"))

	// }
	// enable: function(frm) {
	// 	frappe.msgprint(("Helo How Are You..! You Are In Parent Doc Right Now with validate function"))

	// },
	// email: function(frm) {
	// 	frappe.msgprint(("Helo How Are You..! You Are In Parent Doc Right Now with validate function"))

	// }
	// after_cancel: function(frm) {
	// 	frappe.msgprint(("Helo How Are You..! You Are In Parent Doc Right Now with after cancel function"))

	// }

	// ===============this is how we show our field data into event=============
// =========for custom notification box=======
	// refresh:function(frm){
	// 	frappe.msgprint({
	// 		title:__("Notificaion"),
	// 		indicator:'red',
	// 		message:__('Hello hi bye bye')
	// 	});
	// },

	// refresh:function(frm){
	// 	if(frm.is_new()){
	// 		frm.set_intro("Now you can Create new Doctype here......")
	// 	}
	// },

	// validate:function(frm){
	// 	frm.set_value("full_name",frm.doc.first_name + " " + frm.doc.last_name)
	// },

	// // ==========================this is how to get data in dialog box from user==========
	// refresh:function(frm){
	// 	if(frm.is_new()){
	// 		let d = new frappe.ui.Dialog({
	// 			title: "Enter some parent details here first",
	// 			indicator:'red',
	// 				fields:[{
	// 				label: "First_Name",
	// 				fieldname:'first_name',
	// 				fieldtype:'Data'
	// 			},
	// 			{
	// 				label: "Last_Name",
	// 				fieldname:'last_name',
	// 				fieldtype:'Data'
	// 			},
	// 			{
	// 				label: "Age",
	// 				fieldname:'age',
	// 				fieldtype:'Data'
	// 			}],
	// 			primary_action_label:'submit',
	// 			primary_action(values){
	// 				frm.set_value('first_name', values.first_name)
	// 				frm.set_value('last_name', values.last_name)
	// 				frm.set_value('age', values.age)
	// 			d.hide()
	// 			}	
	// 		});
	// 		d.show(); 
	// 	}
	// },
	// enable:function(frm){
	// 	if(frm.is_dirty()){
	// 		frappe.msgprint(__("please save document before save"))
	// 	}
	// },
	// // =====For drop down Buttons=====
	// refresh:function(frm){
	// 	// ==============for single button========

	// 	frm.add_custom_button('click Me',() =>{
	// 		frappe.msgprint(__("yoou click  "));
	// 	})
	// 	// ===========singlr button end=====
	// 	frm.add_custom_button('click me 1',() =>{
	// 		frappe.msgprint(__("yoou click 1 "));
	// 	},"click Me")
	// 	frm.add_custom_button('click me 2',() =>{
	// 		frappe.msgprint(__("yoou click 2 "));
	// 	},"click Me")
	// }

	// ===============this is how we can call another function from function========
	// refresh:function(frm){
	// 	if(!frm.is_new()){
	// 		frm.trigger('test');
	// 	}
	// },
	// test:function(frm){
	// 	frappe.msgprint("test function is trigered");
	// }
	enable:function(frm){
		let rwo = frm.add_child('date_and_values',{
			date:'01/02/2022',
			value_1: 10,
			value_2: 20,
		})
		frm.refresh_field('date_and_values')
	}


});
