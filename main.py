import requests

url = "https://apigateway.test-hub2bc.com/kedu/12"

payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0',
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',
  'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZDAzMDZiN2EyYzlkZjlkNzgzZTMxNDQ1YjUyNTNiM2I2MmFjYzAzYWYzMmI1YWQ1NDM4YjVkYzRmODA2NzllZDlmYWM5OGQ0MWQwNjY4N2IiLCJpYXQiOjE2NTA0NjUwNTgsIm5iZiI6MTY1MDQ2NTA1OCwiZXhwIjoxNjgyMDAxMDU4LCJzdWIiOiIxNzY5Iiwic2NvcGVzIjpbXX0.XF3q2BX-xIePbtI79NPLSaZyi5UeiDV6AF9o7rsSRIQJ5XD56hT5EyF3Ogf10KvudWWrZQQeyeZl3ONSgpACT99Y-FBWz3suDh0m3R-_uj5Ke1BtVbdnMmAPSbx5uR2XIPr2KQBlBlQ0_SfU2byfLuxsIKFuM0wS5wFEsSYUiwlXT81CSZXMVr3Gm_HJmT2g5r1Afgd1fPkOJCefTFgoQvrMy2n3VMyLZitMyMMFd9SKhfiyZQk8jCSmhvobxnpN4ou1x8wHMk9JNOxPihytarr8uTuy6rnAHZ7HuK1yEQu5ybpMueWRQjKXR2iM2gPJA5rdMJ-YTRKlQpXLYVMBmHI-8md1Ge4TFiCtMT5HzZgfnqWWVKiDJ7DAY1n3PxwO14cMbHqJsWtKCjcDOt-pxgX5E78-I_ETs3yc2z9QYUpZ9gQx3vQ92Da6nvWR8UM96YAC4MM9rPrioDD__zejWCZOzNQKP8sBu5Wm6MNSnmGsOVgP7oAjx2k-nsNO4KDwYc4oL75Yk3QD8M5nU7zbYm2k5y39VTVHAd5f8TAr9C7pKFuu98wE4ev5Fcr9rBlm36IknTGu1P6gJz7eVglZ0mga0eDUO_ffeAEffCCVyL8QE5osMTrO-fXaZzmhGbjNY54X6wYL6qQg0ydw-kcadYXPNBjH4onn1Z5aveOkW9o',
  'BaseParent': '$2y$10$qzd35FDvG4LLks9bEsDPtOrj9kgj7YYbFd81yWgEBTsi.skvyO1W',
  'Parent': '$2y$10$qzd35FDvG4LLks9bEsDPtOrj9kgj7YYbFd81yWgEBTsi.skvyO1W',
  'ServiceParent': '11235813',
  'Person': '4116',
  'Origin': 'https://test-hub2bc.com',
  'DNT': '1',
  'Connection': 'keep-alive',
  'Referer': 'https://test-hub2bc.com/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'TE': 'trailers',
  'Cookie': 'XSRF-TOKEN=eyJpdiI6IkVQNE50ekZna3VmY3ZJcmw1OStpd1E9PSIsInZhbHVlIjoiQ1hYMkd4TDZ1c25peG82clVSRHNFQjRBbFpiQitwckRWT09Ca0NIT0RMdHZKWlNtdHg0Sm1NZVlFbGtRbXJIRGJVQy9SWVpwdDQ0aVdrNC94bDRzaTFSZVloUXFzM09NQlBoazV0bE5aZldRSnJ5OFFobEZFT3JTa01tRXpacVEiLCJtYWMiOiI5ZGZlZmIyNzAwMGE3YjMxZDg0N2RjZTdiNzQ4ZmI3YmJlMTYxMmZlZTYxYTc4Yjc5YjRjMDUyZGIxMTJiMGMzIn0%3D; apigateway_session=eyJpdiI6Ik5ZdGxSTGJkWCtRdlNEWFdJMGVmMkE9PSIsInZhbHVlIjoid3p0U0RscVBZa2c5RjJkUFU5TFhmMTQ1a2MrZmJXdVkxcG9MQUN4NloxbDNIK3Zoa2lucmZrMlowR3pDOUkvc3RzSnZQbEQ1aGdXV2dLOGxmcE52c003K204ZWl2VDhMcUwxZU82WDRJMGtIMDQwMGM1ZlJMcmtHbGlJTnhCNzgiLCJtYWMiOiIyYjY4NjIxYjlmN2NjYmE0MzRiZjdmMTQ1NGY4N2UxNjBhMjExZjczZWRjODIwMTY4N2RkMDBmMzJhMjI1NjU1In0%3D'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)