class Bank:
    def __init__(self, total_amount, limit_for_loan, limit_for_withdrawal):
        self.total_amount = total_amount
        self.limit_for_loan = limit_for_loan
        self.limit_for_withdrawal = limit_for_withdrawal

    def repeat_withdrawing_money(self, amount, limit_for_withdrawal) :
        count = amount // limit_for_withdrawal
        rest = amount % limit_for_withdrawal
        for i in range(count):
        # 반복문
            print(f'''This is your money - {limit_for_withdrawal}''')
            # 중첩구조
            if i == (count - 1):
                print(f'''This is your money - {rest}''')

    def show_me_the_money(self, amount):
        #조건문 분기1
        if amount <= self.total_amount:
            self.repeat_withdrawing_money(amount, self.limit_for_withdrawal)
        #조건문 분기2
        elif amount <= (self.total_amount + self.limit_for_loan):
            print('Wait!! Do you want loan?')
        #조건문 분기3
        else:
            print('Your money is not enough!')

hana_bank = Bank(1000,200,100)
hana_bank.show_me_the_money(450)
print()

sinhan_bank = Bank(500,500,50)
sinhan_bank.show_me_the_money(250)




