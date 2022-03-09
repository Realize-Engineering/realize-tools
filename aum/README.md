# Introduction

This script uses realize to aggregate all accountValues across all institution
links under this app.

## Install Packages

```pip3 install -r requirements.txt```

## Environment Variables

Get your secret key from the realize [dashboard](https://www.realizefi.com/dashboard).

Bind your secret key to env vars via the following command:

```export REALIZE_SECRET_KEY=<dashboard_secret_key>```

## Run AUM Script

```python3 total-aum.py```
