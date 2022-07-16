import unittest

from Manager.blocks import *

class TestCreatingBlock(unittest.TestCase):
    def test_BlockModel(self):
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
              
        first_block = BlockModel(**first_variables)
        second_block = BlockModel(**variables)
        BaseBlock.update(second_block, first_block)
        
        variables.update({"hash":"4468aa6af062aafc79cb7fc8a62485f3ec8f3b7d58cf615ee68281581c132e70"})
        
        self.assertEqual(second_block.dict(), variables)
        

if __name__=="__main__":
    test = TestCreatingBlock()
    test.main()