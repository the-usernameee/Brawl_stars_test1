from PIL import Image, ImageDraw, ImageFont
import brawlstats
from function import func
#this shit💩💩💩
def draw_outline(draw, x, y, text, font, text_color, outline_color="black",f=0):
    # Сначала рисуем обводку
    draw.text((x-1, y-1), text, font=font, fill=outline_color)
    draw.text((x+1, y-1), text, font=font, fill=outline_color)
    draw.text((x-1, y+1), text, font=font, fill=outline_color)
    draw.text((x+1, y+1), text, font=font, fill=outline_color)
    draw.text((x-1, y), text, font=font, fill=outline_color)
    draw.text((x+1, y), text, font=font, fill=outline_color)
    draw.text((x, y-1), text, font=font, fill=outline_color)
    draw.text((x, y+1), text, font=font, fill=outline_color)
    draw.text((x-2, y-1), text, font=font, fill=outline_color)
    draw.text((x-2, y), text, font=font, fill=outline_color)
    draw.text((x-2, y+1), text, font=font, fill=outline_color)
    draw.text((x-2, y+2), text, font=font, fill=outline_color)
    draw.text((x-1, y-2), text, font=font, fill=outline_color)
    draw.text((x-1, y-1), text, font=font, fill=outline_color)
    draw.text((x-1, y), text, font=font, fill=outline_color)
    draw.text((x-1, y+1), text, font=font, fill=outline_color)
    draw.text((x-1, y+2), text, font=font, fill=outline_color)
    draw.text((x, y-1), text, font=font, fill=outline_color)
    draw.text((x, y), text, font=font, fill=outline_color)
    draw.text((x, y+1), text, font=font, fill=outline_color)
    draw.text((x, y+2), text, font=font, fill=outline_color)
    draw.text((x+1, y-2), text, font=font, fill=outline_color)
    draw.text((x+1, y-1), text, font=font, fill=outline_color)
    draw.text((x+1, y), text, font=font, fill=outline_color)
    draw.text((x+1, y+1), text, font=font, fill=outline_color)
    draw.text((x+1, y+2), text, font=font, fill=outline_color)
    draw.text((x+2, y-1), text, font=font, fill=outline_color)
    draw.text((x+2, y), text, font=font, fill=outline_color)
    draw.text((x+2, y+1), text, font=font, fill=outline_color)
    draw.text((x+2, y+2), text, font=font, fill=outline_color)
    draw.text((x+2, y-2), text, font=font, fill=outline_color)
    draw.text((x+1, y-2), text, font=font, fill=outline_color)
    draw.text((x-1, y-2), text, font=font, fill=outline_color)
    draw.text((x-2, y-2), text, font=font, fill=outline_color)
    if f==0:
    	draw.text((x+2,y+8),text,font=font,fill=outline_color)
    	draw.text((x,y+8),text,font=font,fill=outline_color)
    else:
    	draw.text((x+2,y+6),text,font=font,fill=outline_color)
    	draw.text((x,y+6),text,font=font,fill=outline_color)
    draw.text((x, y), text, font=font, fill=text_color)

def hex_to_rgb(hex_color):
    hex_color = int(hex_color, 16)
    r = (hex_color >> 16) & 0xFF
    g = (hex_color >> 8) & 0xFF
    b = hex_color & 0xFF
    
    return (r, g, b)



clubs={"member":"Участник","senior":"Ветеран","vicePrisedent":"Вице-президент","president":"Президент"}
token=open("api_token.txt").read()
ID="9292YPVVL"
client=brawlstats.Client(token)
rgb_color="white"



try:
	player=dict(client.get_player(ID))
	if "name_color" in player:
		hex_color=player["name_color"]
		rgb_color=hex_to_rgb(hex_color)
	if len(player["club"]):
		club=dict(client.get_club(player["club"]["tag"]))
		for x in club["members"]:
			if x["tag"]==player["tag"]:
				club=(clubs[dict(x)["role"]],club["badge_id"],club["name"])
				print(club)
				break

except:
	print("данный id не найдет")
	exit(0)
print(rgb_color)
#assets
if player["highest_trophies"]<500:
	bg = Image.open('game_assets/bg/v1.png').convert("RGBA")
else:
	if player["trophies"]<500:
		bg = Image.open('game_assets/bg/v2.png').convert("RGBA")
	else:
		bg = Image.open('game_assets/bg/v3.png').convert("RGBA")
ghg=Image.open("game_assets/other/trophy_png.png")
bg.paste(ghg,(0,0),mask=ghg)
width,height=bg.size
#best brawler 
best_brawler_text1=Image.open("game_assets/other/rty59.png")
best_brawler={"highest_trophies":-1}
b=player["brawlers"]
for x in b:
	if x["highest_trophies"]> best_brawler["highest_trophies"]:
		best_brawler=x
