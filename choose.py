import random


def choose():
    meat_list = []
    fish_list = []
    vegetable_list = []
    soup_list = []
    meat_number = int(input('输入您今晚想吃的荤菜数目:'))
    fish_number = 0
    vegetable_number = int(input('输入您今晚想吃的素菜数目:'))
    soup_number = int(input('输入您今晚想吃的汤的数目:'))
    with open('meat.txt', 'r', encoding='utf-8') as rf:
        line = rf.readline()
        while line:
            meat_list.append(rf.readline())
            line = rf.readline()
    with open('fish.txt', 'r', encoding='utf-8') as rf:
        line = rf.readline()
        while line:
            fish_list.append(rf.readline())
            line = rf.readline()
    with open('vegetable.txt', 'r', encoding='utf-8') as rf:
        line = rf.readline()
        while line:
            vegetable_list.append(rf.readline())
            line = rf.readline()
    with open('soup.txt', 'r', encoding='utf-8') as rf:
        line = rf.readline()
        while line:
            soup_list.append(rf.readline())
            line = rf.readline()
    print(f'--------------------今日菜单------------------------')
    today_meat = set()
    today_fish = set()
    today_veg = set()
    today_soup = set()
    if meat_number != 0:
        for _ in range(meat_number):
            choice = random.choice(meat_list)
            if choice not in today_meat:
                today_meat.add(choice)
            else:
                while choice in today_meat:
                    choice = random.choice(meat_list)
                today_meat.add(choice)
            print(choice, end='')

    if fish_number != 0:
        for _ in range(fish_number):
            choice = random.choice(fish_list)
            if choice not in today_fish:
                today_fish.add(choice)
            else:
                while choice in today_fish:
                    choice = random.choice(fish_list)
                today_fish.add(choice)
            print(choice, end='')

    if vegetable_number != 0:
        for _ in range(vegetable_number):
            choice = random.choice(vegetable_list)
            if choice not in today_veg:
                today_veg.add(choice)
            else:
                while choice in today_veg:
                    choice = random.choice(vegetable_list)
                today_veg.add(choice)
            print(choice, end='')

    if soup_number != 0:
        for _ in range(soup_number):
            choice = random.choice(soup_list)
            if choice not in today_soup:
                today_soup.add(choice)
            else:
                while choice in today_soup:
                    choice = random.choice(soup_list)
                today_soup.add(choice)
            print(choice, end='')


if __name__ == '__main__':
    choose()
