import phonenumbers
from phonenumbers import geocoder, carrier, timezone
pN = phonenumbers.parse("+15032014741")
#C = carrier.name_for_number(pN, 'en')
tZ= timezone.time_zones_for_number(pN)
R = geocoder.description_for_number(pN, 'en')
#print(C)
print(R, tZ)
