from aiohttp import web
import asyncio

routes = web.RouteTableDef()


@routes.get('/index')
async def getIndexCtx(req):
    print(req)
    return web.json_response({'status': 1, 'text': 'post successful!!!'}, status=200)


@routes.get('/sleep')
async def getIndexCtx(req):
    print(req)
    await asyncio.sleep(60)
    return web.json_response({'status': 1, 'text': 'post successful!!!'}, status=200)


@routes.post('/article')
async def postArticle(req):
    data = await req.json()
    print(data)
    return web.json_response({'status': 1, 'text': 'post successful!!!'}, status=503)


app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app, host='10.114.50.186', port=8080)
