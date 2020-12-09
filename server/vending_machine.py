
class VendingMachine:
    """
        Vending Machine Object to manage the stock
    """

    def __init__(self):
        self.stock = {}
        self.inserted_money = 0

    def load_stock(self, data):
        """
            Loads the json data into the stock. 
        """
        print("--> Loading the json")
        if len(data) < 3:
            return False

        self.stock = {}

        for item in data:
            self.stock[item['name']] = {"stock": item["stock"], "price": item["price"]}

        return True

    def get_items(self):
        """
            Retrive all existing items
        """
        result = []
        for name in self.stock.keys():
            result.append({"name": name, "stock": self.stock[name]["stock"], "price": self.stock[name]["price"]})
        return result

    def get_item(self, item_name):
        """
            Getting the item based on the inserted money
        """
        print(f"--> Get item: {item_name}")
        item = self.stock.get(item_name)
        if item:
            if item["stock"] > 0 and self.inserted_money >= item["price"]:
                item["stock"] = item["stock"] - 1
                self.inserted_money -= item["price"]
                return item_name, True
        else:
            return item_name, False
    
    def insert_money(self, amount):
        """
            Insert money
        """
        print(f"--> Inserting money: {amount}")
        if self.inserted_money + int(amount) < 100:
            self.inserted_money += int(amount)
            return self.inserted_money
        return 0