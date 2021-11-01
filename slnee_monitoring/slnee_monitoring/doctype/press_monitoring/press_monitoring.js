// Copyright (c) 2021, erpcloud.systems and contributors
// For license information, please see license.txt

frappe.ui.form.on("Press Monitoring","writer_2", function(frm){
    cur_frm.set_value("writer","");
    cur_frm.set_value("news_editor","");
    cur_frm.set_value("writer_name","");

});

frappe.ui.form.on('Press Monitoring', 'writer',  function(frm) {
    if (cur_frm.doc.writer_2 =="كاتب مقال"){

    frappe.call({ method: "frappe.client.get_value",
	args: { doctype: "Writer",
	fieldname: "writer_name",
	filters: { 'name': cur_frm.doc.writer},
	}, callback: function(r)
	{cur_frm.set_value("writer_name", r.message.writer_name);
  } });
        }
});

frappe.ui.form.on('Press Monitoring', 'news_editor',  function(frm) {
  if (cur_frm.doc.writer_2 =="محرر صحفى"){

    frappe.call({ method: "frappe.client.get_value",
    args: { doctype: "News Editor",
    fieldname: "name",
    filters: { 'name': cur_frm.doc.news_editor},
    }, callback: function(r)
    {cur_frm.set_value("writer_name", r.message.name);
  } });
        }
});

frappe.ui.form.on('Press Monitoring', 'validate',  function(frm) {
  if (cur_frm.doc.writer_2 =="لايوجد"){
    cur_frm.set_value("writer_name", cur_frm.doc.writer_2);
  }
});