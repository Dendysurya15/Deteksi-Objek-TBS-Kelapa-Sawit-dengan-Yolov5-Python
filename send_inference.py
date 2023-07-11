import os
from pprint import pprint
import aiohttp
import asyncio
import datetime
from datetime import datetime, timedelta
import pytz
from pathlib import Path

tzInfo = pytz.timezone('Asia/Bangkok')
url = 'https://srs-ssms.com/post-py-sampling.php'
headers = {"content-type": "application/x-www-form-urlencoded",
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
timer = 20
log_dir = Path(os.getcwd() + '/log_inference_sampling/log_inference.TXT')

def read_text_file(file_path,timestamp):
    if os.path.exists(file_path):
        with open(file_path, 'r') as z:
            content = z.readlines()
            try:
                payload = content[0][:-1]
                code = asyncio.get_event_loop().run_until_complete(post_count(payload))


                print(code)
                if  code == 99999 or len(content[0].strip()) == 0 or content[0] == '' or '\n' in content[0] or '\r\n' in content[0] or code == 200:
                    wr = open(file_path, "w")
                    for x in range(len(content)):
                        if x != 0:
                            wr.write(content[x])
                wr.close()
                print("Status : " + str(code) + " " + payload +".")
            except Exception as e:
                # code = asyncio.get_event_loop().run_until_complete(post_count('-;-;-;-;-;-;0;0;0;0;0;0;0;'+timestamp+';' + timestamp))
                # print(str(code))
                print("Errornya "+ str(e))
                #file kosong
                
async def post_count(params):
    try:

        paramArr = params.split(";")

        async with aiohttp.ClientSession() as session:
            param = {'no_tiket': str(paramArr[0]),'no_plat': str(paramArr[1]),'bisnis_unit': str(paramArr[2]),'divisi': str(paramArr[3]),'blok': str(paramArr[4]), 'status': str(paramArr[5]), 'ripe': str(paramArr[6]), 'unripe': str(paramArr[7]), 'overripe': str(paramArr[8]), 'empty_bunch': str(paramArr[9]), 'abnormal': str(paramArr[10])
            , 'kastrasi': str(paramArr[11]), 'tp': str(paramArr[12]), 'waktu_mulai': str(paramArr[13]), 'waktu_selesai': str(paramArr[14])}
            async with session.post(url,data=param) as resp:
                response = resp.status

            # print(param)
    except:
        response = 99999
    return response

lastDate = datetime.now(tz=tzInfo)+timedelta(seconds=timer, minutes=0, hours=0)

while True:
    
    if datetime.now(tz=tzInfo) > lastDate:
        read_text_file(log_dir,datetime.now(tz=tzInfo).strftime("%Y-%m-%d %H:%M:%S"))
        lastDate = datetime.now(tz=tzInfo) + timedelta(seconds=timer, minutes=0, hours=0)