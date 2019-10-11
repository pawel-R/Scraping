import requests
from bs4 import BeautifulSoup


s = 0

while (True):

    url = f"https://www.x-kom.pl/g-4/c/1590-smartfony-i-telefony.html?page={s+1}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    container = soup.find_all(class_="sc-4el5v8-7 iPPysr sc-52s1mv-0 foJNzj")


    for k, v in enumerate(container):
        print("Product:")
        name = container[k].find("h3").string
        print(name)

        rate = container[k].find(class_="sc-4el5v8-16 kIMsrT sc-1u6l9jk-1 ixvhfp sc-673ayz-0 dfQSis")["title"]
        mark = rate[-3:]
        if mark[-1] == "ę":
            mark = 0
        else:
            mark = mark.replace(",", ".")
            mark = float(mark)

        print(f"\nRate: {mark}")

        print("\nDiscription:")
        discription = container[k].find(class_="sc-1vco2i8-0 sc-4el5v8-15 fLNKyj sc-1vco2i8-1 ZosGi")
        li = discription.find_all("li")
        for i in li:
            print(i.get_text())

        try:
            shipping = container[k].find(class_="sc-4el5v8-19 hqUOSY sc-1xk7jm0-2 fpNmST").get_text()
            print("\nShipping: Free")
        except:
            shipping = False
            print("\nShipping: not free")

        try:
            old_Price = container[k].find(class_="apyg3s-0 apyg3s-2 iFPESx").get_text()
            print(f"Old price: {old_Price}")

        except:
            old_Price = False

        new_Price = container[k].find(class_="apyg3s-0 apyg3s-3 loxMbz").get_text()

        if old_Price == False:
            print(f"Price: {new_Price}")

        else:
            print(f"New price: {new_Price}")

        if bool(old_Price) == True:
            x = float(old_Price[:-3].replace(",", ".").replace(" ", ""))
            y = float(new_Price[:-3].replace(",", ".").replace(" ", ""))

            discount = x - y
            print(f"Discount: {round(discount, 2)}")

        print("---------------------------------------")
        print()

    s += 1
