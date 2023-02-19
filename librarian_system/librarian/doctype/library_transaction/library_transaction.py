# Copyright (c) 2023, librarian and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryTransaction(Document):
    #before submitting validate the issue and return article
    def before_submit(self):
        if self.type=="Issue":
            self.validate_issue()
            self.validate_maximum_limit()
            #set the status to issued
            article=frappe.get_doc("Article",self.article)
            article.status="issued"
            article.save()
        
        elif self.type=="Return":
            self.validate_return()
            #set the status to availabe
            article=frappe.get_doc("Article",self.article)
            article.status="available"
            article.save()

    #validate the issue
    def validate_issue(self):
        self.validate_membership()
        article=frappe.get_doc("Article",self.article)

        if article.status=="issued":
            frappe.throw("Article is issued with another member")

    #Validate the returnment of the article
    def validate_return(self):
        article=frappe.get_doc("Article",self.article)

        if article.status=="available":
               frappe.throw("Article can not be issued before it is issued first")
    #validate number of issues
    def validate_maximum_limit(slef):
        article=frappe.get_single_value("Library Settings","max_articles")
        count=frappe.db.count(
            "Library Transaction",
            {
                "library_member":self.library_member,"type":"issue","docstatus":DocStatus.submitted()
            },
        )
        if count >= max_articles:
            frappe.throw("Maximum limit reached for issuing articles")           

    #Validate membership
    def validate_membership(self):
        valid_membership=frappe.db.exists(
            "Library Membership",
            {
                "library_member":self.library_member,
                "docstatus":DocStatus.submitted(),
                "from_date":("<",self.date),
                "to_date":(">",self.date),


            },
        )		
        if not valid_membership:
            frappe.throw("The member does not have a valid membership")


