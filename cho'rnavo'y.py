from re import match , findall
tel=input("Tel raqamingizni kiriting:")
andoza1="^9........"
andoza2="^33......."
andoza3="^77......."
andoza4="^88......."
if match(andoza1, tel) or match(andoza1, tel) or match(andoza1, tel) or match(andoza1, tel):
    print("Qabul qilindi!")
else:
    print("Raqam noto'g'ri formatda kiritildi!")
andoza_url="https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"
matn="Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI "
#Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"

url=findall(andoza_url, matn)
print(url)
