from connection import Connection

# "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"

# block dictionary

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
    'company': 'elephants'
}
block_8 = {
    'ip': 'localhost',
    'company': 'elephantsHairy'
}

conn = Connection('mongodb://localhost:27017/', 'blocks', 'open', 'super')

conn.open_table.add_block(block)
conn.add_super_block(block_8)

'''
conn.add_open_block(block)
conn.add_open_block(block_1)
conn.add_open_block(block_2)

print(conn.get_last_open_block())

conn.add_super_block(block_7)
conn.add_super_block(block_8)

print(conn.get_last_super_block())
'''
