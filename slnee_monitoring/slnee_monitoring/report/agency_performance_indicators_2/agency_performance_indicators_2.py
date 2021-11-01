# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
from frappe import _


def execute(filters=None):
	columns = get_columns()
	data = []

	service_classification = frappe.db.get_all("Press Monitoring", filters=filters, fields=["service_classification"])
	for s in service_classification:


		data = frappe.db.get_all("Agency", filters={"name":filters.get("name")}, fields=["name", "main_classification", "sub_classification"])
		#press_monitoring = {}
		for press_monitoring in data:
			press_monitoring["agency"] = press_monitoring.name
			press_monitoring["positive"] = frappe.db.count("Press Monitoring", filters={"agency": press_monitoring.name, "service_classification": s[0][0], "content_overall_rating": "Positive"})
			press_monitoring["neutral"] = frappe.db.count("Press Monitoring", filters={"agency": press_monitoring.name, "service_classification": s[0][0], "content_overall_rating": "Neutral"})
			press_monitoring["negative"] = frappe.db.count("Press Monitoring", filters={"agency": press_monitoring.name, "service_classification": s[0][0], "content_overall_rating": "Negative"})

			chart = get_chart_data(data)
			report_summary = get_report_summary(data)

		return columns, data, None, chart, report_summary

def get_columns():
	return [
		{
			"label": _("Agency"),
			"fieldname": "agency",
			"fieldtype": "Link",
			"options": "Agency",
			"width": 250
		},
		{
			"label": _("Positive"),
			"fieldname": "positive",
			"fieldtype": "Int",
			"width": 180
		},

		{
			"label": _("Neutral"),
			"fieldname": "neutral",
			"fieldtype": "Int",
			"width": 180
		},
		{
			"label": _("Negative"),
			"fieldname": "negative",
			"fieldtype": "Int",
			"width": 180
		}
	]

def get_chart_data(data):
	labels = []
	positive = []
	neutral = []
	negative = []

	for press_monitoring in data:
		labels.append(press_monitoring.agency)
		positive.append(press_monitoring.positive)
		neutral.append(press_monitoring.neutral)
		negative.append(press_monitoring.negative)

	return {
		"data": {
			'labels': labels[:30],
			'datasets': [
				{
					"name": "Positive",
					"values": positive[:30]
				},
				{
					"name": "Neutral",
					"values": neutral[:30]
				},
				{
					"name": "Negative",
					"values": negative[:30]
				},
			]
		},
		"type": "bar",
		"colors": ["green", "blue", "red"],
		"barOptions": {
			"stacked": False
		}
	}

def get_report_summary(data):
	if not data:
		return None



	return [

	]