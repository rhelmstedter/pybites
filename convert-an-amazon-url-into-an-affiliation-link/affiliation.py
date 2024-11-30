def generate_affiliation_link(url):
    item_id = url.split("dp/")[1].split("/")[0]
    return f"http://www.amazon.com/dp/{item_id}/?tag=pyb0f-20"
