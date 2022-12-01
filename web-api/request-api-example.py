# JSON DATA PUSH API by Robert Prochowicz, great help from Henri-Francois Chadeisson and Scott Rigney
# Tested with MSTR 10.10 / 2018-01-29

import requests
import base64
import json



### Parameters ###
base_url = "https://pokeapi.co/api/v2/pokemon?limit=100&offset=0";
offset_api=0
limit_api=100

#### FUNCTIONS ###

def get_report(base_url):
    print("Getting report results...")
    header_gs = {'Accept': 'application/json'}    
    r = requests.get(base_url + "reports/", headers=header_gs)
    # r = requests.get('XXXX.getDataSetByFeedId', params={'feedId': feed_id}, auth=(username, passwd))

    if r.ok:
        print("Report results received...")        
        print("HTTP %i - %s" % (r.status_code, r.reason))
        return r.text
    else:
        print("HTTP %i - %s" % (r.status_code, r.reason))

def export_to_json(base_url):
    print("Exporting report results to JSON file...")
    r = get_report(base_url)
    text_file = open("report_results.json", "w", encoding="utf8")
    text_file.write(r)
    text_file.close()

def export_to_csv(base_url):
    print("Exporting report results to JSON file...")

    csv_file = open('report_results.csv', "w", encoding="utf8")
    csv_file.write("Attribute1, Attribute2, Attribute3, Metric1, Metric2"+"\n") #manually modify this CSV file header
    csv_file.close()

    #there are 3 attributes in my example; add/remove levels according to the number of attributes in your case
    r = get_report(base_url)
    report_parsed = json.loads(r)
    a1_list = report_parsed['result']['data']['root']['children']
    for a1 in a1_list:
        a1_val = a1['element']['name']
        a2_list=a1['children']
        for a2 in a2_list:
            a2_val=a2['element']['name']
            a3_list=a2['children']
            for a3 in a3_list:
                a3_val=a3['element']['name']
                metrics=a3['metrics']
                #print(metrics)
                #uncomment the line above in order to check metrics names; update metric names in 'csv_file.write' line below; in my case it is Cost and Revenue
                #there are 2 metric in this example, modify the script accordingly to the amount of metrics in your case
                csv_file = open('report_results.csv', "a", encoding="utf8")
                csv_file.write("'"+a1_val + "','" + a2_val + "','" + a3_val + "'," + str(metrics['Cost']['rv']) + "," + str(metrics['Revenue']['rv'])+"\n")
                csv_file.close()
    print("Export finished")

def main():    
    choice = None
    while choice != "0":
        print \
        ("""
        ---MENU---
        
        0 - Exit        
        1 - Export report results to JSON file
        2 - Export report results to CSV file
        """)

        choice = input("Your choice: ") # What To Do ???
        print()
    
        if choice == "0":
            print("Good bye!")   
        elif choice == "1":
            export_to_json(base_url)
        elif choice == "2":
            export_to_csv(base_url)
        else:
            print(" ### Wrong option ### ")

### Main program    
main()