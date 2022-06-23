# 원형 이중 연결 리스트

from dataclasses import dataclass
from gettext import dngettext

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next or prev
        self.prev = prev or next

class DoubleLinkedList:
    def __init__(self):
        self.head = self.current =  Node()  # 더미 노드 생성: 개발의 편의를 위함
        self.no = 0
    
    def __len__(self):
        return self.no
    
    def is_empty(self):
        return self.head.next is self.head
    
    def search(self, data):
        cnt = 0
        ptr = self.head.next

        while ptr is not self.head:
            if data == ptr.data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data):
        return self.search(data) >= 0
    
    def add(self, data):
        # 주목 노드 바로 뒤에 삽입
        ptr = self.current
        node = Node(data, ptr.next, ptr)
        ptr.next.prev = node
        ptr.next = node
        self.current = node
        self.no += 1
    
    def remove_cnode(self):     # 현재 노드 삭제
        if not self.is_empty():
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.prev
            self.no -= 1
            if self.current is self.head:
                self.current = self.head.next

    def remove(self, p):
        if not self.is_empty():
            ptr = self.head.next
            while ptr is not self.head:
                if ptr is p:
                    self.current = p
                    self.remove_cnode()
                    break   # 중복되는 데이터 또 지우는 것 방지
                ptr = ptr.next
    
    def remove_first(self):
        if not self.is_empty():
            self.current = self.head.next
            self.remove_cnode()

    def clear(self):
        while not self.is_empty():
            self.remove_first()
        self.no = 0

        
