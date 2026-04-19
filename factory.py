class SGB:
    def buy(self, amount):
        return f"Purchased {amount} units of SGB"

class ETF:
    def buy(self, amount):
        return f"Purchased {amount} shares of ETF"




class InvFactory:
    @staticmethod
    def get_investment(asset):
        if asset == "SGB":
            return SGB()
        
        elif asset == "ETF":
            return ETF()
        else:
            raise ValueError("Unknown asset")

factory = InvFactory()
my_asset = factory.get_investment("SGB")
print(my_asset.buy(100))
        
        
#Factory - we dont want to define objects again n again for different classess. we create a class that handles the logic of which object is created for which class by returning the class as its object is instanciated.