// Copyright (c) 2016, erpcloud.systems and contributors
// For license information, please see license.txt
/* eslint-disable */
frappe.query_reports["Agency performance indicators 2"] = {
	"filters": [
		{
			"fieldname": "name",
			"label": __("Agency"),
			"fieldtype": "Link",
			"options" : "Agency",
		},
		{
			"fieldname": "service_classification",
			"label": __("Service Classification"),
			"fieldtype": "Link",
			"options" : "Service Classification",
		},
		{
			"fieldname": "main_classification",
			"label": __("Main Classification"),
			"fieldtype": "Select",
			"options" : ["","بلدية فرعية","أخري"],
		},
		{
			"fieldname": "sub_classification",
			"label": __("Sub Classification"),
			"fieldtype": "Select",
			"options" : ["","أ","ب","ج","د"],
		}

	]
}