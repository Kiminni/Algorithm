# 오픈 주소법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# 버킷의 속성
class Status(Enum):
    OCCUPIED = 0 # 데이터를 저장
    EMPTY = 1 # 비어있음
    DELETED = 2 # 삭제 완료

class Bucket:
    # 해시를 구성하는 버킷
    def __init__(self, key: Any = None, value: Any = None,stat: Status = Status.EMPTY) -> None:
        # 초기화
        self.key = key
        self.value = value
        self.stat = stat