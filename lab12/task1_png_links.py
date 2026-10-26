import requests
h = requests.get((d := "https://gsom.spbu.ru") + "/en/").content.decode()
open((u := d + h[h.rfind('"', 0, e := h.find(".png") + 4) + 1:e]).split("/")[-1], "wb").write(requests.get(u).content)
print(h.count(".png"), u)
