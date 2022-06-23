# 단순 연결 리스트
# 데이터와 포인터를 포함한 노드로 구현
# 객체 지향 언어인 python 비교적 구현 쉬움

from dataclasses import dataclass
# dataclass(): __init__() 나 __repr__() 과 같은 생성된 특수 메서드를
# 사용자 정의 클래스에 자동으로 추가하는 데코레이터와 함수를 제공합니다.


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class SList:
    def __init__(self):
        self.no = 0
        self.head = None
        self.current = None
    
    def __len__(self):
        return self.no

    def search(self, data):   # 머리부터 탐색
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1
    
    def __contains__(self, data):
        return self.search(data) >= 0

    def add_first(self, data):
        ptr = self.head
        self.head = self.current = Node(data, ptr)
        self.no += 1
    
    def add_last(self, data):
        ptr = self.head
        if self.head is None:
            self.add_first(data)
            return
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = self.current = Node(data, None)
        self.no += 1
    
    def remove_first(self):
        if self.head is not None:
            self.head = self.current = self.head.next
            self.no -= 1
    
    def remove_last(self):
        if self.head is not None:
            if self.head.next is None:
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head
                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None
                self.current = pre
                self.no -= 1
    
    def remove(self, p):
        if self.head is not None:
            if p is self.head:
                self.remove_first()
            else:
                ptr = self.head
                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return
                ptr.next = p.next
                self.current = ptr
                self.no -= 1
    
    def remove_current_node(self):
        self.remove(self.current)
    
    def clear(self):
        while self.head is not None:
            self.remove_first()
        self.current = None
        self.no = 0
    
    def next(self):
        if self.current is None or self.current.next is None:
            return False
        self.current = self.current.next
        return True

    def print_current_node(self):
        if self.current is None:
            print("출력할 노드가 없습니다.")
        else:
            print(self.current.data)
    
    def print_all(self):
        if self.head is not None:
            ptr = self.head
            print(ptr.data, end=' ')
            while ptr.next is not None:
                print("->", end=' ')
                ptr = ptr.next
                print(ptr.data, end=' ')