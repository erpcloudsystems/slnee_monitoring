// Copyright (c) 2016, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Most writers Netural"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.defaults.get_user_default("year_start_date"),
			"reqd": 1
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.defaults.get_user_default("year_end_date"),
			"reqd": 1
		},

		{
			"fieldname":"writer_2",
			"label": __("Writer 2"),
			"fieldtype": "Select",
			"options" : ["","لايوجد","كاتب مقال","محرر صحفى"],
			"reqd": 0
		},

		{
			"fieldname":"writer",
			"label": __("Writer"),
			"fieldtype": "Link",
			"options" : "Writer",
			"reqd": 0
		},
		{
			"fieldname":"news_editor",
			"label": __("News Editor"),
			"fieldtype": "Link",
			"options" : "News Editor",
			"reqd": 0
		}
	]
}
