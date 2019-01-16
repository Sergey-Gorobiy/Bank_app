from random import randrange, randint

class Bank:
    atm_count = 1
    atm_numbers = []
    __max_atm_bill = 1400
    def __init__(self, atm, money):
        self.money = Money (money)
        self.atm = []
        for i in range (1, atm + 1):
            self.atm.append(ATM())
            Money.cashToATM(self.money)
        print('You create new Bank. It has', len (Bank.atm_numbers), 'ATM and', money, 'dollars on its account')


    def addATM (self):
        self.atm.append(ATM())
        Money.cashToATM(self.money)
        print('You add new ATM and its number is', Bank.atm_numbers[-1], '. By default it gets', self.atm[-1].amount, 'dollars from the main department')


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
                    if (Bank.__max_atm_bill - i.bill_sum - self.atm[n].bill_100_dol) > 0:
                        i.bill_100_dol += self.atm[n].bill_100_dol
                        i.bill_sum += self.atm[n].bill_100_dol
                        i.amount += self.atm[n].bill_100_dol * 100
                        self.atm[n].bill_sum -= self.atm[n].bill_100_dol
                        self.atm[n].bill_100_dol = 0

                    if (Bank.__max_atm_bill - i.bill_sum - self.atm[n].bill_50_dol) > 0:
                        i.bill_50_dol += self.atm[n].bill_50_dol
                        i.bill_sum += self.atm[n].bill_50_dol
                        i.amount += self.atm[n].bill_50_dol * 50
                        self.atm[n].bill_sum -= self.atm[n].bill_50_dol
                        self.atm[n].bill_50_dol = 0

                    if (Bank.__max_atm_bill - i.bill_sum - self.atm[n].bill_20_dol) > 0:
                        i.bill_20_dol += self.atm[n].bill_20_dol
                        i.bill_sum += self.atm[n].bill_20_dol
                        i.amount += self.atm[n].bill_20_dol * 20
                        self.atm[n].bill_sum -= self.atm[n].bill_20_dol
                        self.atm[n].bill_20_dol = 0

                    if (Bank.__max_atm_bill - i.bill_sum - self.atm[n].bill_10_dol) > 0:
                        i.bill_10_dol += self.atm[n].bill_10_dol
                        i.bill_sum += self.atm[n].bill_10_dol
                        i.amount += self.atm[n].bill_10_dol * 10
                        self.atm[n].bill_sum -= self.atm[n].bill_10_dol
                        self.atm[n].bill_10_dol = 0

                    if (Bank.__max_atm_bill - i.bill_sum - self.atm[n].bill_5_dol) > 0:
                        i.bill_5_dol += self.atm[n].bill_5_dol
                        i.bill_sum += self.atm[n].bill_5_dol
                        i.amount += self.atm[n].bill_5_dol * 5
                        self.atm[n].bill_sum -= self.atm[n].bill_5_dol
                        self.atm[n].bill_5_dol = 0

                    if (Bank.__max_atm_bill - i.bill_sum - self.atm[n].bill_2_dol) > 0:
                        i.bill_2_dol += self.atm[n].bill_2_dol
                        i.bill_sum += self.atm[n].bill_2_dol
                        i.amount += self.atm[n].bill_2_dol * 2
                        self.atm[n].bill_sum -= self.atm[n].bill_2_dol
                        self.atm[n].bill_2_dol = 0

                    if (Bank.__max_atm_bill - i.bill_sum - self.atm[n].bill_1_dol) > 0:
                        i.bill_1_dol += self.atm[n].bill_1_dol
                        i.bill_sum += self.atm[n].bill_1_dol
                        i.amount += self.atm[n].bill_1_dol
                        self.atm[n].bill_sum -= self.atm[n].bill_1_dol
                        self.atm[n].bill_1_dol = 0

                    if (Bank.__max_atm_bill - i.bill_sum) == 0:
                        pass

                    elif self.atm[n].bill_sum > 0 and self.atm[n].bill_100_dol > 0:
                        i.bill_100_dol += Bank.__max_atm_bill - i.bill_sum
                        i.amount += (Bank.__max_atm_bill - i.bill_sum) * 100
                        self.atm[n].bill_100_dol -= Bank.__max_atm_bill - i.bill_sum
                        i.bill_sum = Bank.__max_atm_bill
                        self.atm[n].bill_sum -= self.atm[n].bill_100_dol

                    elif self.atm[n].bill_sum > 0 and self.atm[n].bill_50_dol > 0:
                        i.bill_50_dol += Bank.__max_atm_bill - i.bill_sum
                        i.amount += (Bank.__max_atm_bill - i.bill_sum) * 50
                        self.atm[n].bill_50_dol -= Bank.__max_atm_bill - i.bill_sum
                        i.bill_sum = Bank.__max_atm_bill
                        self.atm[n].bill_sum -= self.atm[n].bill_50_dol

                    elif self.atm[n].bill_sum > 0 and self.atm[n].bill_20_dol > 0:
                        i.bill_20_dol += Bank.__max_atm_bill - i.bill_sum
                        i.amount += (Bank.__max_atm_bill - i.bill_sum) * 20
                        self.atm[n].bill_20_dol -= Bank.__max_atm_bill - i.bill_sum
                        i.bill_sum = Bank.__max_atm_bill
                        self.atm[n].bill_sum -= self.atm[n].bill_20_dol

                    elif self.atm[n].bill_sum > 0 and self.atm[n].bill_10_dol > 0:
                        i.bill_10_dol += Bank.__max_atm_bill - i.bill_sum
                        i.amount += (Bank.__max_atm_bill - i.bill_sum) * 10
                        self.atm[n].bill_10_dol -= Bank.__max_atm_bill - i.bill_sum
                        i.bill_sum = Bank.__max_atm_bill
                        self.atm[n].bill_sum -= self.atm[n].bill_10_dol

                    elif self.atm[n].bill_sum > 0 and self.atm[n].bill_5_dol > 0:
                        i.bill_5_dol += Bank.__max_atm_bill - i.bill_sum
                        i.amount += (Bank.__max_atm_bill - i.bill_sum) * 5
                        self.atm[n].bill_5_dol -= Bank.__max_atm_bill - i.bill_sum
                        i.bill_sum = Bank.__max_atm_bill
                        self.atm[n].bill_sum -= self.atm[n].bill_5_dol

                    elif self.atm[n].bill_sum > 0 and self.atm[n].bill_2_dol > 0:
                        i.bill_2_dol += Bank.__max_atm_bill - i.bill_sum
                        i.amount += (Bank.__max_atm_bill - i.bill_sum) * 2
                        self.atm[n].bill_2_dol -= Bank.__max_atm_bill - i.bill_sum
                        i.bill_sum = Bank.__max_atm_bill
                        self.atm[n].bill_sum -= self.atm[n].bill_2_dol

                    elif self.atm[n].bill_sum > 0 and self.atm[n].bill_1_dol > 0:
                        i.bill_1_dol += Bank.__max_atm_bill - i.bill_sum
                        i.amount += (Bank.__max_atm_bill - i.bill_sum)
                        self.atm[n].bill_1_dol -= Bank.__max_atm_bill - i.bill_sum
                        i.bill_sum = Bank.__max_atm_bill
                        self.atm[n].bill_sum -= self.atm[n].bill_1_dol

                    else:
                        pass

            if self.atm[n].bill_100_dol > 0:
                self.money.bill_100_dol += self.atm[n].bill_100_dol
                self.atm[n].bill_100_dol = 0
                self.atm[n].bill_sum -= self.atm[n].bill_100_dol

            if self.atm[n].bill_50_dol > 0:
                self.money.bill_50_dol += self.atm[n].bill_50_dol
                self.atm[n].bill_50_dol = 0
                self.atm[n].bill_sum -= self.atm[n].bill_50_dol

            if self.atm[n].bill_20_dol > 0:
                self.money.bill_20_dol += self.atm[n].bill_20_dol
                self.atm[n].bill_20_dol = 0
                self.atm[n].bill_sum -= self.atm[n].bill_20_dol

            if self.atm[n].bill_10_dol > 0:
                self.money.bill_10_dol += self.atm[n].bill_10_dol
                self.atm[n].bill_10_dol = 0
                self.atm[n].bill_sum -= self.atm[n].bill_10_dol

            if self.atm[n].bill_5_dol > 0:
                self.money.bill_5_dol += self.atm[n].bill_5_dol
                self.atm[n].bill_5_dol = 0
                self.atm[n].bill_sum -= self.atm[n].bill_5_dol

            if self.atm[n].bill_2_dol > 0:
                self.money.bill_2_dol += self.atm[n].bill_2_dol
                self.atm[n].bill_2_dol = 0
                self.atm[n].bill_sum -= self.atm[n].bill_2_dol

            if self.atm[n].bill_1_dol > 0:
                self.money.bill_1_dol += self.atm[n].bill_1_dol
                self.atm[n].bill_1_dol = 0
                self.atm[n].bill_sum -= self.atm[n].bill_1_dol

            self.atm_numbers.remove(num_of_atm)
            self.atm.pop(n)
            print('ATM №', num_of_atm, 'has been successfully deleted')




    def ATM_amount_of_money (self, num_of_atm):
        for i in range(len(Bank.atm_numbers)):
            if Bank.atm_numbers[i] == num_of_atm:
                return (print ('ATM №', num_of_atm, 'contains', self.atm[i].amount, 'dollars'))
            elif i == len(Bank.atm_numbers) - 1:
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

            if (Bank.__max_atm_bill - i.bill_sum) * 100 < a:
                d += 1

        if c == len (self.atm) or d == len (self.atm):
            print('There are no one atm to add money in. All ATMs are full')
            pass
        else:
            b = 0
            while self.atm[n].bill_sum == Bank.__max_atm_bill and (Bank.__max_atm_bill - self.atm[n].bill_sum * 100) < a:
                b = randint(0, len(self.atm))
                while b == n:
                    b = randint(0, len(self.atm))
                n = b

            print('ATM №', self.atm[n].number, 'is chosen. Now it contains', self.atm[n].amount, 'dollars')

            if a >= 100:
                self.atm[n].bill_100_dol += int(a / 100)
                self.atm[n].bill_sum += int(a / 100)
                self.atm[n].amount += int(a / 100) * 100
                self.money.amount += int(a / 100) * 100
                a -= int(a / 100) * 100

            if a >= 50:
                self.atm[n].bill_50_dol += int(a / 50)
                self.atm[n].bill_sum += int(a / 50)
                self.atm[n].amount += int(a / 50) * 50
                self.money.amount += int(a / 50) * 50
                a -= int(a / 50) * 50

            if a >= 20:
                self.atm[n].bill_20_dol += int(a / 20)
                self.atm[n].bill_sum += int(a / 20)
                self.atm[n].amount += int(a / 20) * 20
                self.money.amount += int(a / 20) * 20
                a -= int(a / 20) * 20

            if a >= 10:
                self.atm[n].bill_10_dol += int(a / 10)
                self.atm[n].bill_sum += int(a / 10)
                self.atm[n].amount += int(a / 10) * 10
                self.money.amount += int(a / 10) * 10
                a -= int(a / 10) * 10

            if a >= 5:
                self.atm[n].bill_5_dol += int(a / 5)
                self.atm[n].bill_sum += int(a / 5)
                self.atm[n].amount += int(a / 5) * 5
                self.money.amount += int(a / 5) * 5
                a -= int(a / 5) * 5

            if a >= 2:
                self.atm[n].bill_2_dol += int(a / 2)
                self.atm[n].bill_sum += int(a / 2)
                self.atm[n].amount += int(a / 2) * 2
                self.money.amount += int(a / 2) * 2
                a -= int(a / 2) * 2

            if a >= 1:
                self.atm[n].bill_1_dol += int(a / 1)
                self.atm[n].bill_sum += int(a / 1)
                self.atm[n].amount += int(a / 1)
                self.money.amount += int(a / 1)
                a -= int(a / 1)

            print('After add operation ATM №', self.atm[n].number, 'contains', self.atm[n].amount, 'dollars')

    def getMoney (self, amount, num_ATM = 0): #If input has only one argument (amount of money), you will get money from the main department (not from ATM).
        a = amount
        if num_ATM == 0:
            if a < self.money.amount:
                if a >= 100:
                    self.money.bill_100_dol -= int(a / 100)
                    self.money.amount -= int(a / 100) * 100
                    a -= int(a / 100) * 100

                if a >= 50:
                    self.money.bill_50_dol -= int(a / 50)
                    self.money.amount -= int(a / 50) * 50
                    a -= int(a / 50) * 50

                if a >= 20:
                    self.money.bill_20_dol -= int(a / 20)
                    self.money.amount -= int(a / 20) * 20
                    a -= int(a / 20) * 20

                if a >= 10:
                    self.money.bill_10_dol -= int(a / 10)
                    self.money.amount -= int(a / 10) * 10
                    a -= int(a / 10) * 10

                if a >= 5:
                    self.money.bill_5_dol -= int(a / 5)
                    self.money.amount -= int(a / 5) * 5
                    a -= int(a / 5) * 5

                if a >= 2:
                    self.money.bill_2_dol -= int(a / 2)
                    self.money.amount -= int(a / 2) * 2
                    a -= int(a / 2) * 2

                if a >= 1:
                    self.money.bill_1_dol -= int(a / 1)
                    self.money.amount -= int(a / 1)
                    a -= int(a / 1)

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
                if a < self.atm[n].amount:
                    if a >= 100:
                        self.atm[n].bill_100_dol -= int(a / 100)
                        self.atm[n].bill_sum -= int(a / 100)
                        self.atm[n].amount -= int(a / 100) * 100
                        self.money.amount -= int(a / 100) * 100
                        a -= int(a / 100) * 100

                    if a >= 50:
                        self.atm[n].bill_50_dol -= int(a / 50)
                        self.atm[n].bill_sum -= int(a / 50)
                        self.atm[n].amount -= int(a / 50) * 50
                        self.money.amount -= int(a / 50) * 50
                        a -= int(a / 50) * 50

                    if a >= 20:
                        self.atm[n].bill_20_dol -= int(a / 20)
                        self.atm[n].bill_sum -= int(a / 20)
                        self.atm[n].amount -= int(a / 20) * 20
                        self.money.amount -= int(a / 20) * 20
                        a -= int(a / 20) * 20

                    if a >= 10:
                        self.atm[n].bill_10_dol -= int(a / 10)
                        self.atm[n].bill_sum -= int(a / 10)
                        self.atm[n].amount -= int(a / 10) * 10
                        self.money.amount -= int(a / 10) * 10
                        a -= int(a / 10) * 10

                    if a >= 5:
                        self.atm[n].bill_5_dol -= int(a / 5)
                        self.atm[n].bill_sum -= int(a / 5)
                        self.atm[n].amount -= int(a / 5) * 5
                        self.money.amount -= int(a / 5) * 5
                        a -= int(a / 5) * 5

                    if a >= 2:
                        self.atm[n].bill_2_dol -= int(a / 2)
                        self.atm[n].bill_sum -= int(a / 2)
                        self.atm[n].amount -= int(a / 2) * 2
                        self.money.amount -= int(a / 2) * 2
                        a -= int(a / 2) * 2

                    if a >= 1:
                        self.atm[n].bill_1_dol -= int(a / 1)
                        self.atm[n].bill_sum -= int(a / 1)
                        self.atm[n].amount -= int(a / 1)
                        self.money.amount -= int(a / 1)
                        a -= int(a / 1)

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
        self.bill_100_dol = 100
        self.bill_50_dol = 100
        self.bill_20_dol = 100
        self.bill_10_dol = 100
        self.bill_5_dol = 100
        self.bill_2_dol = 100
        self.bill_1_dol = 100
        self.bill_sum = self.bill_100_dol + self.bill_50_dol + self.bill_20_dol + self.bill_10_dol + self.bill_5_dol + self.bill_2_dol + self.bill_1_dol
        self.amount = (self.bill_100_dol * 100) + (self.bill_50_dol * 50) + (self.bill_20_dol * 20) + (self.bill_10_dol * 10) + (self.bill_5_dol * 5) + (self.bill_2_dol * 2) + (self.bill_1_dol * 1)



