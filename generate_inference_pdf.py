import os
from pprint import pprint
import aiohttp
import asyncio
import datetime
from datetime import datetime, timedelta
import pytz
from pathlib import Path

tzInfo = pytz.timezone('Asia/Bangkok')
url = 'https://srs-ssms.com/grading_ai/generate_inference_pdf.php'
headers = {"content-type": "application/x-www-form-urlencoded",
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
timer = 20
log_dir = Path(os.getcwd() + '/log_inference_sampling/log.TXT')
arr = []

async def main():
    if os.path.exists(log_dir):
        with open(log_dir, 'r') as z:
            content = z.readlines()
            # try:
            payload = content[0].split(";")
            code = asyncio.get_event_loop().run_until_complete(
                
                async with aiohttp.ClientSession() as session:
                    param = {'unripe': str(payload[0]),'ripe': str(payload[1]),'overripe': str(payload[2]),'empty_bunch': str(payload[3]),'abnormal': str(payload[4]), 'timestamp': str(payload[5])}

                    print(param)
            )
            # for item in content:
            #     arr.append(item.split(";"))
            # print(payload)
            
    async def post_count(params):
        try:
        
                # async with session.post(url,data=param) as resp:
                #     response = resp.status
        except:
            response = 99999
        return response
            # print(content[0])
                # code = asyncio.get_event_loop().run_until_complete(post_count(payload))
                # if  code == 99999 or len(content[0].strip()) == 0 or content[0] == '' or '\n' in content[0] or '\r\n' in content[0] or code == 200:
                #     wr = open(log_dir, "w")
                #     for x in range(len(content)):
                #         if x != 0:
                #             wr.write(content[x])
                # wr.close()
                # print("Status : " + str(code) + " " + payload +".")
            # except Exception as e:
                # code = asyncio.get_event_loop().run_until_complete(post_count('0;0;0;0;0;'+timestamp))
                # print(str(code))
                # print("Errornya "+ str(e))
                #file kosong