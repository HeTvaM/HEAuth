import hashlib

from datetime import datetime
from random import sample, randint

from routes.db import DB
from blocks import ActionBlockModel, BlockModel, SuperBlockModel, BaseBlock
from tests.debug_loggger import Logger
#from db.connection import Connection
#from monogodb import connection

logger = Logger()

try:
    #STR_KEY = os.getenv(UNIQUE_KEY)
    #LOG_STATUS=os.getenv(LOG_STATUS)
    STR_KEY = "123456789"
    LOG_STATUS = "Пользовательская активность"
except NameError:
    pass


class BlockManager:
    hash_table = {}
    #db: Optional[Connection] = Connection('mongodb://localhost:27017/', 'blocks')
    db = DB()
    
    def is_token(self, token):
        logger.log("FIND TOKEN")
        return self._find_token(token)

    def new_request(self, token, data):
        if data.get("status") == "open":
            return self._create_token(
                *self._create_block(data)
            )
        
        return self._create_superblock(token, data)
        
    def init_primary_blocks(self):
        first_block = BlockModel(**{
            "timestamp": datetime.now(),
            "login": "admin",
            "ip": "0.0.0.0",
            "status": "primary"
        })
        
        first_block.hash = sample(STR_KEY, randint(0, len(STR_KEY)) )             
        self.db.add(first_block)
    
    def get_table(self, db):
        return self.db.print(db)

    def _create_superblock(self, token, data):
        open_block = self.db.get_last_block()
        close_block = BlockModel(**data)
        log_block = ActionBlockModel(data=self.hash_table[token])
        superblock = SuperBlockModel(
            blocks=[open_block, log_block, close_block]
        )
                
        # open_block = self.db.get_last_block(self.hash_table.get(token))
        # close_block = Block(CLOSE, *data)
        # log_block = Log(ActionBlogModel)
        # Superblock.update(superblock, self.db._open_table)
        # if self.db.close_table_add(superblock)

    def _create_block(self, data):
        logger.log(f"CREATE BLOCK \ \nDATA: {data}")
        
        block = BlockModel(**data)
        BaseBlock.update(block, self.db.get_last_block())
        id = self.db.add(block)
        # Block.update(block, db.prev())
        # id = self.db.add(block)
        return block, id

    def _create_token(self, block, id):
        logger.log(f"CREATE TOKEN \ \nBLOCK: {block.dict()} \nID: {id}")
        
        key = f"{str(block.dict())}{id} \
                {sample(STR_KEY, randint(0, len(STR_KEY)))}".encode()
        
        hash_algo = hashlib.sha512()
        hash_algo.update(key)
        token = hash_algo.hexdigest()
        self.hash_table[token] = [id]

        return token

    def _find_token(self, token):
        logger.log(f"TOKEN \ {self.hash_table.get(token)}")
        return not self.hash_table.get(token) is None

    def _log_action(self, token, action):
        return not self.hash_table[token].append(action) is None
