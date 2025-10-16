from lib.models.client import Client
from lib.models.project import Project
from lib.models.invoice import Invoice

def main_menu():
    while True:
        print("\n===== Freelance Invoice Tracker =====")
        print("1. Add Client")
        print("2. View Clients")
        print("3. Add Project")
        print("4. View Projects")
        print("5. Create Invoice")
        print("6. View Unpaid Invoices")
        print("7. Mark Invoice as Paid")
        print("8. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Client Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            client = Client(name, email, phone)
            client.save()
            print(f" Client '{name}' added successfully.")

        elif choice == '2':
            clients = Client.get_all()
            for c in clients:
                print(f"[{c.id}] {c.name} - {c.email}")

        elif choice == '3':
            name = input("Project Name: ")
            desc = input("Description: ")
            client_id = input("Client ID: ")
            project = Project(name, desc, client_id)
            project.save()
            print(" Project added.")

        elif choice == '4':
            projects = Project.get_all()
            for p in projects:
                print(f"[{p.id}] {p.name} (Client {p.client_id})")

        elif choice == '5':
            project_id = input("Project ID: ")
            amount = float(input("Amount: "))
            date = input("Issue Date (YYYY-MM-DD): ")
            invoice = Invoice(project_id, amount, date)
            invoice.save()
            print(" Invoice generated.")

        elif choice == '6':
            unpaid = Invoice.get_unpaid()
            for inv in unpaid:
                print(f"[{inv.id}] Project {inv.project_id} - ${inv.amount} - Issued {inv.issue_date}")

        elif choice == '7':
            invoice_id = input("Invoice ID to mark as paid: ")
            Invoice.mark_paid(invoice_id)
            print(" Invoice marked as paid.")

        elif choice == '8':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
