import hashlib

from pydantic import BaseModel, Field, IPvAnyAddress
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
    ip: str = Field(min_length=7, max_length=20)
    status: str
    hash: str = None

    def __eq__(self, other):
        count = self.login == other.login
        count += self.ip == other.ip

        return count == 2


class ActionBlockModel(BlockModel):
    data: dict


class SuperBlockModel(BaseModel, BaseBlock):
    blocks: Any
    hash: str = None

    def dict(self) -> dict:
        blocks_dict = {}
        try:
            dicts = [block.dict() for block in self.blocks]
        for d in dicts:
            blocks_dict.update(d)

        return blocks_dict
