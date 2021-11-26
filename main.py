import pyfiglet
from lib.reqlib import *
from lib.selenlib import *

ascii_banner = pyfiglet.figlet_format("BOTSHOPEEBOT")
start_time = time.time()

# INIT REQUEST
produk = [
    {
        "LINK": "https://shopee.co.id/HANDBAGKU-TAS-LEVEL-URBAN-VILA-WAISTBAG-FANNY-PACK-PRIA-FASHION-SELEMPANG-PINGGANG-DISTRO-KOREA-i.4785324.5761467561",
        "MODEL_PROD": "L",
        "INIT_HARGA": 14000,
        "PRICE": 0
    }
]
reql = Reqlib(produk)


# INIT SELENIUM
DRIVER_PATH = "C:\\Users\\ASUS\\Documents\\backupHTDOCS\\Tutorial\\my-project\\chromedriver.exe"
user_data_dir = "C:\\Users\\ASUS\\AppData\\Local\\Google\\Chrome\\User Data"
selen = Selenlib(DRIVER_PATH, user_data_dir)


def main():
    print(ascii_banner)
    # a = reql.get_harga()
    # print(a)
    selen.open_link(produk[0]["LINK"])
    print(" ")
    prod = {}
    while True:
        prod = reql.get_harga()[0]
        harga = prod["PRICE"]
        if harga == None or harga == 0:
            selen.driver.quit()
            sys.exit("Harga None!!")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S:%f")
        print(f"* [{current_time}] -> {harga}", end="\r")
        if harga <= prod["INIT_HARGA"]:
            break

    print(" ")
    # selen.beli_sekarang(prod["MODEL_PROD"], prod["MODEL_ALL"])
    selen.beli_sekarang("WB.VILA -  MARON", prod["MODEL_ALL"])


if __name__ == '__main__':
    main()
