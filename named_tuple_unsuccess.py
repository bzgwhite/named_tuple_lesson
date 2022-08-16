from datetime import date
from collections import namedtuple

Hand = namedtuple('Hand',('name'))
Arm  = namedtuple('Arm',('name','hand'))
Foot = namedtuple('Foot',('name'))
Human = namedtuple('Human',
    ('name','birth_date','right_arm','left_arm','right_foot','left_foot')
)

if __name__ == '__main__':
    right_hand = Hand('伝説の右手')
    left_hand  = Hand('黄金の左手')
    right_arm  = Arm('伝説の右手',right_hand)
    left_arm   = Arm('黄金の左腕',left_hand)
    right_foot = Foot('神が愛した右足')
    left_foot  = Foot('世界が泣いた左足')

    legend_human = Human(
        '伝説の人類',date(2017,5,1),right_arm,left_arm,right_foot,left_foot
    )
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

    print('--- 繰り返し処理ができるか ---')
    for parts in legend_human:
        print(parts)