from random import randrange, randint

class Bank:
    atm_count = 1
    atm_numbers = []
    money_count = 0
    bill_value = [100, 50, 20, 10, 5, 2, 1]
    __max_atm_bill = 1400
    def __init__(self, atm, money):
        self.money = money
        Bank.money_count = self.money

        self.bill = []
        for i in Bank.bill_value:
            self.bill.append(Bill(i))

        self.atm = []
        for i in range (atm):
            self.atm.append(ATM())
            for n in self.bill:
                n.amount -= 100

        print('You create new Bank. It has', len (Bank.atm_numbers), 'ATM and', money, 'dollars on its account')


    def addATM (self):
        self.atm.append(ATM())
        for n in self.bill:
            n.amount -= 100
        print('You add new ATM and its number is', Bank.atm_numbers[-1], '. By default it gets', self.atm[-1].money_sum, 'dollars from the main department')


    def delATM (self, num_of_atm):
        n = 0
        b = 0
        for i in range(len(Bank.atm_numbers)):
            if Bank.atm_numbers[i] == num_of_atm:
                n = i
                b += 1

        if b == 0:
            print("You couldn't delete the ATM. There is no ATM with №", num_of_atm, "in the Bank")
        else:
            for i in self.atm:
                if i is self.atm[n]:
                    pass
                else:
                    for j in range (len(self.atm[n].bill_value)):
                        if (Bank.__max_atm_bill - i.bill_sum - self.atm[n].bill_amount[j]) > 0:
                            i.bill_amount[j] += self.atm[n].bill_amount[j]
                            i.bill_sum += self.atm[n].bill_amount[j]
                            i.money_amount[j] += self.atm[n].bill_amount[j] * self.atm[n].bill_value[j]
                            i.money_sum += self.atm[n].bill_amount[j] * self.atm[n].bill_value[j]
                            self.atm[n].bill_sum -= self.atm[n].bill_amount[j]
                            self.atm[n].money_amount[j] -= self.atm[n].bill_amount[j] * self.atm[n].bill_value[j]
                            self.atm[n].money_sum -= self.atm[n].bill_amount[j] * self.atm[n].bill_value[j]
                            self.atm[n].bill_amount[j] = 0

                    if (Bank.__max_atm_bill - i.bill_sum) == 0:
                        pass

                    else:
                        for y in range (len(self.atm[n].bill_value)):
                            if self.atm[n].bill_sum > 0 and self.atm[n].bill_amount[y] > 0:
                                i.bill_amount[y] += Bank.__max_atm_bill - i.bill_sum
                                i.money_amount[y] += self.atm[n].bill_amount[y] * self.atm[n].bill_value[y]
                                i.money_sum += self.atm[n].bill_amount[y] * self.atm[n].bill_value[y]
                                self.atm[n].bill_amount[y] -= Bank.__max_atm_bill - i.bill_sum
                                i.bill_sum = Bank.__max_atm_bill
                                self.atm[n].bill_sum -= self.atm[n].bill_amount[y]
                                self.atm[n].money_amount[y] -= self.atm[n].bill_amount[y] * self.atm[n].bill_value[y]
                                self.atm[n].money_sum -= self.atm[n].bill_amount[y] * self.atm[n].bill_value[y]

            for h in range (len(self.atm[n].bill_value)):
                if self.atm[n].bill_amount[h] > 0:
                    self.bill[h].amount += self.atm[n].bill_amount[h]
                    self.atm[n].bill_sum -= self.atm[n].bill_amount[h]
                    self.atm[n].money_amount[h] -= self.atm[n].bill_amount[h] * self.atm[n].bill_value[h]
                    self.atm[n].money_sum -= self.atm[n].bill_amount[h] * self.atm[n].bill_value[h]
                    self.atm[n].bill_amount[h] = 0

            self.atm_numbers.remove(num_of_atm)
            self.atm.pop(n)
            print('ATM №', num_of_atm, 'has been successfully deleted')



    def ATM_amount_of_money (self, num_of_atm):
        for i in range(len(Bank.atm_numbers)):
            if Bank.atm_numbers[i] == num_of_atm:
                return (print ('ATM №', num_of_atm, 'contains', self.atm[i].money_sum, 'dollars'))
            elif i == len (Bank.atm_numbers) - 1:
                print('There is no ATM with №', num_of_atm)
            else:
                pass



    def addMoney_to_ATM (self, amount):
        n = randint (0, len (self.atm))
        a = amount
        c = 0
        d = 0

        for i in self.atm:
            if i.bill_sum == Bank.__max_atm_bill:
                c += 1

            if (Bank.__max_atm_bill - i.bill_sum) * max(i.bill_value) < a:
                d += 1

        if c == len (self.atm) or d == len (self.atm):
            print('There are no one atm to add money in. All ATMs are full')
            pass
        else:
            b = 0
            while self.atm[n].bill_sum == Bank.__max_atm_bill and (Bank.__max_atm_bill - self.atm[n].bill_sum * max(self.atm[n].bill_value)) < a:
                b = randint(0, len(self.atm))
                while b == n:
                    b = randint(0, len(self.atm))
                n = b

            print('ATM №', self.atm[n].number, 'is chosen. Now it contains', self.atm[n].money_sum, 'dollars')

            for w in range (len(self.atm[n].bill_value)):
                if a >= self.atm[n].bill_value[w]:
                    self.atm[n].bill_amount[w] += int (a / self.atm[n].bill_value[w])
                    self.atm[n].bill_sum += int (a / self.atm[n].bill_value[w])
                    self.atm[n].money_amount[w] += int (a / self.atm[n].bill_value[w]) * self.atm[n].bill_value[w]
                    self.atm[n].money_sum += int (a / self.atm[n].bill_value[w]) * self.atm[n].bill_value[w]
                    self.money += int (a / self.atm[n].bill_value[w]) * self.atm[n].bill_value[w]
                    a -= int (a / self.atm[n].bill_value[w]) * self.atm[n].bill_value[w]

            print('After add operation ATM №', self.atm[n].number, 'contains', self.atm[n].money_sum, 'dollars')


    def getMoney (self, amount, num_ATM = 0): #If input has only one argument (amount of money), you will get money from the main department (not from ATM).
        a = amount
        w = 0
        for o in self.atm:
            w += o.money_sum

        if num_ATM == 0:
            if a < self.money - w:
                for s in range(len(self.bill)):
                    if a >= self.bill[s].value:
                        self.bill[s].amount -= int (a / self.bill[s].value)
                        self.money -= int (a / self.bill[s].value) * self.bill[s].value
                        a -= int (a / self.bill[s].value) * self.bill[s].value
                print('You successfully receive', amount, 'dollars out of the Bank')
            else:
                print('There is no enough money in the Bank')

        elif num_ATM > 0:
            n = 0
            b = 0
            for i in range(len(Bank.atm_numbers)):
                if Bank.atm_numbers[i] == num_ATM:
                    n = i
                    b += 1

            if b == 0:
                print('There is no ATM with №', num_ATM)
            else:
                if a < self.atm[n].money_sum:
                    for u in range (len(self.atm[n].bill_value)):
                        if a >= self.atm[n].bill_value[u]:
                            self.atm[n].bill_amount[u] -= int (a / self.atm[n].bill_value[u])
                            self.atm[n].bill_sum -= int(a / self.atm[n].bill_value[u])
                            self.atm[n].money_amount[u] -= int (a / self.atm[n].bill_value[u]) * self.atm[n].bill_value[u]
                            self.atm[n].money_sum -= int (a / self.atm[n].bill_value[u]) * self.atm[n].bill_value[u]
                            self.money -= int (a / self.atm[n].bill_value[u]) * self.atm[n].bill_value[u]
                            a -= int (a / self.atm[n].bill_value[u]) * self.atm[n].bill_value[u]
                    print('You successfully receive', amount, ' dollars out of ATM №', num_ATM)
                else:
                    print('There is no enough money in chosen ATM. Please, pick another ATM or get your money from the main bank department')

        else:
            pass



class ATM:
    def __init__(self):
        self.number = Bank.atm_count
        Bank.atm_numbers.append(self.number)
        Bank.atm_count += 1
        self.bill_value = Bank.bill_value
        self.bill_amount = []
        for i in range (len (self.bill_value)):
            self.bill_amount.append(100)
        self.bill_sum = sum (self.bill_amount)
        self.money_amount = []
        for i in range (len (self.bill_value)):
            self.money_amount.append(self.bill_value[i] * self.bill_amount[i])
        self.money_sum = sum (self.money_amount)



class Bill:
    def __init__(self, bill_value):
        self.value = bill_value
        if Bank.money_count >= self.value:
            self.amount = randrange (int (Bank.money_count / self.value))
            Bank.money_count -= self.value * self.amount
        else:
            self.amount = 0

        if Bank.money_count > 0 and bill_value == 1:
            self.amount += Bank.money_count
            Bank.money_count = 0
        else:
            pass
