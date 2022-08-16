from datetime import date
from typing import NamedTuple


class Hand(NamedTuple):
    name       : str

class Arm(NamedTuple):
    name       : str
    hand       : Hand

class Foot(NamedTuple):
    name       : str

class Human(NamedTuple):
    name       : str
    birth_date : date = date(2017,5,1) # フィールド設定時に代入することでデフォルト値の設定可能
    right_arm  : Arm  = Arm('伝説の右腕',Hand('伝説の右手'))
    left_arm   : Arm  = Arm(name='黄金の左腕',hand=Hand('黄金の左手'))
    right_foot : Foot = Foot('神が愛した右足')
    left_foot  : Foot = Foot(name='世界が泣いた左足')



if __name__ == '__main__':
    legend_human = Human('伝説の人類')
    print('--- index指定と名前指定で呼び出しできるか ---')
    print('名前',legend_human[0], legend_human.name)
    print('誕生日',legend_human[1], legend_human.birth_date)
    print('右腕',legend_human[2][0], legend_human.right_arm.name)
    print('左手',legend_human[3][1][0], legend_human.left_arm.hand.name)

    print('--- 再代入するとエラー検知されるか ---')
    try:
        legend_human.name = '伝説の再代入'
        print('失敗：再代入に成功しました')
    except Exception as e:
        print(e.__doc__)

    print('--- イテレート処理ができるか ---')
    for parts in legend_human:
        print(parts)
