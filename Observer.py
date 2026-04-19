class Customer:
    def __init__(self, name):
        self.name = name
        
    # Every customer needs a way to receive the message
    def read_text(self, product):
        print(f"{self.name} checks phone. {product} is in stock!")


class Store:
    def __init__(self):
        self.contacts = []
        
    def sign_up(self, customer):
        self.contacts.append(customer)
        
    def restock_item(self, product):
        print(f"\n--- Store Manager: We just got a shipment of {product}s! ---")
        
        # 3. THE CORE LOGIC: Loop through the list and text everyone
        for person in self.contacts:
            person.read_text(product)


if __name__ == "__main__":
    # Create the store and a couple of customers
    st = Store()
    alice = Customer("Alice")
    arjun = Customer("Arjun")

    # The customers write their names on the store's clipboard
    st.sign_up(alice)
    st.sign_up(arjun)

    # A month later, the store gets a new item.
    # The store automatically texts Alice and Arjun without us having to do it manually.
    st.restock_item("PlayStation 5")