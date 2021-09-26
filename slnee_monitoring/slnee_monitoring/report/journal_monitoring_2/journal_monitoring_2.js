
frappe.query_reports["Journal Monitoring 2"] = {
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
			"fieldname":"journal",
			"label": __("Journal"),
			"fieldtype": "Link",
			"options" : "Journal",
			"reqd": 0
		}
	]
}

