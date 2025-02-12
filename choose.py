import random


def choose():
    meat_dict = {}
    fish_dict = {}
    vegetable_dict = {}
    soup_dict = {}
    meat_number = int(input('输入您今晚想吃的荤菜数目:'))
    fish_number = 0
    vegetable_number = int(input('输入您今晚想吃的素菜数目:'))
    soup_number = int(input('输入您今晚想吃的汤的数目:'))
    with open('meat.txt', 'r', encoding='utf-8') as rf:
        cnt = 1
        line = rf.readline()
        while line:
            meat_dict[cnt] = line
            cnt += 1
            line = rf.readline()
    with open('fish.txt', 'r', encoding='utf-8') as rf:
        cnt = 1
        line = rf.readline()
        while line:
            fish_dict[cnt] = line
            cnt += 1
            line = rf.readline()
    with open('vegetable.txt', 'r', encoding='utf-8') as rf:
        cnt = 1
        line = rf.readline()
        while line:
            vegetable_dict[cnt] = line
            cnt += 1
            line = rf.readline()
    with open('soup.txt', 'r', encoding='utf-8') as rf:
        cnt = 1
        line = rf.readline()
        while line:
            soup_dict[cnt] = line
            cnt += 1
            line = rf.readline()
    print(f'--------------------今日菜单------------------------')
    today_meat = set()
    today_fish = set()
    today_veg = set()
    today_soup = set()
    if meat_number != 0:
        for _ in range(meat_number):
            num = random.randint(1, len(meat_dict))
            choice = meat_dict[num]
            if choice not in today_meat:
                today_meat.add(choice)
            else:
                while choice in today_meat:
                    num = random.randint(1, len(meat_dict))
                    choice = meat_dict[num]
                today_meat.add(choice)
            print(choice, end='')
    if fish_number != 0:
        for _ in range(fish_number):
            num = random.randint(1, len(fish_dict))
            choice = fish_dict[num]
            if choice not in today_fish:
                today_fish.add(choice)
            else:
                while choice in today_fish:
                    num = random.randint(1, len(fish_dict))
                    choice = fish_dict[num]
                today_fish.add(choice)
            print(choice, end='')

    if vegetable_number != 0:
        for _ in range(vegetable_number):
            num = random.randint(1, len(vegetable_dict))
            choice = vegetable_dict[num]
            if choice not in today_veg:
                today_veg.add(choice)
            else:
                while choice in today_veg:
                    num = random.randint(1, len(vegetable_dict))
                    choice = vegetable_dict[num]
                today_veg.add(choice)
            print(choice, end='')

    if soup_number != 0:
        for _ in range(soup_number):
            num = random.randint(1, len(soup_dict))
            choice = soup_dict[num]
            if choice not in today_soup:
                today_soup.add(choice)
            else:
                while choice in today_soup:
                    num = random.randint(1, len(soup_dict))
                    choice = soup_dict[num]
                today_soup.add(choice)
            print(choice, end='')


if __name__ == '__main__':
    choose()
