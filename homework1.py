

hero_list = []


def delete_hero(hero_list):
    """
    :param hero_list:  英雄列表信息
    :param hero_name:  英雄的名字
    :return:
    """
    hero_name = input("请输入需要删除的英雄信息：")
    for i in hero_list:
        if hero_name == i["name"]:
            hero_list.remove(i)
            print(f"删除之后所有的英雄的数据信息为{hero_list}")
            return hero_list
    print("没有找到要删除的英雄")
    return hero_list


def create_hero(hero_list):
    """
    :param hero_list: 英雄列表信息
    :param hero_name: 英雄名称
    :param hero_volume: 英雄血量
    :param hero_power: 英雄攻击力
    
    """
    hero_name = input("请输入英雄的名称：")

    for i in hero_list:
        if i["name"] == hero_name:
            print("添加的英雄重复了")
            return hero_list                 
        else:
            pass
    hero_volume = input("请输入英雄的血量：")
    hero_power = input("请输入英雄的攻击力：")
    hero_info = {"name": hero_name, "volume": hero_volume, "power": hero_power}             
    print("创建成功！英雄名称为{} ，英雄的血量为{} ，英雄的攻击力为{}".format(hero_name,hero_volume,hero_power))
   
    hero_list.append(hero_info) 

    return hero_list

def update_hero(hero_list):
    hero_name = input("请输入英雄的名称：")
    hero_volume = input("请输入英雄的血量：")
    hero_power = input("请输入英雄的攻击力：")
    for i in range(len(hero_list)):
        if hero_list[i].get("name") == hero_name:
            hero_list[i]["volume"] = hero_volume
            hero_list[i]["power"] = hero_power
            print("修改成功，修改后的英雄名称为{},血量为{},英雄的攻击力为{}".format(hero_name,hero_volume,hero_power))
            return hero_list
        else:
            pass
    print("没有找到要修改的英雄")
    

def check_hero(hero_list):
    hero_name = input("请输入英雄的名称：")
    for i in range(len(hero_list)):
        if hero_list[i].get("name") == hero_name:
            hero_volume = hero_list[i].get("volume")
            hero_power = hero_list[i].get("power")
            print(f"查看的英雄名称为{hero_name}， 血量为{hero_volume}，英雄的攻击力为{hero_power}")
            return hero_list    
    print("没有找到要查看的英雄")
  

print("""
    1. **创建英雄**
    2. **查看英雄信息**
    3. **修改英雄信息**
    4. **删除英雄**
    5. **退出系统**
""")
while True:
    res = input("请输入对应的选项，即可执行对应的操作：")
    if res == "1":
        create_hero(hero_list)
    # 如果想要实现 查看jinx 的血量，jinx 的所有信息。
    elif res == "2":
        check_hero(hero_list)

        # 在字符串中，如果用到了引号，符合内单外双， 内双外单的规则
        # print(f"查看英雄{hero_info['name']}对应的血量为{hero_info['volume']}")
    elif res == "3":
        update_hero(hero_list)
    elif res == "4":
        delete_hero(hero_list)

    elif res == "5":
        print("退出系统")
        break        
    else: 
        print("""
        1. **创建英雄**
        2. **查看英雄信息**
        3. **修改英雄信息**
        4. **删除英雄**
        5. **退出系统**    
        """)
        pass

print(f"英雄列表中的所有元素为{hero_list}")  

  



