class Money:
    def __init__(self, money):
        money_count = money
        self.bill_100_dol = randrange (int (money_count / 100))
        money_count -= self.bill_100_dol * 100

        if money_count >= 50:
            self.bill_50_dol = randrange (int (money_count / 50))
            money_count -= self.bill_50_dol * 50
        else:
            self.bill_50_dol = 0

        if money_count >= 20:
            self.bill_20_dol = randrange (int (money_count / 20))
            money_count -= self.bill_20_dol * 20
        else:
            self.bill_20_dol = 0

        if money_count >= 10:
            self.bill_10_dol = randrange (int (money_count / 10))
            money_count -= self.bill_10_dol * 10
        else:
            self.bill_10_dol = 0

        if money_count >= 5:
            self.bill_5_dol = randrange (int (money_count / 5))
            money_count -= self.bill_5_dol * 5
        else:
            self.bill_5_dol = 0

        if money_count >= 2:
            self.bill_2_dol = randrange (int (money_count / 2))
            money_count -= self.bill_2_dol * 2
        else:
            self.bill_2_dol = 0

        self.bill_1_dol = money_count

        self.amount = (self.bill_100_dol * 100) + (self.bill_50_dol * 50) + (self.bill_20_dol * 20) + (self.bill_10_dol * 10) + (self.bill_5_dol * 5) + (self.bill_2_dol * 2) + (self.bill_1_dol * 1)


    def cashToATM (self):
        self.bill_100_dol -= 100
        self.bill_50_dol -= 100
        self.bill_20_dol -= 100
        self.bill_10_dol -= 100
        self.bill_5_dol -= 100
        self.bill_2_dol -= 100
        self.bill_1_dol -= 100