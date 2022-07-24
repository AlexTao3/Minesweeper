import pygame
from pygame.locals import *
import zgui
from zgui.guiglobal import *

# Minesweeper 
faceimg = pygame.image.load('face.bmp')
mineimg = pygame.image.load('mines.bmp')
numimg = pygame.image.load('num.bmp')
mineimgs = {}
minename = ["up","flag","?","touchmine","wrongflag","mine","dk",8,7,6,5,4,3,2,1,0]
for i in range(16):
        mineimgs[minename[i]] = mineimg.subsurface((0,i*16,16,16))
mineimgs['down'] = mineimgs[0].copy()
faceimgs = {}
facename = ["down","sunglasses","sad",":O","smile"]
for i in range(5):
        faceimgs[facename[i]] = faceimg.subsurface((0,i*24,24,24))

class Minesweeper(Window):
	"""a classic Minesweeper game, Window"""

	def __init__(self,**args):
		args['size'] = (200,280)
		args['title'] = "Minesweeper"
		args['resizeable'] = False
		args['bgcolor'] = (192,192,192)
		args['closeable'] = True
		super().__init__(**args)
		default = {}
		default['over'] = False
		default['minesnum'] = 10
		default['minesleft'] = 10
		default['inittime'] = time.time()
		default['timeused'] = 0
		default['minechanged'] = False
		self.setDefault(default,args)
		self['minesleft'] = self['minesnum']
		mainLay = VBoxLayout()
		topLay = HBoxLayout(sizehint= [10,15])
		mineLay = GridLayout(grid = (9,9),spacing=0,sizehint = [10,60])
		botLay = HBoxLayout()
		self.mines = []
		for i in range(9):
			l = []
			for j in range(9):
				m = Mine(number = (i,j))
				m.left.connect(self.leftClick)
				m.right.connect(self.rightClick)
				l.append(m)
			self.mines.append(l)
		for i in range(9):
			for j in range(9):
				mineLay.add(self.mines[i][j],(i,j))
		self.mineLeft = Label(text = self['minesleft'],fontsize = 20,textcolor = RED)
		self.face = MineFace()
		self.timeUse = Label(text = self['timeused'],fontsize = 20, textcolor = RED)

		topLay.add(self.mineLeft)
		topLay.add(self.face)
		topLay.add(self.timeUse)
		mainLay.add(topLay)
		mainLay.add(mineLay)
		self.setLayout(mainLay)
		self.restart()
		self.face.mouseLeftUp.connect(self.restart)

	def restart(self):
		"""restart game"""
		self['over'] = False
		self['started'] = False
		self['opened'] = 0
		self['minesleft'] = self['minesnum']
		self['minechanged'] = True
		self.face['state'] = 'smile'
		mine = random.sample(range(81), 10)
		for n,m in self.getMines():
			m['state'] = 'up'
			m['flag'] = ''
			if n in mine: m['flag'] = 'mine'
		d =[0,1, 1,1, 1,0, 1,-1, 0,-1, -1,-1, -1,0, -1,1]
		for x in range(9):
			for y in range(9):
				if not self.mines[x][y]['flag']:
					s = 0
					for i in range(8):
						tx,ty = x+d[i*2],y+d[i*2+1]
						if tx>=0 and ty>=0 and tx<9 and ty<9 and self.mines[tx][ty]['flag'] == 'mine':
							s+=1
					self.mines[x][y]['flag'] = s

	def getMines(self):
		"""generator of mines"""
		for i in range(9):
			for j in range(9):
				yield (i*9+j,self.mines[i][j])

	def update(self):
		self['layout'].update()
		t = 0
		if self['started']:
			t = int(time.time()-self['inittime'])
		if t!= self['timeused']: 
			if not self['over']:
				self['timeused'] = t
				self.timeUse.setText(t)
		if self['opened']+ self['minesnum'] == 9*9:
			self.gamewin()
		if self['minechanged']:
			self.mineLeft.setText(self['minesleft'])
			self['minechanged'] = False

	def startgame(self):
		"""start new game"""
		self['inittime'] = time.time()
		self['timeused'] = 0
		self['started'] = True

	def leftClick(self,num):
		"""if left click on a block"""
		if self['over']: return
		if not self['started']: self.startgame()
		x = num[0]
		y = num[1]
		m = self.mines[x][y]
		if m['state'] == 'flag': return
		if m['flag'] == 'mine':
			self.mines[x][y]['state'] = 'touchmine'
			self.gameover()
			return
		if m['state'] == 'up' or m['state'] == 'down':
			if isinstance(m['flag'],int):
				self['opened']+=1
		m['state'] = m['flag']
		if m['flag'] == 0:
			d =[0,1, 1,1, 1,0, 1,-1, 0,-1, -1,-1, -1,0, -1,1]
			for i in range(8):
				tx,ty = x+d[i*2],y+d[i*2+1]
				if tx>=0 and ty>=0 and tx<9 and ty<9 and self.mines[tx][ty]['state'] == 'up':
					self.mines[tx][ty].mouseLeftUp()

	def rightClick(self,num):
		"""if right click on a block"""
		if self['over']: return
		x = num[0]
		y = num[1]
		m = self.mines[x][y]
		if not m['state'] in ['up','flag','?']: return
		if m['state'] == 'up':
			m['state'] = 'flag'
			self['minesleft'] -=1
		elif m['state'] == 'flag':
			m['state'] = '?'
			self['minesleft'] +=1
		elif m['state'] == '?':
			m['state'] = 'up'
		self['minechanged'] = True

	def gamewin(self):
		"""when win the game"""
		self['opened'] = 0
		self['over'] = True
		self['started'] = False
		self.face['state'] = 'sunglasses'
		self.openAll()
		MessageBox(title = 'You Win',text = 'Good job!\nYou win!\nTime: %d second'%self['timeused'])

	def gameover(self):
		"""when lose the game"""
		self['over'] = True
		self['started'] = False
		self.face['state'] = 'sad'
		self.openAll()
		MessageBox(title = 'Game Over',text = 'HAHAHAAHHA\nGame Over!')

	def openAll(self):
		"""open all the mines"""
		for n,m in self.getMines():
			if m['state'] == 'flag' and m['flag']!='mine':
				m['state'] = 'wrongflag'
			elif m['flag'] == 'mine' and m['state']!='touchmine':
				m['state'] = 'mine'
			elif m['state'] != 'touchmine':
				m['state'] = m['flag']

