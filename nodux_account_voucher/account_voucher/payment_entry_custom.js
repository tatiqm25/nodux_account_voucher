// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
{% include "erpnext/public/js/controllers/accounts.js" %}

frappe.ui.form.on('Payment Entry Type', {

	payment_form: function(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		get_payment_mode_account(frm, d.payment_form, function(account){
			frappe.model.set_value(cdt, cdn, 'account', account)
		});
		if(d.payment_form == "Cheque"){
			frappe.model.set_value(cdt, cdn, 'titular', frm.doc.party);
		}
	},

	amount: function(frm) {
		var total_amount = 0.0;
		$.each(frm.doc.payments_type || [], function(i, row) {
				if (row.amount) {
				total_amount += flt(row.amount);
			}
		});
		frm.set_value("paid_amount", total_amount);
	},

	account: function(frm){
		var mound, mode;
		$.each(frm.doc.payments_type || [], function(i, row) {
				if (row.account) {
					mound = row.account;
					mode = row.payment_form;
			}
		});
		if(frm.doc.payment_type == "Receive") {
			frm.set_value("paid_to", mound);
		}else if (frm.doc.payment_type == "Pay") {
			frm.set_value("paid_from", mound);
		}
	},
 // CUANDO SE AGREGUE DOCTYPE BANCO
	// bank:function(frm, cdt, cdn){
	// 	var d = locals[cdt][cdn];
	// 	var nro_account = frappe.db.get_value("Bank", {"bank_name": d.bank.}, "nro_account");
	// 	var nro_document = frappe.db.get_value("Bank", {"bank_name": d.bank}, "nro_document");
	//	frappe.model.set_value(cdt, cdn, 'nro_account', nro_account);
	//	frappe.model.set_value(cdt, cdn, 'nro_document', nro_document);
	// },

	nro_document:function(frm){
		var num_ref;
		$.each(frm.doc.payments_type || [], function(i, row) {
				if (row.nro_document) {
					num_ref = row.nro_document;
			}
		});
		frm.set_value("reference_no", num_ref);
	},

	date_reference:function(frm){
		var date_ref;
		$.each(frm.doc.payments_type || [], function(i, row) {
				if (row.date_reference) {
					date_ref = row.date_reference;
			}
		});
		frm.set_value("reference_date", date_ref);
	}
})
