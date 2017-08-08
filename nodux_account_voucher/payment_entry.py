# # -*- coding: utf-8 -*-
# # Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# # For license information, please see license.txt
# from __future__ import unicode_literals
# import frappe, json
# from frappe import _, scrub, ValidationError
# from frappe.utils import flt, comma_or, nowdate
# from erpnext.accounts.utils import get_outstanding_invoices, get_account_currency, get_balance_on
# from erpnext.accounts.party import get_party_account
# from erpnext.accounts.doctype.journal_entry.journal_entry \
# 	import get_average_exchange_rate, get_default_bank_cash_account
# from erpnext.setup.utils import get_exchange_rate
# from erpnext.accounts.general_ledger import make_gl_entries
#
# from erpnext.controllers.accounts_controller import AccountsController
#
# def validate_bank_accounts(self):
# 	if self.payment_type in ("Pay", "Internal Transfer"):
# 		for payment_form in self.payments_type:
# 			validate_account_type(payment_form, ["Bank", "Cash"])
#
#
# 	if self.payment_type in ("Receive", "Internal Transfer"):
# 		for payment_form in self.payments_type:
# 			validate_account_type(payments_type, ["Bank", "Cash"])
#
# def validate_account_type(account, account_types):
# 	account_type = frappe.db.get_value("Account", account, "account_type")
# 	print "Cuuuuenta tipo",account_type
# 	if account_type not in account_types:
# 		print "INGRESO"
# 		frappe.throw(_("Account Type for {0} must be {1}").format(account, comma_or(account_types)))
