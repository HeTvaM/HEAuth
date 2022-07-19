from connection import Connection
import asyncio

block = {
    'ip': 'localhost',
}
block_1 = {
    'ip': 'localhost1',
}
block_2 = {
    'ip': 'localhost2',
}
block_3 = {
    'ip': 'localhost3',
}
block_4 = {
    'ip': 'localhost4',
}
block_5 = {
    'ip': 'localhost5',
}
block_6 = {
    'ip': 'localhost6',
}
block_7 = {
    'ip': 'localhost',
    'company': 'elephants',
    'token': 1000
}
block_8 = {
    'ip': 'localhost',
    'company': 'elephantsHairy',
    'token': 9560649353045
}

conn = Connection('mongodb://localhost:27017/', 'blocks', 'open', 'super')
# print(asyncio.run(conn.add_block('open', block_7)))
# print(asyncio.run(conn.add_block('super', block_1)))
# asyncio.run(conn.add_block('open', block_8))
# print(asyncio.run(conn.verify(9560649353045)))
# print(asyncio.run(conn.verify(1001)))
# a = asyncio.run(conn.search_by_id('open', '62d51cb7eda97ec74683b895'))
# print(a)
# asyncio.run(conn.delete_block('open', '62d51cb7eda97ec74683b895'))
# collection = asyncio.run(conn.show_table('open')))
# print(asyncio.run(conn.get_last_block('open')))