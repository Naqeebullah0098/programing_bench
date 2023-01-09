# -*- coding: utf-8 -*-
# Copyright (c) 2022, Naqeeb khan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ServerSideScripting(Document):
	pass
# ==================this is how we get and set values..================= 

	# def validate(self):
	# 	frappe.msgprint("helo frappe")

	# def validate(self):
	# 	frappe.msgprint(("first name is ={0} ,middle name is ={1} , last name is = {2} and my full name is = {3}").format(self.first_name,self.middle_name,self.last_name,self.first_name + " " + self.middle_name + " " + self.last_name))

	# def validate(self):
	# 	for row in self.get('family_members'):
	# 		frappe.msgprint(("{0} name is = {1} and age is = {2} and relation is {3}").format(row.idx,row.name1,row.age,row.relation))
	
	
	# ================== this is how to get and setvalues...=============
	
	# def validate(self):
	# 	self.get_document()

	# def get_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting',self.client_side_scripting)
	# 	frappe.msgprint(("first name is {0} and age i s={1}").format(doc.first_name,doc.age))

	# 	for r in doc.get('family_members'):
	# 		frappe.msgprint(("{0} name is ={1} and age is ={2} and relation is {3}").format(r.idx,r.name1,r.age,r.relation))


	# ============how to create new doc and delete doc using server side scripting=============

	# def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name = 'ahtesham'
	# 	doc.last_name = 'khan'
	# 	doc.age = 22
	# 	doc.append('family_members',{
	# 		'name1':'asad',
	# 		'age':22,
	# 		'relation':'son'
	# 	})
	# 	doc.insert()
# ===================thi is how to delete doc using server side scripts==========

	# def validate(self):
	# 	frappe.delete_doc('Client Side Scripting', 'pre0002')

# =======this is how we insert new document in database===============

	# def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name= 'sigma'
	# 	doc.age = 46
	# 	doc.insert()

# ==================thi is how we save document================
	# def validate(self):
	# 	self.save()

	# def save(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name= 'sohail'
	# 	doc.age = 46
	# 	doc.save()

# ==============deleting a document first we get the doc then delete it==============
	# def validate(self):
	# 	self.delete_document()

	# def delete_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting', 'pre0003')
	# 	doc.delete()

	# =================updating values in database.............======

	# def validate(self):
	# 	self.set_document()
	# def set_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting','pre0002')
	# 	doc.db_set('age',46)
	# 	doc.db_set('first_name','dolly')



	# =====================thi is how to ge list of documents inside doctype we can also use filters annd fields names for geting specific document

	# def validate(self):
	# 	self.get_list()

	# def get_list(self):
	# 	doc = frappe.db.get_list('Client Side Scripting',
	# 	filters={
	# 		'enable':1,
	# 		# 'first_name':'none',
	# 		# 'age':46
	# 	},
	# 	fields=['first_name','age']) 
	# 	for d in doc:
	# 		frappe.msgprint(("first name is {0} and age is {1}").format(d.first_name,d.age))


	
	# ========================how to get and set value from database======================================
	# syntax # frappe.get_value(doctype, name, field name)  OR  frappe.get_value(doctype,filters,fieldname)
	
	# def validate(self):
	# 	self.get_value()
	# def get_value(self):
	# 	first_name, age = frappe.db.get_value('Client Side Scripting','pre0002',['first_name','age'])
	# 	frappe.msgprint(('first name is {0} and age is {1}').format(first_name,age))


	# =============================how to set values ==================
	# syntax  #   frappe.db.set_value(doctype ,name, field name, value)


	# def validate(self):
	# 	self.set_value()
	# def set_value(self):
	# 	frappe.db.set_value('Client Side Scripting','pre0002','full_name','dolly molly')
	# 	first_name, age ,full_name= frappe.db.get_value('Client Side Scripting','pre0002',['first_name','age','full_name'])
	# 	frappe.msgprint(('first name is {0} and age is {1} and full name is {2}').format(first_name,age,full_name))

	# ======================exists() and count()  ======exists is used for if doctype exists or not   and    count is used for count the docuument inside the doctpe....

	# def validate(self):
	# 	if frappe.db.exists('Client Side Scripting','pre0002'):
	# 		frappe.msgprint('doctype already exist')
	# 	else:
	# 		frappe.msgprint('doctype dosent exist ')


# ===============count()===============================================
# ########### syntax = frappe.db.count(doctype,filters)
	# def validate(self):
	# 	count = frappe.db.count('Client Side Scripting',{'enable':1})
	# 	frappe.msgprint(('the enable documnet count is {0}').format(count))


	# =============this is how to use sql queries in frappe=========
	# 
	
	#======= this is how we call client side function from server side function...........with frm_call()==========
	# def frm_call(self,msg):
	# 	import time
	# 	time.sleep(5)
	# 	self.mob_no = 778899777
	# 	return "hi this msg from the call"


