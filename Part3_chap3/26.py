'''
하노이의 탑 (실습) : 잘 이해하고 외우기
'''
            # 원판 개수, 출발 기둥, 도착 기둥, 경유 기둥
def moveDisc(disCnt, fromBar, toBar, viaBar):
    if disCnt == 1:
        print(f'{disCnt}disc를 {fromBar}애서 {toBar}(으)로 이동!')

    else:
        # disCnt-1 개 원판을 경우 기둥으로 이동
        moveDisc(disCnt-1, fromBar, viaBar, toBar)

        # disCnt 개 원판을 목적 기둥으로 이동
        print(f'{disCnt}disc를 {fromBar}애서 {toBar}(으)로 이동!')

        # disCnt-1 개 원판을 도착 기둥으로 이동
        moveDisc(disCnt-1, viaBar, toBar, fromBar)

moveDisc(3, 1, 3, 2)