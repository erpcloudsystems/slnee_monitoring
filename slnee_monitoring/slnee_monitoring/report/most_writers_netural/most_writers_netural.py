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
            "label": _("Writer 2"),
            "fieldname": "writer_2",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": _("Writer / Editor Name"),
            "fieldname": "writer_name",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": _("Journal Name"),
            "fieldname": "Journal_name",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": _("Number of Neutral Press"),
            "fieldname": "number_of_neutral_press",
            "fieldtype": "Int",
            "width": 180
        },

    ]


def get_data(filters, columns):
    item_price_qty_data = []
    item_price_qty_data = get_item_price_qty_data(filters)
    return item_price_qty_data


def get_item_price_qty_data(filters):
    conditions = ""
    if filters.get("from_date"):
        conditions += " and a.publish_date>=%(from_date)s"
    if filters.get("to_date"):
        conditions += " and a.publish_date<=%(to_date)s"
    if filters.get("writer_2"):
        conditions += " and a.writer_2 =%(writer_2)s"
    if filters.get("writer"):
        conditions += " and a.writer =%(writer)s"
    if filters.get("news_editor"):
        conditions += " and a.news_editor =%(news_editor)s"
    item_results = frappe.db.sql("""
				select distinct
                        a.writer_2 as writer_2,
						a.writer_name as writer_name,
						a.Journal_name as Journal_name,
						(select count(name) from `tabPress Monitoring` w where w.content_overall_rating ='Neutral' and a.writer = w.writer and a.Journal_name = w.Journal_name {conditions} ) as number_of_neutral_press
				from
				`tabPress Monitoring` a

				where
				(select count(name) from `tabPress Monitoring` w where w.content_overall_rating ='Neutral' and a.writer = w.writer and a.Journal_name = w.Journal_name {conditions} ) > 0
				and
				a.docstatus != 2
				{conditions}
				ORDER BY number_of_neutral_press DESC;

				""".format(conditions=conditions), filters, as_dict=1)

    # price_list_names = list(set([item.price_list_name for item in item_results]))

    # buying_price_map = get_price_map(price_list_names, buying=1)
    # selling_price_map = get_price_map(price_list_names, selling=1)

    result = []
    if item_results:
        for item_dict in item_results:
            data = {
                'name': item_dict.name,
                'workflow_state': _(item_dict.workflow_state),
                'publish_date': item_dict.publish_date,
                'content_item': _(item_dict.content_item),
                'content_overall_rating': _(item_dict.content_overall_rating),
                'count_of_press_release': item_dict.count_of_press_release,
                'articles': item_dict.articles,
                'article': item_dict.article,
                'study': item_dict.study,
                'Journal_name': item_dict.Journal_name,
                'number_of_negative_press': item_dict.number_of_negative_press,
                'number_of_positive_press': item_dict.number_of_positive_press,
                'number_of_neutral_press': item_dict.number_of_neutral_press,
                'url': item_dict.url,
                'writer_name': item_dict.writer_name,
                'writer': item_dict.writer,
                'agency': item_dict.agency,
                'creation': item_dict.creation,
                'service_classification': item_dict.service_classification,
                'full_name': item_dict.full_name,
                'writer_2': item_dict.writer_2
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
