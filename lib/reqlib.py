import time
from datetime import datetime
import requests
import re
import json
import os
import sys


class Reqlib():

    REQ = 0

    def __init__(self, produk):
        self.PRODUK = produk
        self.REQ = requests.Session()

    def get_prod(self):
        return self.PRODUK

    def get_harga(self):
        ret = []
        for i in range(0, len(self.PRODUK)):
            # for p in self.PRODUK:
            p = self.PRODUK[i]
            r = re.search(r"i\.(\d+)\.(\d+)", p["LINK"])
            shop_id, item_id = r[1], r[2]
            URL = f"https://shopee.co.id/api/v4/item/get?itemid={item_id}&shopid={shop_id}"
            HEAD = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
            }
            GET_DATA = self.REQ.get(URL, headers=HEAD)
            prod = GET_DATA.json()
            items = prod["data"]
            # print(items)
            harga = 0
            mdl = ""
            mode = []
            if "models" in items:
                model = items["models"]
                # print(model)
                for m in model:
                    mode.append(m["name"])
                    if m["stock"] > 0:
                        harga = int(m["price"]/100000)
                        mdl = m["name"]
                # print(json.dumps(model, sort_keys=True, indent=4))
            else:
                harga = int(items["price"]/100000)
            p["MODEL_ALL"] = mode
            p["MODEL_PROD"] = mdl
            p["PRICE"] = harga
            self.PRODUK[i] = p

        return self.PRODUK
