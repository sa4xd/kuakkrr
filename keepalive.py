name: Keepalive Python

on:
  workflow_dispatch:   # 手动触发
  schedule:
    - cron: "0 5 * * *"  

jobs:
  keepalive:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install deps (if any)
        run: |
          pip install -U pip
          # pip install -r requirements.txt  # 如果有依赖就打开

      - name: Run keepalive script
        run: |
          python keepalive.py
