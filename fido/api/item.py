import frappe
from frappe import _

@frappe.whitelist()
def get_item_list(start=0, page_length=20, filters={}, fields=["*"], price_list="Standard Selling", customer=""):
    try:
        items = frappe.db.get_list("Item", filters=filters, fields=fields, start=start, page_length=page_length)
        for item in items:
            price = frappe.db.get_value("Item Price", filters={"item_code": item.name, "selling": 1}, fieldname="price_list_rate")
            item["item_price"] = price if price else 0
        return items
    except Exception as e:
        frappe.throw(_("Something went wrong: {0}").format(str(e)))
