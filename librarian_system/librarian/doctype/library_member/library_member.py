# Copyright (c) 2023, librarian and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class libraryMember(Document):
	pass
#this method will run every time a document is saved
#enable the read only input

	def before_save(self):
		self.full_name=f'{self.first_name} {self.last_name or""}'


	