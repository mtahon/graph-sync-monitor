 	
#!/usr/bin/env python
import requests
import time
from datetime import datetime, timedelta 

base_url = 'https://api.thegraph.com/index-node/graphql'
payload = {"query" : "{indexingStatusForCurrentVersion(subgraphName: \"mtahon/uniswap-tokenlist\") { chains { latestBlock { hash number }}}}"}
target_block = 10581999
first_block = 0
interval = 10

# Get the current block number
def get_block_number():
    r = requests.post(base_url, json=payload)
    return int(r.json()['data']['indexingStatusForCurrentVersion']['chains'][0]['latestBlock']['number'])

# Define the start parameters
start_time = datetime.now()
start_block = get_block_number()
current_block = start_block

while(current_block < target_block):
    # Get the new block and time
    previous_block = current_block
    current_time = datetime.now()
    current_block = get_block_number()

    # Skip 
    if(previous_block >= current_block):
        print("No Progress")
        continue
    speed = (current_block - start_block) / (current_time - start_time).seconds
    remaining = (target_block - current_block) / speed
    target_date = datetime.now() + timedelta(seconds=remaining)
    print("Current Block: %i | Speed: %f b/s | Target: %s" % (current_block, speed, target_date))
    time.sleep(interval)