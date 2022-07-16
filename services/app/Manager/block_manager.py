import hashlib

from blocks import ActionBlockModel, BlockModel, SuperBlockModel, BaseBlock
from random import sample, randint
from Routes.db import DB
#from db.connection import Connection
#from monogodb import connection


try:
    #STR_KEY = os.getenv(UNIQUE_KEY)
    #LOG_STATUS=os.getenv(LOG_STATUS)
    STR_KEY = "123456789"
    LOG_STATUS = "Пользовательская активность"
except NameError:
    pass


class BlockManager:
    hash_algo = hashlib.sha512()
    hash_table = {}
    #db: Optional[Connection] = Connection('mongodb://localhost:27017/', 'blocks')
    dB = DB()
    
    def is_token(self, token):
        return self._find_token(token)

    def new_request(self, data, status, token=None):
        # Need to change bc it's doesn't work correctly
        if status=="open":
            return self._create_token(
                self._create_block(data, status)
            )
        
        return self._create_superblock(token, data, status)
        
    def init_primary_blocks(self):
        pass

    def _create_superblock(self, token, data, status):
        open_block = self.db.get_last_block()
        close_block = BlockModel(status, data)
        log_block = ActionBlockModel(status, self.hash_table[token])
        superblock = SuperBlockModel(
            *[open_block, log_block, close_block]
        )
                
        # open_block = self.db.get_last_block(self.hash_table.get(token))
        # close_block = Block(CLOSE, *data)
        # log_block = Log(ActionBlogModel)

        # Superblock.update(superblock, self.db._open_table)
        # if self.db.close_table_add(superblock)

    def _create_block(self, data, status):
        block = BlockModel(status, *data)
        BaseBlock.update(block, self.db.get_last_block())
        id = self.db.add(block)
        # Block.update(block, db.prev())
        # id = self.db.add(block)
        return block, id

    def _create_token(self, status, block, id):
        key = f"{str(block.dict())}{id} \
                {sample(STR_KEY, randint(len(STR_KEY)))}"

        self.hash_algo.update(key)
        token = self.hash_algo.hexdigest()
        self.hash_table[token] = [id]

        return token

    def _find_token(self, token):
        return self.hash_table.get(token) is None

    def _log_action(self, token, action):
        return self.hash_table[token].append(action) is None
