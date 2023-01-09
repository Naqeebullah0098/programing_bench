# -*- coding: utf-8 -*-
# Copyright (c) 2022, Naqeeb khan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import *
from frappe.model.document import Document

class ChildDoc(Document):
	@frappe.whitelist()
	def list_all_parent_docs(self,doctype):
		data = frappe.get_all(doctype,fields=["*"])

		for d in data:
		
			self.append("parent_list",{
				"full_name":d.full_name,
				"age":d.age
			})
	
	











































	# ======================================================================================================================
	# =====================This is how we Apply Events from server side ==============================================
	# ===================================================================================================================================== 
	# def validate(self):
	# 	frappe.msgprint("helo from validate function event")
	# def before_save(self):
	# 	frappe.throw("helo from before_save function event")
	# def after_insert(self):
	# 		frappe.msgprint("helo from after_insert function event")
	# def after_delete(self):
	# 	frappe.msgprint("are you sure want to delete")	


	# ===========================this is how we get values from table....=======================
	# def validate(self):
	# 	self.get_value()

	# def get_value(self):
	# 	first_name,last_name,age = frappe.db.get_value('Parent Doc','Naqeeb',['first_name','last_name','age'])
	# 	frappe.msgprint(("first name is = {0} and last name = {1} and age is {2}").format(first_name,last_name,age))

	# ===========================this is how we get values from table....=======================
		# def validate(self):
		# 	self.set_value()

		# def set_value(self):
		# 	frappe.db.set_value('Parent Doc','Naqeeb','last_name','Khan')

# ==============================this is how we get entire document========================
		# def validate(self):
		# 	self.get_document()
		# def get_document(self):
		# 	doc =frappe.get_doc('Parent Doc', self.parent_doc_link)
		# 	frappe.msgprint(("The parent full name is {0} {1}").format(doc.full_name,doc.age))


#====================this is how we create docment via client side scripting instead of web view==============
	# def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc = frappe.new_doc('Parent Doc')
	# 	doc.first_name = 'Abdullah'
	# 	doc.last_name = 'khushi'
	# 	doc.age = 23
	# 	doc.save()
# ?==========================================how to delete doc via server side scriptig===========================
	# def validate(self):
	# 	self.delete_document()
	
	# def delete_document(self):
	# 	doc = frappe.get_doc('Child Doc', 'abc')
	# 	doc.delete()
# =========================different documents methods==================

#==============Doc insert method is used for inserting the table into database================== 
	# def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc = frappe.new_doc('Parent Doc')
	# 	doc.first_name = 'Nomi'
	# 	doc.last_name = 'Jee'
	# 	doc.age = 24
	# 	doc.insert()

# ===========this is how we set the values from database===========
	# def validate(self):
	# 	self.db_set_document()

	# def db_set_document(self):
	# 	doc = frappe.get_doc('Parent Doc', 'Naqeeb')
	# 	doc.db_set('age', 45)


# ====================this is how we get entire list of document frm data base by applying filters,,,,,,
	# def validate(self):
	# 	self.get_list()

	# def get_list(self):
	# 	doc = frappe.db.get_list('Parent Doc',
	# 	filters={
	# 		'enable': 1

	# 	},
	# 	fields=['first_name', 'last_name']
	# 	)
	# 	for d in doc :
	# 		frappe.msgprint(("first name is = {0} and last name is {1}").format(d.first_name,d.last_name))

# ================this is how to chk documents by applyig filters========
# frappe.db.count('Doctype','Name')
	# def validate(self):
	# 	doc =frappe.db.count('Parent Doc',{'enable':1 })
	# 	frappe.msgprint(("the enable document count is {0}").format(doc))

# ==============this is how to chk if database exist or NOt...=====================
# frappe.db.exist('Doctype','Name')

	# def validate(self):
	# 	if frappe.db.exists('Parent Doc','Naqeeb'):
	# 		frappe.msgprint('data base exist bro dont worry')
	# 	else:
	# 		frappe.msgprint('bro data base dosent exist')



	# ======================this is how to write sql queries of database with frappy method by this method we can perform CRUD opertaion on databse table============
	# def validate(self):
	# 	self.sql()
	# def sql(self):
	# 	data = frappe.db.sql(""" SELECT first_name,last_name,age FROM `tabParent Doc` WHERE enable = 1 """, as_dict=1)
	# 	for d in data:
	# 		frappe.msgprint(("The Parent First Name is = {0} and the last name is = {1} and age is = {2}").format(d.first_name,d.last_name,d.age))		



	# ====================this is how we set automaticaaly parents data in child data ================
