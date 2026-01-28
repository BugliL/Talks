from datetime import datetime
import sqlite3
import smtplib

email_server = smtplib.SMTP('localhost', 1025)
total_amount = 0.0
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

def process_supplier_invoices():
    global connection, cursor, total_amount, email_server
    cursor.execute("SELECT * FROM supplier_invoices WHERE status != 'PROCESSED'")
    invoices = cursor.fetchall()
    total_amount = 0.0
    urgent_count = 0; vip_discount = 0; report_text = ""
    
    for inv in invoices:
        if inv[8] == 1:  # Fattura urgente
            cursor.execute("UPDATE supplier_invoices SET priority = 'HIGH' WHERE id = " + str(inv[0]))
            if inv[4] > 5000:  # Importo alto
                cursor.execute("SELECT vip_status FROM suppliers WHERE id = " + str(inv[2]))
                supplier = cursor.fetchone()
                if supplier and supplier[0] == 1:  # Fornitore VIP
                    discounted = inv[5] * 0.98
                    vip_discount += inv[5] - discounted
                    total_amount += discounted
                    query = str(inv[0]) + ", " + str(vip_discount) + ", '" + str(datetime.now()) + "'"
                    cursor.execute("INSERT INTO vip_discounts VALUES (" + query + ")")
            else:
                total_amount += inv[5]
        else:
            total_amount += inv[5]
            
        cursor.execute("UPDATE supplier_invoices SET status = 'PROCESSED' WHERE id = " + str(inv[0]))
    
    final_report = "FATTURE FORNITORI " + str(datetime.now().day) + "/" + str(datetime.now().month) + "\n"
    email_server.sendmail("finance@acme.com", "finance@acme.com", final_report)
    f = open("/tmp/suppliers_" + str(datetime.now().date()) + ".txt", "w")
    f.write(final_report)
    f.close()
    connection.commit()
    
    if urgent_count > 5:
        return False, "TROPPI URGENTI", urgent_count
    else:
        return True, final_report, total_amount