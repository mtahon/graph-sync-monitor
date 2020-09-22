# The Graph - Syncronization Monitor

This simple Python tools monitor the syncronization of a subgraph and predicts a target date for syncronization.

It works by polling The Graph every 10s for the indexing status of a subgraph.

## Installation

Clone the repository:

```shell
git clone git@github.com:mtahon/graph-sync-monitor.git
```

Change directory:

```shell
cd graph-sync-monitor
```

Create a virtual environment:

```shell
python3 -m venv env
```

Activate the virtual environment:

```shell
source env/bin/activate
```

Install the dependencies

```shell
pip install -r requirements.txt
```

## Running the monitoring

Start the monitoring:

```shell
$ python sync.py
Current Block: 10527783 | Speed: 0.747518 b/s | Target: 2020-09-23 13:37:37.123809
Current Block: 10527791 | Speed: 0.747765 b/s | Target: 2020-09-23 13:37:12.830740
Current Block: 10527797 | Speed: 0.746723 b/s | Target: 2020-09-23 13:38:56.285456
Current Block: 10527800 | Speed: 0.744641 b/s | Target: 2020-09-23 13:42:25.478459
Current Block: 10527802 | Speed: 0.742115 b/s | Target: 2020-09-23 13:46:40.870269
```

It displays key metrics:

* Current Block being indexed
* Indexing Speed in Block per second, as an average since the monitoring started
* Target date to reach the requested block at the average indexing speed

After a few minutes the average indexing speed is more stable and the target date should not change much. The script can be stopped at this point with `CONTROL`+`C`.
