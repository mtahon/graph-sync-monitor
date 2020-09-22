 	
#!/usr/bin/env python
import requests
import time
from datetime import datetime, timedelta 

base_url = 'https://api.thegraph.com/index-node/graphql'
payload = {"query" : "{indexingStatusForCurrentVersion(subgraphName: \"mtahon/uniswap-tokenlist\") { chains { latestBlock { hash number }}}}"}
target_block = 10581999
current_block = 0
interval = 10

def get_block_number():
    r = requests.post(base_url, json=payload)
    return int(r.json()['data']['indexingStatusForCurrentVersion']['chains'][0]['latestBlock']['number'])

while(current_block < target_block):
    previous_block = current_block
    current_block = get_block_number()
    if(previous_block >= current_block):
        continue
    speed = (current_block - previous_block) / interval
    remaining = (target_block - current_block) / speed
    target_date = datetime.now() + timedelta(seconds=remaining)
    print("Current Block: %i | Speed: %f b/s | Target: %s" % (current_block, speed, target_date))
    time.sleep(interval)