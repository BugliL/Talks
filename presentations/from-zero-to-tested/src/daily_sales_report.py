
def daily_sales_report():
    global connection, cursor, total_sales, yesterday_date, email_server
    cursor.execute("SELECT * FROM sales WHERE date = '" + str(datetime.now().date()) + "'")
    sales = cursor.fetchall()
    total_sales = 0.0
    cash_sales = 0; card_sales = 0; discount_amount = 0
    report_text = ""
    cursor.execute("SELECT COUNT(*) FROM customers WHERE active = 1")
    active_customers = cursor.fetchone()[0]
    
    for s in sales:
        total_sales += s[3]
        report_text = report_text + "Vendita ID: " + str(s[0]) + " - "
        if s[4] == 1:
            cursor.execute("UPDATE customer_stats SET visits = visits + 1 WHERE id = " + str(s[7]))
            if s[5] > 100:
                report_text = report_text + "GRANDE ACQUISTO - "
                if s[6] == "VIP":
                    cash_sales += s[3] * 0.9
                    discount_amount += s[3] * 0.1
                    report_text = report_text + "VIP SCONTO 10% - "
                else:
                    cash_sales += s[3]
                    report_text = report_text + "NORMALE - "
            else:
                cash_sales += s[3]
                report_text = report_text + "PICCOLO - "
        else:
            report_text = report_text + "CARTA - "
            if s[5] > 50:
                card_sales += s[3] * 0.95
                discount_amount += s[3] * 0.05
                cursor.execute("INSERT INTO promotions_used VALUES (" + str(s[0]) + ", 'CARD_DISCOUNT', '" + str(datetime.now()) + "')")
                report_text = report_text + "SCONTO CARTA 5% - "
            else:
                card_sales += s[3]
        report_text = report_text + "€" + str(s[3]) + "\n"
    
    report_text = "ACME CORP - " + "REPORT " + "VENDITE " + "DEL " + str(datetime.now().day) + "/" + str(datetime.now().month) + "/" + str(datetime.now().year) + " alle " + str(datetime.now().hour) + ":" + str(datetime.now().minute) + "\n" + "=" * 50 + "\n" + report_text + "=" * 50 + "\n"
    report_text = report_text + "TOTALE" + ": " + "€" + str(total_sales) + "\n"
    report_text = report_text + "CONTANTI" + ": " + "€" + str(cash_sales) + "\n" 
    report_text = report_text + "CARTE" + ": " + "€" + str(card_sales) + "\n"
    report_text = report_text + "SCONTI" + ": " + "€" + str(discount_amount) + "\n"
    report_text = report_text + "CLIENTI" + " " + "ATTIVI" + ": " + str(active_customers) + "\n"
    
    email_server.sendmail("manager@acme.com", report_text)
    cursor.execute("INSERT INTO email_log VALUES ('" + str(datetime.now()) + "', 'manager@acme.com', 'REPORT_SENT')")
    f = open("/tmp/sales_" + str(datetime.now().date()) + ".txt", "w")
    f.write(report_text)
    f.close()
    cursor.execute("UPDATE stats SET last_report = '" + str(datetime.now()) + "'")
    cursor.execute("UPDATE stats SET total_reports = total_reports + 1")
    connection.commit()
    
    if total_sales > 1000:
        cursor.execute("INSERT INTO achievements VALUES ('HIGH_SALES', '" + str(datetime.now().date()) + "')")
        connection.commit()
        return True, report_text, total_sales
    else:
        return False, report_text