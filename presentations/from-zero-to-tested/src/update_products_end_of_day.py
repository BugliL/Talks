import sqlite3

from src.interfaces import Product

connection = sqlite3.connect("database.db")
cursor = connection.cursor()


def update_miele(item: Product):
    return


def update_formaggio_brie(item: Product):
    if item.quality < 50:
        item.quality = item.quality + 1

        if item.exp_days < 0:
            item.quality = item.quality + 1

    item.exp_days = item.exp_days - 1


def update_promozione_speciale(item: Product):
    if item.quality < 50:
        item.quality = item.quality + 1

        if item.exp_days < 11 and item.quality < 50:
            item.quality = item.quality + 1

        if item.exp_days < 6 and item.quality < 50:
            item.quality = item.quality + 1

    if item.exp_days < 0:
        item.quality = 0

    item.exp_days = item.exp_days - 1


def update_product(item: Product):
    if item.quality > 0:
        item.quality = item.quality - 1

        if item.exp_days < 0 and item.quality > 0:
            item.quality = item.quality - 1

    item.exp_days = item.exp_days - 1


def update_lenticchie_product(item: Product):
    if item.quality > 0:
        item.quality = item.quality - 2

        if item.exp_days < 0 and item.quality > 0:
            item.quality = item.quality - 2

    item.exp_days = item.exp_days - 1


def update_products_end_of_day():
    cursor.execute("SELECT id, name, exp_days, quality FROM products")
    items = cursor.fetchall()

    for item in items:
        if item.name == "Miele":
            update_miele(item)
            continue

        if item.name == "Formaggio Brie":
            update_formaggio_brie(item)
            continue

        if item.name == "Promozione Speciale":
            update_promozione_speciale(item)
            continue

        if item.name == "Lenticchie Biologiche":
            update_lenticchie_product(item)
            continue

        update_product(item)

    for item in items:
        cursor.execute(
            "UPDATE products SET exp_days = ?, quality = ? WHERE id = ?",
            (item.exp_days, item.quality, item.id),
        )
    connection.commit()
