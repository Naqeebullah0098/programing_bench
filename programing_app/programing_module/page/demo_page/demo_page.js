frappe.pages['demo-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'None',
		single_column: true
	});

	
// ============================this is how to customize the page =============================


	page.set_title('MY Page')
	page.set_indicator('','red')
	let $btn = page.set_primary_action('New',() => frappe.msgprint("you click new button"),'octicon octicon-plus')
	// var $btnOne = page.set_secondry_action('Refresh',() => frappe.msgprint("you click refresh button"),'octicon octicon-sync')
	let $btnOne = page.set_secondary_action('Refresh', () => frappe.msgprint("you click refresh button"), 'octicon octicon-sync')

	// page.clear_primary_action()
	// add a normal menu item
	// page.add_menu_item('Send Email', () => open_email_dialog())
	page.add_menu_item('Send Email', () => frappe.msgprint("emial send eamail"), true)
	// page.clear_menu()

	// add a normal menu item
	page.add_action_item('Delete', () => frappe.msgprint("delted") )

	// add a normal inner button
	page.add_inner_button('Update Posts', () => frappe.msgprint("post updated"))


	// add a dropdown button in a group
	page.add_inner_button('New Post', () => frappe.msgprint("new post"), 'Make')
	// change type of ungrouped button
	// page.change_inner_button_type('Update Posts', null, 'primary')

	let field = page.add_field({
		label: 'Status',
		fieldtype: 'Select',
		fieldname: 'status',
		options: [
			'Open',
			'Closed',
			'Cancelled'
		],
		change() {
			frappe.msgprint(field.get_value());
		}
	});	

	// $(frappe.render_template("demo_page",{})).appendTo(page.body);

	$(frappe.render_template("demo_page",{
		data:"Frappe user i am render from demo.js"
	})).appendTo(page.body);


}

