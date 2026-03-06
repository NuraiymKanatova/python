import re
import json

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(text)


prices = re.findall(r"\d[\d ]*,\d{2}", text)
print("Prices found:")
print(prices)

product_names = re.findall(r"\d+\.\n(.+)", text)
print("Products:")
for name in product_names:
    print(name)

datetime_match = re.search(r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}", text)
if datetime_match:
    print("Date and time:")
    print(datetime_match.group())

payment_match = re.search(r"(Банковская карта|Наличные|Карта)", text)
if payment_match:
    print("Payment method:")
    print(payment_match.group())

total_match = re.search(r"ИТОГО:\s*\n(\d[\d ]*,\d{2})", text)
if total_match:
    total_amount = total_match.group(1)
    print("Receipt total:")
    print(total_amount)

def parse_price(price_text):
    return float(price_text.replace(" ", "").replace(",", "."))

if total_match:
    total_number = parse_price(total_match.group(1))
    print("Total as number:")
    print(total_number)


result = {
    "products": product_names,
    "date_time": datetime_match.group() if datetime_match else None,
    "payment_method": payment_match.group() if payment_match else None,
    "total": parse_price(total_match.group(1)) if total_match else None
}

print("\nStructured output:")
print(json.dumps(result, ensure_ascii=False, indent=4))