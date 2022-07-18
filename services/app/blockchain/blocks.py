import hashlib

from pydantic import BaseModel, Field, IPvAnyAddress
from datetime import datetime, time
from typing import List, Optional, Any


class BaseBlock:
    @staticmethod
    def update(cls, prev_block) -> bool:
        hash_algo = hashlib.sha256()
        data = str(prev_block.dict()).encode()
        try:
            hash_algo.update(data)
            cls.hash = hash_algo.hexdigest()
        except AttributeError:
            return False

        return True


class BlockModel(BaseModel, BaseBlock):
    timestamp: datetime
    login: str = Field(min_length=3, max_length=40)
    ip: str #IPvAnyAddress
    status: str
    hash: str = None


class ActionBlockModel(BlockModel):
    data: dict
        

class SuperBlockModel(BaseModel, BaseBlock):
    blocks: Any
    hash: str = None
    
    def dict(self) -> dict:
        blocks_dict = {}
        dicts = [block.dict() for block in self.blocks]
        for d in dicts:
            blocks_dict.update(d)

        return blocks_dict      


if __name__=="__main__":
    date = datetime.now()
    
    first_variables = {"login": "dbelyaev",
                       "date": date,
                       "ip": "",
                       "status": "open"
                       }
    
    variables = {"login": "dbelyaev",
                 "date": date,
                 "ip": "112.121.211.221",
                 "status": "open"
                 }
    
    variables_close = {"login": "dbelyaev",
                 "date": date,
                 "ip": "112.121.211.221",
                 "status": "close"
                 }
    
    variables_action = {"login": "dbelyaev",
                 "date": date,
                 "ip": "112.121.211.221",
                 "status": "action",
                 "data": {date:"DATA PERMISSION"}
                 }
    
    first_block = BlockModel(**first_variables)
    print(first_block.dict())
     
    Mblock = BlockModel(**variables)
    CloseBlock = BlockModel(**variables_close)
    ActionBlock = ActionBlockModel(**variables_action)
    
    BaseBlock.update(Mblock, first_block)
    BaseBlock.update(CloseBlock, Mblock)
    BaseBlock.update(ActionBlock, CloseBlock)
    
    super = SuperBlockModel(**{"blocks": [Mblock, ActionBlock, CloseBlock]})
    BaseBlock.update(super, first_block)
    
    print(Mblock.dict(), end="\n\n")
    
    print("SUPER", super.dict())
    