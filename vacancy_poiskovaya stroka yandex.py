n = int(input())
dic = {}
for i in range(n):
    zapros = list(input(). split( ))
    if zapros[0] == '+':
        dic[zapros[2]] = dic.get(zapros[2],0) + int(zapros[1])
    sorted_value = sorted(dic.items(), key=lambda kv: kv[0])
    sorted_dic = dict(sorted_value)
    sorted_items = sorted(sorted_dic.items(), key=lambda kv: kv[1], reverse=True)
    sorted_dic = dict(sorted_items)

    if zapros[0] == '?':
        for key,value in sorted_dic.items():
            if zapros[1] in key:
                print(key)
                break



