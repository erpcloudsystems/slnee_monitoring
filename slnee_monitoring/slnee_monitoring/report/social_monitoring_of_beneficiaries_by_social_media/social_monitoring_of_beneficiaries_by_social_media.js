// Copyright (c) 2016, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Social monitoring of beneficiaries by social media"] = {
	"filters": [

		{
			"fieldname":"agency_",
			"label": __("Agency"),
			"fieldtype": "Link",
			"options" : "Agency",
			"reqd": 0
		}
	]
}


