frappe.ready(function() {
	// bind events here
	// frappe.web_form.after_load = () => {
	// 	frappe.msgprint("please fill all the values before saving")
	// };


	// this is how we perorm actiopns  on fields....when we enable it....

	// frappe.web_form.after_load = () => {
	// 	frappe.web_form.on('enable',(field,value)=> {
	// 		frappe.msgprint("Hi frappe user....")
	// 	})
	// };

// this is how 
	frappe.web_form.after_load = () => {
		frappe.web_form.on('first_name',(field,value)=> {
			frappe.msgprint("Hi frappe user..lmnopq..")
		})
	};

										// frappe.web_form.after_load = () => {
										// frappe.web_form.set_value([age], [13])
										// };
	
	// frappe.web_form.set_value([age], [13])

	frappe.web_form.on('dob',(field,value) => {
		if (value) {
			dob = new Date(value);
			var today = new Date();
			var age = Math.floor((today - dob) / (365.25 * 24 * 60 * 60 ));
			frappe.web_form.set_value("age",[age])

		}
	});
	


})