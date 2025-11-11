import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()


def update_products_end_of_day():
    cursor.execute("SELECT id, name, exp_days, quality FROM products")
    items = cursor.fetchall()
    for item in items:
        if item.name == "Miele":
            continue

        if (
            item.name not in ["Formaggio Brie", "Promozione Speciale", "Miele"]
            and item.quality > 0
        ):
            item.quality = item.quality - 1

        if item.name == "Formaggio Brie" and item.quality < 50:
            item.quality = item.quality + 1

            if item.exp_days < 0:
                item.quality = item.quality + 1

        if item.name == "Promozione Speciale" and item.quality < 50:
            item.quality = item.quality + 1

            if item.exp_days < 11 and item.quality < 50:
                item.quality = item.quality + 1

            if item.exp_days < 6 and item.quality < 50:
                item.quality = item.quality + 1

        if item.name == "Promozione Speciale" and item.exp_days < 0:
            item.quality = 0

        if item.exp_days < 0 and item.name != "Formaggio Brie":
            if item.name != "Promozione Speciale":
                if item.quality > 0:
                    item.quality = item.quality - 1

        item.exp_days = item.exp_days - 1

    for item in items:
        cursor.execute(
            "UPDATE products SET exp_days = ?, quality = ? WHERE id = ?",
            (item.exp_days, item.quality, item.id),
        )
    connection.commit()
