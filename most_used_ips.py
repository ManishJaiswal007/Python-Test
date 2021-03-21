import pandas as pd 
from IPy import IP



def get_top_client_ips(file_name,limit):

    # Using readlines()
    file1 = open(file_name, 'r')
    Lines = file1.readlines()
     
    count = 0
    ips=[]
    # Strips the newline character
    for line in Lines:
        ip=line.split('- -')[0]
        ips.append(ip)
    
    ips_df = pd.DataFrame(ips,columns=['ip_add'])
    df = ips_df.groupby('ip_add').ip_add.agg({'count':['count']}).reset_index()
    df.columns = df.columns.droplevel(1)
    df2 = df.sort_values("count",ascending=0)['ip_add'][:limit]
    return [IP(x).strNormal() for x in df2]
