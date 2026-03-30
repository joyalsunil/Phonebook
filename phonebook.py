import time
import jojofun as jojo

while True:
    
    jojo.loading_animation(21, 5, 0.1, 0.1, "Program started!")

    print("1. Add contact")
    print("2. View contacts")
    print("3. Delete contact")
    print("4. Search contacts")
    print("5. Exit \n")
    print("...............")
    print("...............")

    choice = input("\r\nEnter your choice: ")
    if choice == '1':
        file = open("phonebook.txt", "a")
        print("...............")
        print("...............")
        name = input("\r\nEnter name: ").upper()

        if not name.isalpha():
            jojo.loading_animation(13, 3, 0.4, 0.1, "Name is invalid. Try again!")
            print("...............")
            print("...............")
            print("...............")
            continue

        number = input("\rEnter number: ")
        if not number.isdigit():
            jojo.loading_animation(13, 3, 0.4, 0.1, "Number is invalid.")

            print("\nTry again!\n")
            print("...............")
            print("...............")
            print("...............")
            print("...............")
            continue
        else:
            with open("phonebook.txt", "r") as f:
                contacts = f.readlines()
            found_contacts = [contact for contact in contacts if contact.startswith(number + " ,")]
            if found_contacts:
                print("\nContacts existing:")
                for contact in found_contacts:
                    print(contact.strip()+"\n")
                    print("\nTry again!\n")
                    print("...............")
                    print("...............")
                    print("...............")
                    print("...............")
                    continue
            else:
                file.write(name + " , " + number + "\n")
                file.close()
                jojo.loading_animation(21, 5, 0.4, 0.1, "Number added!")

    elif choice == '2':
        jojo.loading_dots(15, 0.1)
        file = open("phonebook.txt", "r")
        print("\n" + file.read())
        file.close()
    elif choice == '3':
        jojo.loading_dots(15, 0.1)
        file = open("phonebook.txt", "r")
        contacts = file.readlines()
        file.close()

        if not contacts:
            print("Phonebook is empty.")
        else:
            print("Contacts:")
            for contact in contacts:
                print(contact.strip())
            name_to_delete = input("Enter the name of the contact to delete: ").upper()
            with open("phonebook.txt", "w") as file:
                for contact in contacts:
                    if not contact.startswith(name_to_delete + " ,"):
                        file.write(contact)
            jojo.loading_animation(21, 5, 0.4, 0.1, "Contact deleted!")
    elif choice == '4':
        jojo.loading_dots(9, 0.1)
        file = open("phonebook.txt", "r")
        contacts = file.readlines()
        file.close()
        if not contacts:
            jojo.loading_dots(9, 0.1)
            print("\nPhonebook is empty.")
        else:
            jojo.loading_dots(9, 0.1)
            name_to_search = input("\nEnter the name of the contact to search: ").upper()
            found_contacts = [contact for contact in contacts if contact.startswith(name_to_search + " ,")]
            if found_contacts:
                print("\nFound contacts:")
                for contact in found_contacts:
                    print(contact.strip()+"\n")
                time.sleep(2)
            else:
                print("\nContact not found.")
    elif choice == '5':
        jojo.rev_loading_animation(21, 5, 0.4, 0.1, "Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
