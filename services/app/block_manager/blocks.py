from pydantic import BaseModel, Field, IPvAnyAddress
from datetime import datetime, time
from typing import List, Optional

import hashlib

class BaseBlock:
    hash_algo: any = hashlib.sha256()

    @classmethod
    def update(cls, prev_block) -> bool:
        try:
            self.hash_algo.update(prev_block.dict())
            cls.hash = hash_algo.hexdigest()
        except:
            return False

        return True


class BlockModel(BaseModel, BaseBlock):
    login: str = Field(min_length=3, max_length=40)
    date: datetime
    ip: IPvAnyAddress
    status: str


class ActionBlogModel(BlockModel):
    data: dict


class Block(BlockModel):
    def __init__(self, status, login, date, ip):
        super().__init__(login, date, ip, status)

        self.hash = None


class SuperBlockModel(BaseModel, BaseBlock):
    data: any


class SuperBlock(SuperBlockModel):
    def __init__(self, open, action_log, close):
        super().__init__([open, action_log, close])

        self.hash = None

    def dict(self) -> dict:
        blocks_dict = {}
        dicts = [block.dict() for block in self.data]
        for d in dicts:
            blocks_dict.update(d)

        return block_dicts


if __name__=="__main__":
    pass
