

frappe.query_reports["Count Of Service Classification press release  per journal"] = {
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
			"fieldname": "service_classification",
			"label": __("Service Classification"),
			"fieldtype": "Link",
			"options" : "Service Classification",
			"reqd": 0
		}

	]
}

