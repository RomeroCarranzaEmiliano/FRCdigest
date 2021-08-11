"""
	scrapers.py
"""

import FRCdigest_webscrapers.api as scrapers
import discord

def departamento_sistemas_novedades(data):
    """
        Scraps the systems department website for news and creates a discord message
    """
    print(scrapers)
    news = scrapers.news_systems_department()

    if not news:
        return False

    response_list = []
    for a in news:
        colour = discord.Colour.from_rgb(100, 200, 100)
        description = a["content"]
        response = discord.Embed(title=a["title"], url=a["link"],
            description=description, color=colour)
        if len(a["images"]) > 0:
            response.set_image(url=a["images"][0])
        response_list.append(response)

    return response_list


dictionary = {
	"departamento_sistemas_novedades": departamento_sistemas_novedades,
}