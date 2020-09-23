 	
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
start_block = get_block_number()
start_time = datetime.now()
current_block = start_block
time.sleep(interval)

while(current_block < target_block):
    # Get the latest indexed block
    try:
        current_block = get_block_number()
    except requests.exceptions.ConnectionError:
        print("Connection Error")
        time.sleep(interval)
        continue

    # If we are just starting and no progress, skip
    if current_block == start_block:
        continue

    # Compute the speed and remaining time
    current_time = datetime.now()
    speed = (current_block - start_block) / (current_time - start_time).seconds
    remaining = (target_block - current_block) / speed
    target_date = datetime.now() + timedelta(seconds=remaining)

    # Display the stats
    print("Last indexed block: %i | Speed: %f b/s | Target: %s" % (current_block, speed, target_date))
    time.sleep(interval)