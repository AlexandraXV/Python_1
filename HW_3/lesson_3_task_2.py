from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Samsung", "Galaxy S22 Ultra", "+79123456789"))
catalog.append(Smartphone("Apple", "iPhone 13 Pro Max", "+79987654321"))
catalog.append(Smartphone("Xiaomi", "Mi 12S Ultra", "+79012345678"))
catalog.append(Smartphone("OnePlus", "10 Pro", "+79876543210"))
catalog.append(Smartphone("Realme", "GT Neo 3", "+79112233445"))

for phone in catalog:
    phone.sayInfo()
