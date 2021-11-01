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
            "label": _("Agency"),
            "fieldname": "agency_",
            "fieldtype": "Data",
            "width": 125
        },
        {
            "label": _("Overall Tweet Classification"),
            "fieldname": _("overall_tweet_classification"),
            "fieldtype": "Data",
            "width": 140
        },
		{
			"label": _("Tweet Classification"),
			"fieldname": "tweet_classification",
			"fieldtype": "Data",
			"width": 120
		},
        {
            "label": _("Tweet Subject"),
            "fieldname": _("tweet_subject"),
            "fieldtype": "Data",
            "width": 100
        },

        {
            "label": _("Tweet Link"),
            "fieldname": "tweet_link",
            "fieldtype": "Data",
            "width": 200
        }

    ]


def get_data(filters, columns):
    item_price_qty_data = []
    item_price_qty_data = get_item_price_qty_data(filters)
    return item_price_qty_data


def get_item_price_qty_data(filters):
    conditions = ""
    if filters.get("from_date"):
        conditions += " and `tabSocial Media Monitoring`.publish_date>=%(from_date)s"
    if filters.get("to_date"):
        conditions += " and `tabSocial Media Monitoring`.publish_date<=%(to_date)s"
    if filters.get("agency_"):
        conditions += " and `tabSocial Media Monitoring`.agency_ =%(agency_)s"
    item_results = frappe.db.sql("""
				select
						`tabSocial Media Monitoring`.agency_ as agency_,
						`tabSocial Media Monitoring`.overall_tweet_classification as overall_tweet_classification,
						`tabSocial Media Monitoring`.tweet_classification as tweet_classification,
						`tabSocial Media Monitoring`.tweet_subject as tweet_subject,
						`tabSocial Media Monitoring`.tweet_link as tweet_link
						
				from
				`tabSocial Media Monitoring` 
				where
				`tabSocial Media Monitoring`.docstatus != 2
				{conditions}

				ORDER BY `tabSocial Media Monitoring`.agency_ ASC


				""".format(conditions=conditions), filters, as_dict=1)

    # price_list_names = list(set([item.price_list_name for item in item_results]))

    # buying_price_map = get_price_map(price_list_names, buying=1)
    # selling_price_map = get_price_map(price_list_names, selling=1)

    result = []
    if item_results:
        for item_dict in item_results:
            data = {
                'agency_': item_dict.agency_,
                'tweet_classification': item_dict.tweet_classification,
                'tweet_subject': _(item_dict.tweet_subject),
                'overall_tweet_classification': _(item_dict.overall_tweet_classification),
                'tweet_link': item_dict.tweet_link,

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
