# -*- coding: utf-8 -*-
# Copyright (c) 2022, Naqeeb khan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ClientSideScripting(Document):
	pass

# thi is how we use server side method using frappy call function....................=== 
@frappe.whitelist()
def frappe_call(msg):
	import time
	time.sleep(5)
	frappe.msgprint(msg)
	# self.mob_no = 778899777
	# return "hi this msg from the frappe_call"