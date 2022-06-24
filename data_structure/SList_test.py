# SList_test

from SList import SList

newL = SList()

while True:
    print()
    print("1: 맨 앞에 추가, 2: 맨 뒤에 추가, 3: 삭제, 4: 출력, 5: 데이터 개수, q: 프로그램 종료")
    option = int(input("옵션을 선택하세요: 1~5 or q: "))

    if option == 1:
        data = input("데이터를 입력하세요: ")
        newL.add_first(data)
    elif option == 2:
        data = input("데이터를 입력하세요: ")
        newL.add_last(data)
    elif option == 3:
        target = input("삭제할 데이터를 입력하세요: ")
        newL.remove(target)
    elif option == 4:
        print("모든 데이터를 출력합니다.")
        print()
        newL.print_all()
        print()
    elif option == 5:
        print("현재 데이터 개수:", len(newL))

