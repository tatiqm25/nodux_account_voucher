# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, json
from frappe import _, scrub, ValidationError
from frappe.utils import flt, comma_or, nowdate
from erpnext.accounts.utils import get_outstanding_invoices, get_account_currency, get_balance_on
from erpnext.accounts.party import get_party_account
from erpnext.accounts.doctype.journal_entry.journal_entry \
	import get_average_exchange_rate, get_default_bank_cash_account
from erpnext.setup.utils import get_exchange_rate
from erpnext.accounts.general_ledger import make_gl_entries

from erpnext.controllers.accounts_controller import AccountsController
from frappe.utils import nowdate

def validate(doc, event):
    validate_bank_accounts(doc)

def validate_bank_accounts(doc):
	if doc.payment_type in ("Pay", "Internal Transfer"):
		for payment_form in doc.payments_type:
			validate_account_type(doc.paid_from, ["Bank", "Cash"])

	if doc.payment_type in ("Receive", "Internal Transfer"):
		for payment_form in doc.payments_type:
			validate_account_type(doc.paid_to, ["Bank", "Cash"])

def validate_account_type(account, account_types):
	account_type = frappe.db.get_value("Account", account, "account_type")
	if account_type not in account_types:
		frappe.throw(_("Account Type for {0} must be {1}").format(account, comma_or(account_types)))

#Asiento Contable
#def generate_accounting(doc):
	#for line in doc.payments_type:
	 # if line.payment_form == "Cash":
	  #  lined = frappe.get_doc({
	   #   "doctype": "Journal Entry Account",
	    #  "account": paid_to,
	     # "debit_in_account_currency":line.amount,
	      #"credit_in_account_currency":0,
	    #})
	    #linec = frappe.get_doc({
	    #  "doctype": "Journal Entry Account",
	    #  "debit_in_account_currency":0,
		  #  "account": paid_from,
	     # "credit_in_account_currency":line.amount
	    #})
	    #journal = frappe.get_doc({
	    #  "doctype":"Journal Entry",
	    #  "voucher_type": "Journal Entry",
	    #  "posting_date": nowdate(),
		#})

	    #journal.append('accounts', lined)
	    #journal.append('accounts', linec)
	    #journal.save()
	    #journal.save()
		#journal.docstatus = 1
	    #self.status = "Done"
	    #self.save()
	  #else:
	   # frappe.throw("Ingrese forma de pago")
