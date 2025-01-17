Andrew Montgomery - amontgom@uwaterloo.ca

# Task 1: Triangle Render
## Code (Python):
```python
import pygame # graphics rendering library
window = pygame.display.set_mode((720,720)) # create the window
def triangle(x,y,m,n): # function that draws a right angle triangle at (x,y) with height m and base n
	pygame.draw.line(window, (255,255,255), (x,y), (x,x+n))
	pygame.draw.line(window, (255,255,255), (x,y+n), (x+m,x+n))
	pygame.draw.line(window, (255,255,255), (x,y), (x+m,x+n))
while True:
	if pygame.event.peek(pygame.QUIT): # detect when window closes
		break
	triangle(0,0,3 * 100,4 * 100) # draw the triangle (zoomed in x100 for your viewing pleasure)
	pygame.display.flip() # update the display
```
## Output:
![alt text](<Pasted image 20241011224504.png>)

## Assumptions made:
- Triangle is right triangle with right angle on the left
- Triangle is not filled
- Triangle is at top left \[(0,0) in Pygame-ce\]
# Task 2: Parser 
## Code (Python):
```python
import json


output = []

with open("parser/Products A-Z _ Product Suites _ Micro Focus _ OpenText.html", "r") as f:
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

```

## Output:
```json
[
    {
        "Product Name": "Adoption Readiness Tool",
        "Starting Letter": "A",
        "Description": "An interactive e-Learning software platform to manage rapid content\ndevelopment, increase user adoption and accelerate ROI.",
        "Free Trial / Demo Request URL": "mailto:ART-Demo@microfocus.com",
        "Support Link URL": "https://www.microfocus.com/en-us/support/Adoption%20Readiness%20Tool%20(ART)",
        "Community URL": "https://community.microfocus.com/welcome_to_the_community/adoption-readiness-tool/"
    },
    {
        "Product Name": "ALM / Quality Center <https://www.microfocus.com/en-us/products/",
        "Starting Letter": "A",
        "Description": "Govern application lifecycle activities to ensure alignment with\nbusiness objective and quality standard.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/alm-quality-center/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "ALM Octane <https://www.microfocus.com/en-us/products/alm-octane/",
        "Starting Letter": "A",
        "Description": "High-quality application delivery at enterprise scale. For Agile, Hybrid\nor Traditional teams.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/alm-octane",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "ArcSight Intelligence <https://www.microfocus.com/en-us/products/",
        "Starting Letter": "A",
        "Description": "ArcSight Intelligence augments existing security tools and empowers\nsecurity operations teams to identify and respond to the threats that\nmatter.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/arcsight-intelligence/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "ArcSight Intelligence for",
        "Starting Letter": "A",
        "Description": "Advanced Behavioral Analytics tool for CrowdStrike that empowers\nsecurity operations teams to find and respond to insider & advanced\npersistent threats before it\u2019s too late.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/arcsight-intelligence-for-crowdstrike/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "ArcSight Recon <https://www.microfocus.com/en-us/products/",
        "Starting Letter": "A",
        "Description": "Implement a SIEM log management solution created for security analytics,\ninvestigation, and compliance.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/arcsight",
        "Support Link URL": "https://www.microfocus.com/en-us/support/ArcSight%20Recon",
        "Community URL": "https://community.microfocus.com/cyberres/arcsight/"
    },
    {
        "Product Name": "Asset Management X <https://www.microfocus.com/en-us/products/",
        "Starting Letter": "A",
        "Description": "Manage IT assets for improved costs.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/asset-management-software/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Cloud",
        "Starting Letter": "C",
        "Description": "Monitoring, capacity and performance management for virtualized environments",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/cloud-optimizer/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Content Manager Cloud <https://www.microfocus.com/en-us/products/",
        "Starting Letter": "C",
        "Description": "Flexible enterprise content management software - in the cloud,\ndelivered in a SaaS model.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/enterprise-content-management-saas/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Data Protector <https://www.microfocus.com/en-us/products/data-",
        "Starting Letter": "D",
        "Description": "Backup and disaster recovery for diverse, dynamic, and distributed\nenterprise.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/data",
        "Support Link URL": "https://community.microfocus.com/img/bandr/",
        "Community URL": "https://marketplace.microfocus.com/itom/category/all?product=data-protector"
    },
    {
        "Product Name": "Data Protector for Cloud Workloads <https://www.microfocus.com/en-",
        "Starting Letter": "D",
        "Description": "A modern backup protection solution, ensuring disaster recovery and fast\nransomware restore for Microsoft 365, containers, hypervisors, and cloud\nplatforms.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/data",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Dimensions RM <https://www.microfocus.com/en-us/products/",
        "Starting Letter": "D",
        "Description": "Requirements management solution that provides end-to-end traceability\nof processes",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/products/dimensions-rm/trial/",
        "Support Link URL": "https://www.microfocus.com/en-us/support/Dimensions%20RM",
        "Community URL": "https://community.microfocus.com/adtd/dimensionsrm/"
    },
    {
        "Product Name": "Enterprise Suite <https://www.microfocus.com/en-us/products/",
        "Starting Letter": "E",
        "Description": "Analysis, development, test, and deployment solutions for IBM z Systems",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/enterprise",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Filr",
        "Starting Letter": "F",
        "Description": "Provides secure file access and sharing from any device",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/filr/request-demo>contac",
        "Support Link URL": "https://www.microfocus.com/en-us/support/Filr",
        "Community URL": "https://community.microfocus.com/collaboration/filr/"
    },
    {
        "Product Name": "Fortify on Demand <https://www.microfocus.com/en-us/products/",
        "Starting Letter": "F",
        "Description": "Application Security as a managed service",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/application",
        "Support Link URL": "https://community.microfocus.com/cyberres/fortify/",
        "Community URL": "https://marketplace.microfocus.com/cyberres/category/all?product=fortify-on-demand"
    },
    {
        "Product Name": "Fortify WebInspect <https://www.microfocus.com/en-us/products/",
        "Starting Letter": "F",
        "Description": "Provides comprehensive dynamic analysis of complex web applications and\nservices",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/webinspect-dynamic-analysis-dast/request-demo",
        "Support Link URL": "https://www.microfocus.com/en-us/support/Fortify%20WebInspect",
        "Community URL": "https://community.microfocus.com/cyberres/fortify/"
    },
    {
        "Product Name": "HCMX FinOps Express <https://www.microfocus.com/en-us/products/",
        "Starting Letter": "H",
        "Description": "Optimize your cloud costs. Cut waste and control spend with Micro Focus\nHCMX FinOps Express.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/finops-express/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Hybrid Cloud Management X <https://www.microfocus.com/en-us/",
        "Starting Letter": "H",
        "Description": "Easier and enhanced multi cloud management. Deploy business customized\nsolutions with flexibility and speed.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/hybrid-cloud-management-x/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "IDOL <https://www.microfocus.com/en-us/products/information-data-",
        "Starting Letter": "I",
        "Description": "Securely access and analyze enterprise (and public) text, audio, and\nvideo data.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/information-data-analytics-idol/request-demo",
        "Support Link URL": "https://www.microfocus.com/en-us/support/IDOL",
        "Community URL": "https://community.microfocus.com/t5/IDOL/ct-p/IDOL"
    },
    {
        "Product Name": "Law Enforcement Media Analysis <https://www.microfocus.com/en-us/",
        "Starting Letter": "L",
        "Description": "Digital forensics for organizations processing video and image evidence\nwho need to identify and extract facts during an investigation \u2013 Powered\nby IDOL.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/law-enforcement-media-analysis/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "LoadRunner Cloud <https://www.microfocus.com/en-us/products/",
        "Starting Letter": "L",
        "Description": "Simple and scalable SaaS delivered performance testing solution.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/loadrunner",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "LoadRunner Enterprise <https://www.microfocus.com/en-us/products/",
        "Starting Letter": "L",
        "Description": "Cross-enterprise performance testing for multiple and concurrent testing\nprojects",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/loadrunner-enterprise/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "LoadRunner Professional <https://www.microfocus.com/en-us/",
        "Starting Letter": "L",
        "Description": "The premium, market leading performance testing solution for project teams.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/loadrunner",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "NetIQ Advanced Authentication <https://www.microfocus.com/",
        "Starting Letter": "N",
        "Description": "Move beyond username and passwords and securely protect data and\napplications",
        "Free Trial / Demo Request URL": "https://www.netiq.com/products/advanced-authentication",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "NetIQ Data Access Governance (DAG) <https://www.microfocus.com/en-",
        "Starting Letter": "N",
        "Description": "Expand identity and access management (IAM) to include unstructured data.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/data-access-governance/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Network Automation <https://www.microfocus.com/en-us/products/",
        "Starting Letter": "N",
        "Description": "Drive automated configuration, change and security compliance across\nyour enterprise network. The capabilities of Network Automation are also\nincluded in Network Operations Management.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/network-automation/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Network Node Manager i <https://www.microfocus.com/en-us/products/",
        "Starting Letter": "N",
        "Description": "Unifies fault, availability, and performance monitoring for networks.\nThe capabilities of Network Node Manager i are also included in Network\nOperations Management.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/network-node-manager-i-network-management-software/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Network Operations Management Suite <https://www.microfocus.com/",
        "Starting Letter": "N",
        "Description": "Monitor, manage, troubleshoot, automate, and ensure compliance for\ntraditional, virtual, and software-defined networks (SDN). Network\nOperations Management includes the functionality of Network Node Manager\ni, Network Automation, and more.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/network-operations-management-suite/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Open Source Select",
        "Starting Letter": "O",
        "Description": "See how Select Enterprise works and get answers on how this benefits\nyour organization.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/open-source-select-enterprise/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "OpenText Analytics Database Enterprise Edition <https://",
        "Starting Letter": "O",
        "Description": "Vertica Analytics Database is the leading unified analytics warehouse\nand data lake",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/analytics",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Operations Bridge <https://www.microfocus.com/en-us/products/",
        "Starting Letter": "O",
        "Description": "AIOps for Cloud Monitoring - Automated event and performance monitoring\nfor multi-cloud and on-premises environments as well as complete\napplication health management including synthetic and real user\napplication monitoring and diagnostics. The capabilities of Business\nProcess Monitor, Real User Monitor, and Diagnostics are included in\nOperations Bridge.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/operations-bridge/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Operations Bridge Integration",
        "Starting Letter": "O",
        "Description": "Integration of Operations Bridge to many 3rd party monitoring and\nticketing tools. Customers download here.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/operations",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Operations Bridge Integration Hub for",
        "Starting Letter": "O",
        "Description": "Integration of Operations Bridge to many 3rd party monitoring and\nticketing tools. Partners download here.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/operations",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Operations Bridge Manager <https://www.microfocus.com/en-us/",
        "Starting Letter": "O",
        "Description": "Operations Bridge Manager (OBM) is the core component of the Operations\nBridge, it automatically discovers and correlates data, event topology,\nand metrics. Data comes from agents and connectors.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/operations-bridge-manager/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Operations Orchestration with RPA <https://www.microfocus.com/en-",
        "Starting Letter": "O",
        "Description": "Orchestrate end-to-end IT processes with outstanding agility.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/operations-orchestration-it-process-automation/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Retain Unified Archiving <https://www.microfocus.com/en-us/",
        "Starting Letter": "R",
        "Description": "Archive all business communication for case assessment, search, and\neDiscovery.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/retain-unified-archiving/request-demo",
        "Support Link URL": "https://www.microfocus.com/en-us/support/Retain%20Unified%20Archiving",
        "Community URL": "https://community.microfocus.com/t5/Retain/ct-p/Retain"
    },
    {
        "Product Name": "Server Automation <https://www.microfocus.com/en-us/products/",
        "Starting Letter": "S",
        "Description": "Automate server lifecycle management across heterogeneous server\nenvironments.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/server-automation-software/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Service Management Automation X (SMAX) <https:// www.microfocus.com/en-us/products/service-management-automation-",
        "Starting Letter": "S",
        "Description": "Machine learning-based ITSM and ESM software to meet all your service\ndesk and IT service management needs.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/service",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "SiteScope <https://www.microfocus.com/en-us/products/sitescope-",
        "Starting Letter": "S",
        "Description": "Agentless application monitoring that provides heterogeneous and hybrid\nsupport, and quick time to value with easy installation and configuration.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/sitescope-application-monitoring/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "UFT Developer <https://www.microfocus.com/en-us/products/uft-",
        "Starting Letter": "U",
        "Description": "UFT Developer is a shift-left functional test automation tool that\nenables easy test creation using the IDE, language, and testing\nframeworks of choice",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/uft-developer",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "UFT Digital Lab <https://www.microfocus.com/en-us/products/uft-",
        "Starting Letter": "U",
        "Description": "A lab of real devices to help you build an app experience from real-\nworld insights",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/uft-digital-lab/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "UFT Mobile <https://www.microfocus.com/en-us/products/uft-mobile/",
        "Starting Letter": "U",
        "Description": "A lab of real devices to help you build an app experience from real-\nworld insights",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/uft-mobile/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "UFT One",
        "Starting Letter": "U",
        "Description": "UFT One automates functional testing for web, mobile, API, RPA, and\nenterprise application software, increasing test coverage from the UI to\nthe API.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/uft-one/free",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Universal Discovery and Universal CMDB <https:// www.microfocus.com/en-us/products/configuration-management-system-",
        "Starting Letter": "U",
        "Description": "Collects, stores, manages, updates, and shows data on infrastructure\nconfiguration",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/configuration-management-system-database/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Unstructured Data Analytics OEM SDK \u2013 Powered by IDOL <https:// www.microfocus.com/en-us/products/unstructured-data-analytics-oem-",
        "Starting Letter": "U",
        "Description": "Unstructured Data Analytics OEM SDK \u2013 Powered by IDOL",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/unstructured-data-analytics-oem-sdk/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "ValueEdge\u2122 Platform <https://www.opentext.com/products/valueedge-",
        "Starting Letter": "V",
        "Description": "Accelerate, monitor, and orchestrate digital value streams",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/valueedge",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "VM Explorer <https://www.microfocus.com/en-us/products/vm-server-",
        "Starting Letter": "V",
        "Description": "VM backup and replication for VMware vSphere and Microsoft Hyper-V\nenvironments.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/vm-server",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Voltage Fusion <https://www.microfocus.com/en-us/cyberres/data-",
        "Starting Letter": "V",
        "Description": "Quickly find, protect, and secure your sensitive and high-value data\nwith Voltage Fusion.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/voltage-file-analysis-suite/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Voltage Fusion <https://www.microfocus.com/en-us/cyberres/data-",
        "Starting Letter": "V",
        "Description": "Quickly find, protect, and secure your sensitive and high-value data\nwith Voltage Fusion.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/voltage-fusion/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Voltage SecureData Integrations for Snowflake <https://",
        "Starting Letter": "V",
        "Description": "Enabling high-scale, high-performance, and secure data analytics, data\nscience and data sharing.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/voltage-securedata-for-snowflake/request-demo",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "Voltage SecureMail <https://www.microfocus.com/en-us/products/",
        "Starting Letter": "V",
        "Description": "Achieving email security with an end-to-end email encryption solution\nwithout impacting the user experience.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/products/cloud-email",
        "Support Link URL": "https://www.microfocus.com/en-us/support/Voltage%20SecureMail",
        "Community URL": "https://community.microfocus.com/t5/Voltage/ct-p/Voltage"
    },
    {
        "Product Name": "Voltage SecureMail Cloud <https://www.microfocus.com/en-us/",
        "Starting Letter": "V",
        "Description": "SaaS service for the protection of your most sensitive information and\nyour email transition to Office 365.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/en-us/products/cloud-email",
        "Support Link URL": "",
        "Community URL": ""
    },
    {
        "Product Name": "ZENworks Suite <https://www.microfocus.com/en-us/products/",
        "Starting Letter": "Z",
        "Description": "ZENworks Suite helps you easily track, manage, and protect your endpoint\ndevices.",
        "Free Trial / Demo Request URL": "https://www.microfocus.com/products/zenworks/trial/",
        "Support Link URL": "",
        "Community URL": ""
    }
]
```
