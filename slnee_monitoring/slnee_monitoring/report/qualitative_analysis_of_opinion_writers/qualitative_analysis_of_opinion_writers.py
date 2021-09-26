# Copyright (c) 2013, erpcloud.systems and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    data = get_data(filters, columns)
    return columns, data


def get_columns():
    return [
		{
			"label": _("Writer"),
			"fieldname": "writer_name",
			"fieldtype": "Link",
			"options": "Writer",
			"width": 180
		},
        {
            "label": _("Journal Name"),
            "fieldname": "journal_name",
            "fieldtype": "Data",
            "width": 180
        },
		{
            "label": _("Service Classification"),
            "fieldname": "service_classification",
            "fieldtype": "Link",
			"options": "Service Classification",
			"width": 180
        },
        {
            "label": _("Content Overall Rating"),
            "fieldname": _("content_overall_rating"),
            "fieldtype": "Data",
            "width": 220
        },
        {
            "label": _("Publish Date"),
            "fieldname": "publish_date",
            "fieldtype": "Date",
            "width": 120
        }
    ]


def get_data(filters, columns):
    item_price_qty_data = []
    item_price_qty_data = get_item_price_qty_data(filters)
    return item_price_qty_data


def get_item_price_qty_data(filters):
    conditions = ""
    if filters.get("from_date"):
        conditions += " and `tabPress Monitoring`.publish_date>=%(from_date)s"
    if filters.get("to_date"):
        conditions += " and `tabPress Monitoring`.publish_date<=%(to_date)s"
    if filters.get("writer"):
        conditions += " and `tabPress Monitoring`.writer =%(writer)s"
    if filters.get("journal_name"):
        conditions += " and `tabPress Monitoring`.journal_name =%(journal_name)s"
    item_results = frappe.db.sql("""
				select
						`tabPress Monitoring`.writer_name as writer_name,
						`tabPress Monitoring`.journal_name as journal_name,
						`tabPress Monitoring`.service_classification as service_classification,
						`tabPress Monitoring`.content_overall_rating as content_overall_rating,
						`tabPress Monitoring`.publish_date as publish_date
						

				from
			    	`tabPress Monitoring`

				where
				`tabPress Monitoring`.docstatus != 2
				{conditions}
				

				ORDER BY `tabPress Monitoring`.name desc

				""".format(conditions=conditions), filters, as_dict=1)

    # price_list_names = list(set([item.price_list_name for item in item_results]))

    # buying_price_map = get_price_map(price_list_names, buying=1)
    # selling_price_map = get_price_map(price_list_names, selling=1)

    result = []
    if item_results:
        for item_dict in item_results:
            data = {
                    'publish_date': item_dict.publish_date,
                    'content_overall_rating': _(item_dict.content_overall_rating),
                    'writer_name': item_dict.writer_name,
                    'service_classification': item_dict.service_classification,
                    'journal_name': item_dict.journal_name,
                    'journal': item_dict.journal,
            }
            result.append(data)

    return result


def get_price_map(price_list_names, buying=0, selling=0):
    price_map = {}

    if not price_list_names:
        return price_map

    rate_key = "Buying Rate" if buying else "Selling Rate"
    price_list_key = "Buying Price List" if buying else "Selling Price List"

    filters = {"name": ("in", price_list_names)}
    if buying:
        filters["buying"] = 1
    else:
        filters["selling"] = 1

    pricing_details = frappe.get_all("Item Price",
                                     fields=["name", "price_list", "price_list_rate"], filters=filters)

    for d in pricing_details:
        name = d["name"]
        price_map[name] = {
            price_list_key: d["price_list"],
            rate_key: d["price_list_rate"]
        }

    return price_map
