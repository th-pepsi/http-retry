import asyncio

import aiohttp

from retry import retry

routesPath = ['index', 'article', 'sleep']
herf = 'http://10.114.50.186:8080/'

@retry(count=2, interval=5)
async def requestAPI(path):
    async with aiohttp.ClientSession() as session:
        if path == 'article':
            payload = {
                "name": "John Doe",
                "age": 30,
                "email": "john.doe@example.com"
            }
            async with session.post(f'{herf}{path}', json=payload) as res:
                return res

        else:
            async with session.get(f'{herf}{path}') as res:
                return res


async def inputReq():
    while True:
        path = input('please enter which path you want to get:')
        path = path.strip()
        if path in routesPath:
            await requestAPI(path)
        elif path == 'q':
            raise Exception('you exit the process!')
            break
        else:
            print('you enter wrong path!')
            continue


if __name__ == '__main__':
    asyncio.run(inputReq())
