from firebase import Firebase

class Main:
    def __init__(self):
        self.firebase = Firebase()
        self.menu()

    def menu(self):
        while True:
            print(
                "What would you like to do?\n",
                "1. View list\n",
                "2. Add item to list\n",
                "3. Remove item from list\n"
            )
            option = input("Enter the number corrosponding to your selection: ")
            if option not in ["1", "2", "3"]:
                print("\nYou have to pick just the number.")
            else:
                if option == "1":
                    self.view_list()
                elif option == "2":
                    self.add_item()
                elif option == "3":
                    self.remove_item()
    
    def view_list(self):
        data = self.firebase.read()

        if len(self.firebase.data.keys()) == 0:
            print("\nYour to-do list is empty.\n")
            return
        print("\nHere is your to-do list:")

        i = 1
        for key in data.keys():
            if data[key]:
                print(f"{i}. {data[key]}")
                i += 1
        print()

    def add_item(self):
        self.view_list()
        item = input("What would you like to add (cancel to cancel)? ")

        if item.lower() == "cancel":
            return
        
        self.firebase.add(item)
        print(f"\nSuccessfully added {item}\n")

    def remove_item(self):
        self.view_list()
        if len(self.firebase.data.keys()) > 0:
            while True:
                option = input("What would you like to remove (cancel to cancel)? ")

                if option.lower() == "cancel":
                    return
                
                if not self.validate(option, range(1, len(self.firebase.data.keys()))):
                    print("It has to be one of the items.")
                else:
                    self.firebase.remove(int(option))
                    print(f"Successfully removed {option}\n")
                    return
    
    def validate(self, item, allowed):
        try:
            item = int(item)
        except ValueError:
            return False
        return item in allowed


if __name__ == "__main__":
    Main()