class Mine(GUIObject):
	"""class of mine, GUIObject"""

	def __init__(self,**args):
		super().__init__(**args)
		default = {}
		default['state'] = 'up'
		default['flag'] = 0
		default['number'] = (0,0)
		self.setDefault(default,args)
		self.left = Signal()
		self.right = Signal()

		def mp():
			if self['state'] == 'up':
				self['state'] = 'down'

		def mu():
			self.left(self['number'])

		def ru():
			self.right(self['number'])
		self.mouseRightUp.connect(ru)
		self.mouseLeftUp.connect(mu)
		self.mouseLeftPress.connect(mp)
		self['size'] = (18,18)

	def resize(self,size):
		delta = pos_minus(size,self['size'])
		self['pos'] = pos_plus(self['pos'],(delta[0]//2,delta[1]//2))

	def update(self):
		if self['state'] == 'down':
			self['state'] = 'up'

	def draw(self,screen):
		screen.blit(mineimgs[self['state']],self['pos']) 

class MineFace(GUIObject):
	"""class of smiling face , GUIObject"""

	def __init__(self,**args):
		super().__init__(**args)
		default = {}
		default['filename'] = ""
		default['state'] = 'smile'
		self.setDefault(default,args)
		self['size'] = (24,24)

		def mp():
			if self['state'] == 'smile':
				self['state'] = 'down'
		self.mouseLeftPress.connect(mp)

	def update(self):
		if self['state'] == 'down':
			self['state'] = 'smile'

	def resize(self,size):	
		delta = pos_minus(size,self['size'])
		self['pos'] = pos_plus(self['pos'],(delta[0]//2,delta[1]//2))

	def draw(self,screen):
		screen.blit(faceimgs[self['state']],self['pos'])

class Main:

	def __init__(self):


		pygame.init()
		self.screen = pygame.display.set_mode((800,600))
		self.running = True
		self.gui = zgui.init(theme = 'WINDOWS8GRAY')

		pygame.display.set_caption("Minesweeper") 
		
		menuBar = MenuBar()
		statusBar = StatusBar()

		f = Menu(text = 'File')
		ms = MenuItem(text = 'New Minesweeper')
		ex = MenuItem(text = 'Exit')
		f.add(ms)
		f.add(ex)
		menuBar.add(f)

		h = Menu(text = 'Help')
		ab = MenuItem(text = 'About')
		h.add(ab)
		menuBar.add(h)

		self.gui.setStatusBar(statusBar)
		self.gui.setMenuBar(menuBar)
  
		self.gui.statusBar.setText("Minesweeper")

		def about():
			MessageBox(text = "Minesweeper\nCopyright: Zihao Zhang 2013",title = 'About')
		ab.mouseLeftUp.connect(about)

		def quit():
			mb = YesNoBox(text = 'Are you sure you want to exit?',title = 'Confirm')
			mb.yes.mouseLeftUp.connect(self.quit)

		self.gui.Quit.connect(quit)
		ex.mouseLeftUp.connect(quit)

		def newmine():
			self.gui.add(Minesweeper(),(60,60))
		ms.mouseLeftUp.connect(newmine)
		newmine()

		self.bg = pygame.transform.scale(pygame.image.load("win8.jpg").convert(),(800,600))


	def run(self):

		while self.running:
			self.screen.blit(self.bg,(0,0))
			evt = pygame.event.get()
			self.gui.update(evt)
			self.gui.draw(self.screen)
			pygame.display.flip()

		pygame.quit()

	def quit(self):
		self.running = False

if __name__ == '__main__':
	app = Main()
	app.run()
