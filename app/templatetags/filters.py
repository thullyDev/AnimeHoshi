from django import template 
from datetime import datetime
import urllib

register = template.Library() 

@register.filter('cus_urlencode')
def cus_urlencode(text): return urllib.parse.quote(text.lower())

@register.filter('exp_filter')
def exp_filter(exp_time):
    if exp_time == "0": return False
    
    current_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S') 
    current_date = datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S') 
    vip_exp_date = datetime.strptime(exp_time, '%Y-%m-%d %H:%M:%S')
    dif = current_date-vip_exp_date
    date_str = str(dif)
    if date_str.find("days") == -1: return True
    temp_list = date_str.split(" days")
    exp_date = int(temp_list[0])
    print(exp_date)
    
    if exp_date < 30: return True
    
    return False

@register.filter('exp_parser')     
def exp_parser(exp_time):
    if exp_time == "0": return "No days"
   
    current_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S') 
    current_date = datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S') 
    vip_exp_date = datetime.strptime(exp_time, '%Y-%m-%d %H:%M:%S')
    dif = current_date-vip_exp_date
    date_str = str(dif)
    if date_str.find("days") == -1: return 1
    temp_list = date_str.split(" days")
    exp_date = int(temp_list[0])
    print(exp_date)
    
    if exp_date < 30: return exp_date
    
    return "Expired"

