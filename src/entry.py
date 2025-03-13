from js import Response

async def on_fetch(request, env):
    return Response.new("Hi! I'm ridwaanhall")
