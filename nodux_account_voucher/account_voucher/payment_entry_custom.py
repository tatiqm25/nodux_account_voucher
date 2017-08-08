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

def validate(doc, event):
    setup_party_account_field(doc)
    set_missing_values(doc)
    validate_payment_type(doc)
    validate_party_details(doc)
    validate_bank_accounts(doc)
    set_exchange_rate(doc)
    validate_mandatory(doc)
    validate_reference_documents(doc)
    set_amounts(doc)
    clear_unallocated_reference_document_rows(doc)
    validate_payment_against_negative_invoice(doc)
    validate_transaction_reference(doc)
    set_title(doc)
    set_remarks(doc)


def validate_bank_accounts(doc):
	if doc.payment_type in ("Pay", "Internal Transfer"):
		for payment_form in doc.payments_type:
			validate_account_type(doc.mode_of_payment, ["Bank", "Cash"])

    if doc.payment_type in ("Receive", "Internal Transfer"):
    	for payment_form in doc.payments_type:
            validate_account_type(doc.paid_to, ["Bank", "Cash"])

def validate_account_type(account, account_types):
	account_type = frappe.db.get_value("Account", account, "account_type")
	if account_type not in account_types:
		frappe.throw(_("Account Type for {0} must be {1}").format(account, comma_or(account_types)))
