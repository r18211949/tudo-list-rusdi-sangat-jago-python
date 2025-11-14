tasks = []

def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Lihat tugas")
    print("2. Tambah tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

def show_tasks():
    if not tasks:
        print("\nBelum ada tugas.")
    else:
        print("\nDaftar Tugas:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Masukkan tugas baru: ")
    tasks.append(task)
    print("Tugas ditambahkan!")

def delete_task():
    show_tasks()
    if tasks:
        try:
            index = int(input("Nomor tugas yang mau dihapus: ")) - 1
            removed = tasks.pop(index)
            print(f"Tugas '{removed}' dihapus!")
        except:
            print("Nomor tidak valid.")

while True:
    show_menu()
    choice = input("Pilih menu (1-4): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Keluar...")
        break
    else:
        print("Pilihan tidak valid.")