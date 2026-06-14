import time
import datetime

def main():
    print("Keepalive job started.")
    while True:
        now = datetime.datetime.utcnow().isoformat()
        print(f"[{now}] still alive...")


if __name__ == "__main__":
    main()
