import curses as nc

stdscr = nc.initscr()
nc.noecho()
tmap = [[" "," "," "," "," "],
	[" "," "," "," "," "],
	[" "," ","start"," "," "],
	[" "," "," "," "," "],
	[" "," "," "," "," "]]
mapx = 2
mapy = 2
emptyString = "The room is dark.\nYou went past the world boundaries.\nPlease don't do that.\nIt messes up the story.\n"

def recursive_read(file):
	with open(file.strip()) as f:
		lines = f.readlines()
		ret = []
		for line in lines:
			if line.find("include \"") == 0:
				file2 = line.split("\"")[1]
				ret.extend(recursive_read(file2))
			else:
				ret.append(line.replace("\n",""))
		ret.append("")
		return ret

def getMap(x,y):
	if len(tmap) <= y or y < 0:
		return emptyString
	if len(tmap[y]) <= x or x < 0:
		return emptyString
	if len(tmap[y][x].strip()) == 0:
		return emptyString
	return "\n".join(recursive_read("passages/{}.text".format(tmap[y][x])))

def clearScreen():
	stdscr.clearok(1)
	nc.setsyx(0,0)
	stdscr.refresh()

while 1:
	stdscr.clear()
	stdscr.addstr(getMap(mapx,mapy))
	stdscr.refresh()
	c = stdscr.getch()
	if c == ord("q"):
		break;
	if c == ord("w"):
		mapy = mapy - 1
	if c == ord("s"):
		mapy = mapy + 1
	if c == ord("a"):
		mapx = mapx - 1
	if c == ord("d"):
		mapx = mapx + 1
nc.endwin()
