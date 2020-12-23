
# Project available in https://repl.it/@lastlost/boilerplate-budget-app#budget.py

class Category :

    def __init__(self, name) :
        self.name = name
        self.ledger = list()

    def deposit(self, amt, des = "") :
        self.ledger.append({"amount": amt, "description": des})

    def withdraw(self, amt, des = "") :
        if self.check_funds(amt) :
            self.ledger.append({"amount": -amt, "description": des})
            return True
        else :
            return False

    def get_balance(self) :
        balance = 0
        for content in self.ledger :
            balance = balance + float(content['amount'])
        return balance

    def transfer(self, amt, category_name) :
        if self.check_funds(float(amt)) :
            self.withdraw(float(amt), 'Transfer to ' + category_name.name)
            category_name.deposit(float(amt), 'Transfer from ' + self.name)
            return True
        elif self.check_funds(float(amt)) < float(amt) :
            return False
    
    def check_funds(self, amt) :
        if self.get_balance() >= float(amt) :
            return True
        elif self.get_balance() < float(amt) :
            return False
    
    def __str__(self) :
        string = self.name.center(30, "*") + "\n"
        for content in self.ledger :
            string = string + f"{content['description'][:23].ljust(23)}"
            string = string + str(format(float(f"{content['amount']}"), '.2f')).rjust(7) + "\n"
        string = string + "Total: " + str(format(float(self.get_balance()), ".2f"))
        return string
    
def create_spend_chart(categories):
    spt = list()
    spt_percent = list()
    cat_name = list()
    for categorie in categories :
        total = 0
        for content in categorie.ledger :
            x = float(content['amount'])
            if x < 0 :
                total = total + (x*(-1))
        spt.append(total)
    for amt in spt :
        x = int((amt/sum(spt)) * 100)
        spt_percent.append(x)
    subten = "100"
    string = "Percentage spent by category\n"
    for puto in range(11) :
        string = string + subten.rjust(3) + "| "
        for percent in spt_percent :
            if percent >= int(subten) :
                string = string + "o  "
            else :
                string = string + "   "
        string = string + "\n"
        if puto != 10 :
            subten = str(int(subten) - 10)
    string = string + "    -"
    for percent in spt_percent :
        string = string + "---"
    string = string + "\n"
    lent  = 0
    for content in categories :
        if len(content.name) > lent :
            lent = len(content.name)
    for content in categories :
        cat_name.append(content.name.ljust(lent))
    letter_num = 0
    for i in range(lent) :
        for name in cat_name :
            if name == cat_name[0] :
                for letter in name :
                    if letter_num == 0 :
                        string = string + "     " + letter + "  "
                        break
                    else :
                        string = string + "     " + name[letter_num] + "  "
                        break
            else :
                for letter in name :
                    if letter_num == 0 :
                        string = string + letter + "  "
                        break
                    else :
                        string = string + name[letter_num] + "  "
                        break
        if i != lent-1 :
            letter_num = letter_num + 1
            string = string + "\n"
    return string
