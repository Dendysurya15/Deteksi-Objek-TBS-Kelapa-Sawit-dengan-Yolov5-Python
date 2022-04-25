import aiohttp
import asyncio
import pytz
import datetime
from datetime import datetime
tzInfo = pytz.timezone('Asia/Bangkok')
payload = {'count': '50', 'timestamp': '2022-04-05 08:31:36'}
url = 'https://srs-ssms.com/post-py.php'

async def post_count(params):
    async with aiohttp.ClientSession() as session:
        params = {'count': str(70), 'timestamp': datetime.now(tz=tzInfo).strftime("%Y-%m-%d %H:%M:%S")}
        async with session.post(url,data=params) as resp:
            response = resp.status
            return response
            
x = asyncio.get_event_loop().run_until_complete(post_count(payload))
print(str(x))