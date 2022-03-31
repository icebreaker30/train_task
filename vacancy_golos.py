import math


dolya_1 = float(input())
n_people = int(input())
skill = {}

for i in range(n_people):
    man,navuk = input().split()
    skill[man] = navuk

n_picture = int(input())
complex = {}

for i in range(n_picture):
    picture, slojnost = input().split()
    complex[picture] = slojnost

n_people_picture = int(input())
razmetka = {}

for i in range(n_picture):
    task_id = input()
    for j in range(n_people_picture):

        l = list(map(str, input().split()))

        razmetka.update({task_id : l})
#         оно может апдейтить значения Л а не добавлять, надо проверить когда одну картину проверяет много людей

def probabilty_1or0(slojn,skil,clas):
    if clas == 0:
        return 1 - 1/(1 + math.exp(-skil * slojn))
    else:
        return 1/(1 + math.exp(-skil * slojn))
# сейчас мы нашли все вероятности того, что картины принадлежат к класссу 1 по каждому оценщику
# считаем кол-во маджорити м т.е. необходимое минимальное число для принятия решения

m =
print(razmetka)