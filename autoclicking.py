import pyautogui as pg
import time

t = 3       # 각 Step당 대기 시간

# 1 : 프로필 위치
alertbox1_1 = pg.confirm(title='프로필 위치 (1/5)', text='클릭 후 {}초 내로 상대 프로필 위에 포인터 올려주세요'.format(t), buttons=['OK', 'Cancel'])

if alertbox1_1 == 'OK':
    time.sleep(t)
    x1, y1 = pg.position()           # 포인터 위치 찾기 (x,y분리)
    alertbox1_2 = pg.alert(title='완료', text='x좌표:{} y좌표:{}'.format(x1,y1), button='OK')

    # 2 : 프로필 내 반복 공감 스티커 위치
    alertbox2_1 = pg.confirm(title='공감스티커 위치 (2/5)', text='클릭 후 {}초 내로 반복해서 누를 위치에 포인터를 올려주세요'.format(t), buttons=['OK', 'Cancel'])

    if alertbox2_1 == 'OK':
        time.sleep(t)
        x2, y2 = pg.position()
        alertbox2_2 = pg.alert(title='완료', text='x좌표:{} y좌표:{}'.format(x2,y2), button='OK')

        # 3 : 빈 공간 재클릭
        alertbox3_1 = pg.confirm(title='빈 공간 (3/5)', text='클릭 후 {}초 내로 빈 공간에 포인터를 올려주세요'.format(t), buttons=['OK', 'Cancel'])

        if alertbox3_1 == 'OK':
            time.sleep(t)
            x3, y3 = pg.position()
            alertbox3_2 = pg.alert(title='완료', text='x좌표:{} y좌표:{}'.format(x3,y3), button='OK')

            # 4 : 1회당 클릭 수 지정
            alertbox4 = int(pg.prompt(title='1회당 클릭 수 (4/5)', text='1회당 클릭횟수를 적어주세요', default='500'))      # 정수형 입력

            if int(alertbox4) == alertbox4:
                n = int(alertbox4)

                # 5 :반복횟수 지정
                alertbox5 = int(pg.prompt(title='반복실행 (5/5)', text='반복실행 횟수를 적어주세요', default='10'))         # 정수형 입력

                if int(alertbox5) == alertbox5:
                    k = int(alertbox5)

                    for i in range (k):
                        # 상대 프로필 위치 입력
                        pg.moveTo(x1,y1)
                        pg.click(clicks=1)

                        # 상대 클릭 이모티콘 위치 입력
                        time.sleep(0.5)
                        pg.moveTo(x2,y2)
                        pg.click(clicks=n)     # 클릭 횟수 조절 가능

                        # 빈 부분 재클릭
                        time.sleep(1)
                        pg.moveTo(x3,y3)
                        pg.click(clicks=1)

                        print(i+1,"/",k,"번")
                    
                    # 완료
                    alertbox6 = pg.alert(title='종료', text='완료되었습니다', button='OK')