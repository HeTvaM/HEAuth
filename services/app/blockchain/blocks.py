import hashlib

from pydantic import BaseModel, Field, IPvAnyAddres
from datetime import datetime, time
from typing import List, Optional, Any


class BaseBlock:
    @staticmethod
    def update(cls, prev_block) -> bool:
        hash_algo = hashlib.sha512()
        try:
            data = str(prev_block.dict()).encode()
        except AttributeError:
            info = [str(obj) for obj in prev_block]
            data = "".join(info).encode()
        try:
            hash_algo.update(data)
            cls.hash = hash_algo.hexdigest()
        except AttributeError:
            return False

        return True


class BlockModel(BaseModel, BaseBlock):
    timestamp: datetime
    login: str = Field(min_length=3, max_length=40)
    #ip: str = Field(min_length=7, max_length=20)
    ip: IPvAnyAddres
    status: str
    hash: str = None

    def __eq__(self, other):
        count = self.login == other.login
        count += self.ip == other.ip

        return count == 2


class ActionBlockModel(BlockModel):
    data: dict


class CloseBlockModel(BaseModel, BaseBlock):
    login: str = Field(min_length=3, max_length=40)
    ip: str = Field(min_length=7, max_length=20)
    open_date: datetime
    close_date: datetime
    activity: dict
    hash: str = None
