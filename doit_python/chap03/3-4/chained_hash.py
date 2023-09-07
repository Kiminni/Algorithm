# 체인법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    # 해시 구성 노드

    def __init__(self, key: Any, value: Any, next: Node) -> None :
        # 초기화
        self.key = key # 키
        self.value = value # 값
        self.next = next # 뒤쪽 노드 참조

        # 파이썬의 변수는 객체와 연결된 이름 ->객체에 대한 참조 (next만 참조하는 것이 아님)

class ChainedHash:
    def __init__(self, capacity: int) -> None:
        # 초기화

        self.capacity = capacity # 해시 테이블의 크기 지정
        self.table = [None] * self.capacity # 해시 테이블(리스트) 생성

    def hash_value(self, key: Any) -> int:
        # 해시 값을 구함
        
        if isinstance(key, int):
            return key % self.capacity
        
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
    
    # 해시가 int형 -> capacity로 나눈 나머지가 hash 값 
    # 해시가 int형이 아님 ->  표준 라이브러리로 형변환

    def search(self, key: Any) -> Any:
        # 키가 key인 원소를 검색해 값을 반환

        hash = self.hash_value(key) # 검색하는 키의 해시값
        p = self.table[hash]

        while p is not None: 
            if p.key == key: 
                return p.value # 검색 성공 
            p = p.next # 뒤쪽 노드를 주목

        return None
    
    def add(self, key: Any, value: Any) -> bool:
        # 키가 key이고 값이 value인 원소를 추가

        hash = self.hash_value(key) # 추가하는 key의 해시값
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False # 추가 실패
            p = p.next # 뒤쪽 노드를 주목

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp  # 노드 추가
        return True # 추가 성공
    
        # hash_value를 이용해 키 -> 해시값
        # 해시값을 인덱스로 하는 버킷에 주목
        # 연결 리스트 앞에서 부터 선형 검색 후 키와 같은 값 -> 검색 실패, 다른 값 -> 맨 앞에 노드를 추가


    def remove(self, key: Any) -> bool:
        # 키가 key인 원소 삭제
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None
        
        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next

                else:
                    pp.next = p.next
            return False
        
    def dump(self) -> None:
        # 해시 테이블을 출력
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end = '')
            while p is not None:
                print(f' -> {p.key}  ({p.value})',end='')
                p = p.next
            print()
        


        '''
        sha256 -> RSA의 FIPS 알고리즘, 문자열의 해시 값의 생성자
        encode() ->바이트 문자열을 인수로 전달 -> key를 str형으로 변환 후 그 문자열을 encode 함수에 전달
        hexdigest ->해시값을 16진수 문자열로
        int ->16진수 문자열로 하는 int형 
        search() -> 해시 함수를 사용 해 해시 값으로 변환 ->인덱스로 하는 버킷에 주목 -> 연결 리스트를 앞에서 차례로 스캔
        '''