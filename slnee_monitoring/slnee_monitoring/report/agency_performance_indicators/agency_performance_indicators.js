// Copyright (c) 2016, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Agency performance indicators"] = {
	"filters": [
	{
			"label": _("agency"),
			"fieldname": "agency",
			"fieldtype": "Link",
			"options": "Agency",
			"width": 180
	}

	]
};