brawler_id=best_brawler["id"]
best_b_pin=Image.open(f"game_assets/brawlers/pins_gg/{brawler_id}.png")
best_b_pin=best_b_pin.resize((150,150))
bg.paste(best_b_pin,(1445,425),mask=best_b_pin)
best_b_trophy=str(best_brawler["trophies"])
best_b_highest=str(best_brawler["highest_trophies"])
#шрифты
font_for_nicname = ImageFont.truetype("game_assets/other/brawl_stars_font.ttf", size=61)
font_for_trophy = ImageFont.truetype("game_assets/other/brawl_stars_font.ttf", size=38)
font_for_count= ImageFont.truetype("game_assets/other/brawl_stars_font.ttf",size=43)
font_for_club_name=ImageFont.truetype("game_assets/other/brawl_stars_font.ttf",size=38)
font_for_club_role=ImageFont.truetype("game_assets/other/brawl_stars_font.ttf",size=28)
font_for_tag=ImageFont.truetype("game_assets/other/brawl_stars_font.ttf",36)
#координаты данных
tag_coords=(975,366)
vs3_coords=(1896,508)
duo_coords=(1898,737)
solo_coords=(1896,623)

trophy_text_coords=(1082,622)
trophy_highest_coords=(1075,737)

best_b_trophy_coords=(1471,626)
best_b_highest_coords=(1467,738)

icon_coords=(971,159)
nicname_coords=(1250,182)
brawlers_count_coords=(1685,34)
club_name_coords=(1330,876)


# Текст для добавления
club=""
tag=player["tag"]
print(tag)
brawlers_count=f"{len(b)}/82"
solo=str(player["solo_victories"])
duo=str(player["duo_victories"])
vs3=str(player["3vs3_victories"])
name = player["name"]
trophies=str(player["trophies"])
trophies_highest=str(player["highest_trophies"])
# Создание объекта для рисования
draw = ImageDraw.Draw(bg)

# Добавление текста на изображение
draw_outline(draw,*tag_coords,tag,font_for_tag,(149,205,254),f=1)
draw_outline(draw,*brawlers_count_coords,brawlers_count,font_for_count,"white")
draw_outline(draw,*vs3_coords,vs3,font_for_trophy,"white")
draw_outline(draw,*duo_coords,duo,font_for_trophy,"white")
draw_outline(draw,*solo_coords,solo,font_for_trophy,"white")
draw_outline(draw,*best_b_trophy_coords,best_b_trophy,font_for_trophy,"white")
draw_outline(draw,*best_b_highest_coords,best_b_highest,font_for_trophy,"white")
draw.text(nicname_coords,player["name"],font=font_for_nicname,color=rgb_color)
draw_outline(draw,*nicname_coords,name,font_for_nicname,text_color=rgb_color)
draw_outline(draw,*trophy_text_coords, trophies, font_for_trophy,"white")
draw_outline(draw,*trophy_highest_coords,trophies_highest,font_for_trophy,"white")

#добавление иконки
icon_id=player["icon"]["id"]
icon=Image.open(f"game_assets/icons_brawl/{icon_id}.png")
a3=209
icon=icon.resize((a3,a3),Image.BOX)
bg.paste(icon,icon_coords)
bg.paste(best_brawler_text1,(-13,0),mask=best_brawler_text1)
if club:
	club_icon_coords=(1192,866)
	club_role_coords=(1333,917)
	
	club_icon=Image.open(f"game_assets/club/icons/{club[1]}.webp")
	club_icon=club_icon.resize((103,116),Image.BOX)
	club_name=club[2]
	club_role=club[0]
	draw.text(club_role_coords,club_role,font=font_for_club_role,fill=(32, 32, 41))
	draw.text(club_name_coords, club_name, font=font_for_club_name, fill="white")
	bg.paste(club_icon,club_icon_coords,mask=club_icon)
else:
	club_name="Не в клубе"
	draw.text(club_name_coords, club_name, font=font_for_club_name, fill="white")
brawler=Image.open(f"game_assets/brawlers/models/{brawler_id}.png")
bg.paste(brawler,(0,0),mask=brawler)

af=func(trophies,0)
Y1=Image.open(af[0])
Y2=Image.open(af[1])
bg.paste(Y1,(0,0),mask=Y1)
bg.paste(Y2,(0,0),mask=Y2)
ar=func(trophies_highest,1)
Y1=Image.open(ar[0])
Y2=Image.open(ar[1])
bg.paste(Y1,(0,0),mask=Y1)
bg.paste(Y2,(0,0),mask=Y2)
bg.save('output/profile.png')