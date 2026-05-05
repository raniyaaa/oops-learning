class Item:
    def __init__(self, title, id):
        self.title = title
        self.id = id
        self.is_checked_out = False
    def checkout(self):
        if self.is_checked_out == False:
            self.is_checked_out = True
            print(f"{self.title} is checked out")
        else:
            print(f"{self.title} is already checked out")
    def return_item(self):
        if self.is_checked_out == True:
            self.is_checked_out = False
            print(f"{self.title} returned")
    
class Book(Item):
    def get_details(self):
        return f"Book : {self.title} , ID :{self.id}"
    def fine(self, days):
        return days * 3
    

class DVD(Item):
    def get_details(self):
        return f"DVD : {self.title} , ID :{self.id}"
    def fine(self, days):
        return days * 6
    
class Magazine(Item):
    def get_details(self):
        return f"Magazine : {self.title} , ID :{self.id}"
    def fine(self, days):
        return days * 2
class Library:
    def __init__(self):
        self.list = []
    
    def add_item(self, item):
        self.list.append(item)
    
    def search(self, title):
        for item in self.list:
            if title == item.title:
                return item.get_details()
            else:
                return "Not found!"
    
    def show(self):
        for item in self.list:
            if item.is_checked_out:
                print("Status : Not available")
            else:
                print("Status : Available")
            print(item.get_details())


lib = Library()
b1 = Book("Python", 1)
d1 = DVD("Harry Potter", 2)
m1 = Magazine("APJ", 3)

lib.add_item(b1)
lib.add_item(d1)
lib.add_item(m1)

b1.checkout()

lib.show()
b1.return_item()
print("Fine : ", b1.fine(4))
