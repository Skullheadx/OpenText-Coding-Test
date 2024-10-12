"""
write a parser to extract the product list with the following fields from the listing page into a JSON:

    Product Name
    Starting Letter, ex. "Adoption Readiness Tool" à "A"
    Description
    Free Trial / Demo Request URL
    Support Link URL
"""
import json


output = []

with open("Products A-Z _ Product Suites _ Micro Focus _ OpenText.html", "r") as f:
    text = f.read().split("\n\n\n")[4:-4] # data starts at 4th split, and ends at 4th last split.

    for product in text:
        product_name = ""
        desc = ""
        free_demo_trial_url = ""
        community_url = ""
        support_url = ""

        for i, line in enumerate(product.split("\n\n")):
            if i == 0: # first is always name/url NOTE: it is possible to get the url, but was not specified in the requirements
                product_name = " ".join(line.split()[:-1]) # last element will be the url, everything else is the name of product
            elif i == 1: # second is always desc
                description = line[:]
            elif "Get free trial" in line:
                free_demo_trial_url = line.split()[3][1:-1]
            elif "Request a demo" in line:
                free_demo_trial_url = "".join(line.split()[3:5])[1:-1]
            elif "Community" in line or "Support" in line: # community and support always together, so one is redundant
                tmp = line.split(' |') # furthermore, community is always before support
                community_url = "".join(tmp[0].split()[1:3])[1:-1] # have to perform surgery to reconnect the links and remove <>
                support_url = "".join(tmp[1].split()[1:3])[1:-1]

        data_point = {
            "Product Name": product_name,
            "Starting Letter": product_name[0].upper(),
            "Description": description,
            "Free Trial / Demo Request URL": free_demo_trial_url,
            "Support Link URL": support_url,
            "Community URL": community_url
        }
        output.append(data_point)

json_object = json.dumps(output, indent=4) # convert to json

with open("data.json", "w") as outfile: # create json file for output
    outfile.write(json_object)
