# CList_test

from CList import DoubleLinkedList

newL = DoubleLinkedList()

while True:
    print()
    print("1: 데이터 추가, 2: 삭제, 3: 검색, 4: 출력, 5: 초기화, 6: 데이터 개수, q: 프로그램 종료")
    option = input("옵션을 선택하세요: 1~5 or q: ")

    if option == '1':
        data = input("데이터를 입력하세요: ")
        newL.add(data)
    elif option == '2':
        target = input("삭제할 데이터를 입력하세요: ")
        newL.remove(target)
    elif option == '3':
        target = input("검색할 데이터를 입력하세요: ")
        res = newL.search(target)
        if res != -1:
            print(f'해당 데이터는 {res}번 인덱스에 있습니다.')
        else:
            print('해당 데이터는 없습니다.')
    elif option == '4':
        print("모든 데이터를 출력합니다.")
        print()
        newL.print_all()
        print()
    elif option == '5':
        print('모든 데이터를 초기화합니다.')
    elif option == '6':
        print("현재 데이터 개수:", len(newL))
    else:
        print('프로그램을 종료합니다.')
        break

