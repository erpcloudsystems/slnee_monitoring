// Copyright (c) 2016, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Press Monitoring 3"] = {
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
            "label": _("Service Classification"),
            "fieldname": "service_classification",
            "fieldtype": "Link",
            "options": "Service Classification",
            "width": 180
        },
		{
			"fieldname":"agency",
			"label": __("Agency"),
			"fieldtype": "Link",
			"options" : "Agency",
			"reqd": 0
		}
	]
}
