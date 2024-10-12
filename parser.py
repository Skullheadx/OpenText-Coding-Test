"""
write a parser to extract the product list with the following fields from the listing page into a JSON:

    Product Name
    Starting Letter, ex. "Adoption Readiness Tool" à "A"
    Description
    Free Trial / Demo Request URL
    Support Link URL
"""

import json


with open("Products A-Z _ Product Suites _ Micro Focus _ OpenText.html", "r") as f:
    def skip_lines(n):
        for _ in range(n):
            next(f)

    # The product results start at "Results:" and this string only appears once in the file.
    for line in f:
        if "Results:" in line:
            break
    
    # get to the information
    skip_lines(4)
    

    # Parse product name and demo url:
    line = f.readline().split() # last element will be the url, everything else is the name of product
    demo_url = line[-1][1:-1] # slice the first and last character which is < or >
    line.pop()
    product_name = " ".join(line)
    print(product_name)
    print(demo_url)

    # get to desc
    skip_lines(1)
    desc = ""
    while (True):
        line = f.readline()
        if "Get free trial" in line or "Request a demo" in line:
            break
        desc += line
    desc = desc.rstrip() # remove the trailing newlines
    print(desc)


    community_url = ""
    support_url = ""
    while(True):
        line = f.readline()
        if "Community" in line:
            community_url = line.split()[-1][1:] # remove the first character
            community_url += f.readline()[:-4] # remove the "> |" part at the end 
        elif "Support" in line:
            support_url = line.split()[-1][1:] # remove the first character
            support_url += f.readline()[:-4] # remove the "> |" part at the end 
        
        if community_url != "" and support_url != "":
            break

    print(community_url)
    print(support_url)






    


