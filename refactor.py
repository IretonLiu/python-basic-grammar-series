def method1():
    while True:
        print( '1から5で評価を入力してください' )
        point = input()
        if point.isdecimal():
            point = int(point)
            if  point <= 0 or point > 5: # 0以下または5より大きいという条件式
                print( '1から5で入力してください' )
                point = input()
            else:
                print( 'コメントを入力してください' )
                comment = input()
                post = f'ポイント: {point} コメント: {comment}'
                file_pc = open("data.txt", encoding="utf-8", mode="a")
                file_pc.write(f'{post}\n')
                file_pc.close()
                break
        else:
            print( '評価ポイントは数字で入力してください' )

def method2():
    print( 'これまでの結果' )
    read_file = open("data.txt", encoding="utf-8", mode="r")
    print( read_file.read() )
    read_file.close()

while True:
    print( '実施したい処理を選択してください' )
    print( '1:評価ポイントとコメントを入力する' )
    print( '2:今までの結果を確認する' )
    print( '3:終了する' )
    num = input()

    if num.isdecimal():
        num = int(num)

        if num == 1:
            method1()
        elif num == 2:
            method2()
        elif num == 3:
          print( '終了します' )
          break  # 繰り返す処理を終了させる構文
        else:
            print( '1から3で入力してください' )
    else:
        print( '1から3で入力してください' )