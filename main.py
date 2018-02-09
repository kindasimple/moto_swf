#!/usr/bin/env python

if __name__ == "__main__":
    from service.client import get_client
    print(get_client("http://localhost:5000"))
