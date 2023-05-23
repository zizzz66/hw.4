
class SavingAccount():
    pass
class CheckingAccount():
    pass
class Stock():
    pass
class Bond():
    pass
class Security(Stock, Bond):
    pass
class BankAccount(SavingAccount, CheckingAccount):
    pass
class RealEstate():
     pass
class Asset(BankAccount, RealEstate, Security):
    pass
class InterestBearingitem(BankAccount, Security):
    pass
class InsurableItem(BankAccount, RealEstate):
    pass