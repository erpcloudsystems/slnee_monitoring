
frappe.query_reports["Agency performance indicators"] = {
	"filters": [
		{
			"fieldname": "name",
			"label": __("Agency"),
			"fieldtype": "Link",
			"options" : "Agency",
		},
		{
			"fieldname": "main_classification",
			"label": __("Main Classification"),
			"fieldtype": "Select",
			"options" : ["","بلدية فرعية","أخري","أمانة الرياض"],
		},
		{
			"fieldname": "sub_classification",
			"label": __("Sub Classification"),
			"fieldtype": "Select",
			"options" : ["","أ","ب","ج","د"],
		}

	]
}