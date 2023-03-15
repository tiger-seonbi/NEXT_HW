#실습코드
account = 1000
limit_for_loan = 500
limit_for_withdraw = 400
def give_me_money(amount):
    if amount <= account:
        if amount > limit_for_withdraw:
            a = amount//limit_for_withdraw
            b = amount%limit_for_withdraw
            for i in range(a):
                print(limit_for_withdraw)
            print(b)
        else:
            print(amount)
    elif amount <= (account + limit_for_loan):
        a = amount//limit_for_withdraw
        b = amount%limit_for_withdraw
        for i in range(a):
            print(limit_for_withdraw)
        print(b)
    else:
        c = amount - (account + limit_for_loan)
        print(f'''you don't have enough money, you have to deposite {c} dollars''')

# give_me_money(800)
# give_me_money(1200)
# give_me_money(1700)

# 물어보기
def question():
    animal = input()
    if animal == '토끼':
        print('깡총')
    else: 
        print(f'''안녕 난 {animal}이 아니라 알락꼬리꼬마도요야.''')
# question()

# 핵전쟁
def war():
    for i in range(10):
        print(10 - i)
        print('발사')
    print(0)
    print('발사')
war()