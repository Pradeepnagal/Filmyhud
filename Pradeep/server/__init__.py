from aiohttp import web

from .stream_routes import routes

async def web_server():

    web_app = web.Application(client_max_size=90000000)

    web_app.add_routes(routes)

    return web_app

