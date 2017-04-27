from collections import Counter

def get_domain(email_address):
 """split on '@' and return the last piece"""
 #lower() 轉為小寫
 #.split("@")[-1] 取@後面的資料
 return email_address.lower().split("@")[-1]

with open('email.txt', 'r') as f:
 domain_counts = Counter(get_domain(line.strip())
 for line in f
 if "@" in line)
 #資料理有@就放進line處理

 print domain_counts
