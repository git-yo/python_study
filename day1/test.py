menu = {
    "北京":{
        "海淀":{
            "五道口":{
                "soho":{},
                "网易":{},
                "google":{},
            },
            "上地":{
                "百度":{},
            },
            "中关村":{
                "爱奇艺":{},
                "汽车之家":{},
                "youku":{},
            },
        },
        "昌平":{
            "沙河":{},
            "天通苑":{},
            "回龙观":{},
        },
        "朝阳":{},
    },
    "上海":{},
    "山东":{},
}
current_layer = menu
#parent_layer = menu
parent_layers = []
while True:
    for key in current_layer:
        print(key)
    choice = input(">>:").strip()
    if len(choice) == 0 :continue
    if choice in current_layer:
        #parent_layer = current_layer
        parent_layers.append(current_layer)
        current_layer=current_layer[choice] #改成子层
    elif choice == "b":
        #current_layer = parent_layer  # 把子层变成父层
        if  parent_layers: #[]
            current_layer = parent_layers.pop()
    elif choice == "q":
        current_layer = menu
    else:
        print("none")