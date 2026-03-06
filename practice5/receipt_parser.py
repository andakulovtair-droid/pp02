
import re
from pprint import pprint


# Читаем файл
with open(r"C:\Users\Дамир\OneDrive\Рабочий стол\PP2\practice5/raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# ----------------------------
# 1. Извлечь все цены (итоговые по строкам)
# ----------------------------
price_pattern = r"\n(\d[\d\s]*,\d{2})\nСтоимость"
prices = re.findall(price_pattern, text)

# Убираем пробелы внутри чисел
prices_clean = [float(p.replace(" ", "").replace(",", ".")) for p in prices]

# ----------------------------
# 2. Извлечь названия товаров
# ----------------------------
product_pattern = r"\d+\.\n(.+?)\n\d"
products = re.findall(product_pattern, text, re.DOTALL)

products = [p.strip().replace("\n", " ") for p in products]

# ----------------------------
# 3. Общая сумма
# ----------------------------
total_pattern = r"ИТОГО:\n([\d\s]+,\d{2})"
total_match = re.search(total_pattern, text)
total_amount = float(total_match.group(1).replace(" ", "").replace(",", "."))

# ----------------------------
# 4. Дата и время
# ----------------------------
datetime_pattern = r"Время:\s([\d\.]+\s[\d:]+)"
datetime_match = re.search(datetime_pattern, text)
date_time = datetime_match.group(1)

# ----------------------------
# 5. Способ оплаты
# ----------------------------
payment_pattern = r"(Банковская карта|Наличные)"
payment_match = re.search(payment_pattern, text)
payment_method = payment_match.group(1)

# ----------------------------
# 6. Структурированный вывод
# ----------------------------
receipt_data = {
    "products": products,
    "prices": prices_clean,
    "total": total_amount,
    "date_time": date_time,
    "payment_method": payment_method
}

pprint(receipt_data)
