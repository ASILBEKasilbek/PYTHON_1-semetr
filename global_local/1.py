# Kontaktlar Kitobi

# Kontaktlar ro'yxati
contacts = []

def add_contact():
    """ Yangi kontakt qo'shish funksiyasi """
    name = input("Ismni kiriting: ")
    phone = input("Telefon raqamini kiriting: ")
    email = input("Email manzilini kiriting: ")
    address = input("Manzilni kiriting: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("\n✅ Kontakt muvaffaqiyatli qo'shildi!\n")

def update_contact():
    """ Kontaktni yangilash funksiyasi """
    search = input("Yangilash uchun kontaktning ismi yoki telefon raqamini kiriting: ")
    for contact in contacts:
        if contact['name'] == search or contact['phone'] == search:
            print("\nKontakt topildi. Yangi ma'lumotlarni kiriting:")
            contact['name'] = input(f"Yangi ism ({contact['name']}): ") or contact['name']
            contact['phone'] = input(f"Yangi telefon raqami ({contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Yangi email manzili ({contact['email']}): ") or contact['email']
            contact['address'] = input(f"Yangi manzil ({contact['address']}): ") or contact['address']
            print("\n✅ Kontakt muvaffaqiyatli yangilandi!\n")
            return
    print("\n❌ Kontakt topilmadi!\n")

def delete_contact():
    """ Kontaktni o'chirish funksiyasi """
    search = input("O'chirish uchun kontaktning ismi yoki telefon raqamini kiriting: ")
    for contact in contacts:
        if contact['name'] == search or contact['phone'] == search:
            contacts.remove(contact)
            print("\n✅ Kontakt muvaffaqiyatli o'chirildi!\n")
            return
    print("\n❌ Kontakt topilmadi!\n")

def search_contact():
    """ Kontaktni qidirish funksiyasi """
    search = input("Qidirish uchun kontaktning ismi yoki telefon raqamini kiriting: ")
    for contact in contacts:
        if contact['name'] == search or contact['phone'] == search:
            print("\n🔍 Kontakt ma'lumotlari:")
            print(f"Ism: {contact['name']}")
            print(f"Telefon: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Manzil: {contact['address']}")
            return
    print("\n❌ Kontakt topilmadi!\n")

def show_all_contacts():
    """ Barcha kontaktlarni ko'rsatish funksiyasi """
    if not contacts:
        print("\n📭 Kontaktlar ro'yxati bo'sh!\n")
    else:
        print("\n📋 Barcha kontaktlar:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Ism: {contact['name']}, Telefon: {contact['phone']}, Email: {contact['email']}, Manzil: {contact['address']}")

def main_menu():
    """ Dastur menyusi """
    while True:
        print("\n===== 📞 Kontaktlar Kitobi =====")
        print("1. Yangi kontakt qo'shish")
        print("2. Kontaktni yangilash")
        print("3. Kontaktni o'chirish")
        print("4. Kontaktni qidirish")
        print("5. Barcha kontaktlarni ko'rsatish")
        print("6. Chiqish")
        
        choice = input("\nTanlang (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            update_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            show_all_contacts()
        elif choice == '6':
            print("\n👋 Dasturdan chiqdingiz. Xayr!\n")
            break
        else:
            print("\n❌ Noto'g'ri tanlov! Iltimos, qaytadan tanlang.\n")

# Dastur ishga tushadi
if __name__ == "__main__":
    main_menu()
