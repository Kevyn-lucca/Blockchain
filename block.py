import hashlib as hasher
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
  
def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) + 
                str(self.timestamp) + 
                str(self.data) + 
                str(self.previous_hash))
        return sha.hexdigest()
  
def genesis_block():
        return Block(0, date.datetime.now(), "Genesis Block", "0")
 

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Eu sou o bloco: " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)
  
#Cria a blockchain e adiciona o block genesis
blockchain = [genesis_block]
previous_block = blockchain[0]

#Quantidade de blocos(apos o block genesis)
num_of_blocks = 20

#adiciona os blocos
for i in range(0, num_of_blocks):
    block_add = next_block(previous_block)
    blockchain.append(block_add)
    previous_block = block_add
  #Printa no terminal
    print ("Block #{} foi adicionado a blockchain.".format(block_add.index))
    print ("Hash: {}\n".format(block_add.hash)) 