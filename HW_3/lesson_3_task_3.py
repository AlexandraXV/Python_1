from address import Address
from mailing import Mailing

to_address = Address(123456, "Москва", "Ленинский проспект", 15, 23)

from_address = Address(678901, "Санкт-Петербург", "Невский проспект", 25, 42)


mailing = Mailing(to_address, from_address, 500, "AB123456789")

print(mailing)
