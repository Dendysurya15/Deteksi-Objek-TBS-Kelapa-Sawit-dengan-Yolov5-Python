import os
import aiohttp
import asyncio
import datetime
from datetime import datetime, timedelta
import pytz
from pathlib import Path

tzInfo = pytz.timezone('Asia/Bangkok')
url = 'https://srs-ssms.com/post-py.php'
headers = {"content-type": "application/x-www-form-urlencoded",
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
timer = 20
log_dir = Path(os.getcwd() + '/log/log.TXT')

def read_text_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as z:
            content = z.readlines()
            try:
                payload = content[0][:-1]
                code = asyncio.get_event_loop().run_until_complete(post_count(payload))
                if  code == 99999 or len(content[0].strip()) == 0 or content[0] == '' or '\n' in content[0] or '\r\n' in content[0] or code == 200:
                    wr = open(file_path, "w")
                    for x in range(len(content)):
                        if x != 0:
                            wr.write(content[x])
                wr.close()
                print("Status : " + str(code) + " " + payload +".")
            except Exception as e:
                print("Errornya "+ str(e))
                #file kosong
                
async def post_count(params):
    try:
        paramArr = params.split(";")
        async with aiohttp.ClientSession() as session:
            param = {'count': str(paramArr[0]), 'timestamp': str(paramArr[1])}
            async with session.post(url,data=param) as resp:
                response = resp.status
    except:
        response = 99999
    return response

lastDate = datetime.now(tz=tzInfo)+timedelta(seconds=timer, minutes=0, hours=0)

while True:
    
    if datetime.now(tz=tzInfo) > lastDate:
        read_text_file(log_dir)
        lastDate = datetime.now(tz=tzInfo) + timedelta(seconds=timer, minutes=0, hours=0)