"""
write a parser to extract the product list with the following fields from the listing page into a JSON:

    Product Name
    Starting Letter, ex. "Adoption Readiness Tool" à "A"
    Description
    Free Trial / Demo Request URL
    Support Link URL
"""

import json


def parse_product_name_demo_url(l):
    print(l.split())

with open("Products A-Z _ Product Suites _ Micro Focus _ OpenText.html", "r") as f:
    # The product results start at "Results:" and this string only appears once in the file.
    for line in f:
        if "Results:" in line:
            break
    
    for i in range(4):        
        print(f.readline())
    

    # Parse product name and demo url:
    line = f.readline().split() # last element will be the url, everything else is the name of product
    demo_url = line[-1][1:-1] # slice the first and last character which is < or >
    line.pop()
    product_name = " ".join(line)
    print(product_name)
    print(demo_url)
    


