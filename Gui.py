from Main import main, __version__ as ESVersion
from argparse import Namespace
from Rom import Sprite
from glob import glob
import random
from tkinter import Checkbutton, OptionMenu, Toplevel, LabelFrame, PhotoImage, Tk, X, Y, LEFT, RIGHT, BOTTOM, TOP, StringVar, IntVar, Frame, Label, W, E, Entry, Spinbox, Button, filedialog, messagebox
#from tkinter import *
#from tkinter.ttk import *


def guiMain(args=None):
    mainWindow = Tk()
    mainWindow.wm_title("Entrance Shuffle %s" % ESVersion)

    topFrame = Frame(mainWindow)
    rightHalfFrame = Frame(topFrame)
    checkBoxFrame = Frame(rightHalfFrame)

    createSpoilerVar = IntVar()
    createSpoilerCheckbutton = Checkbutton(checkBoxFrame, text="Create Spoiler Log", variable=createSpoilerVar)
    suppressRomVar = IntVar()
    suppressRomCheckbutton = Checkbutton(checkBoxFrame, text="Do not create patched Rom", variable=suppressRomVar)
    quickSwapVar = IntVar()
    quickSwapCheckbutton = Checkbutton(checkBoxFrame, text="Enabled L/R Item quickswapping", variable=quickSwapVar)
    fastMenuVar = IntVar()
    fastMenuCheckbutton = Checkbutton(checkBoxFrame, text="Enable instant menu", variable=fastMenuVar)
    keysanityVar = IntVar()
    keysanityCheckbutton = Checkbutton(checkBoxFrame, text="Keysanity (keys anywhere)", variable=keysanityVar)
    dungeonItemsVar = IntVar()
    dungeonItemsCheckbutton = Checkbutton(checkBoxFrame, text="Place Dungeon Items (Compasses/Maps)", onvalue=0, offvalue=1, variable=dungeonItemsVar)
    beatableOnlyVar = IntVar()
    beatableOnlyCheckbutton = Checkbutton(checkBoxFrame, text="Only ensure seed is beatable, not all items must be reachable", variable=beatableOnlyVar)
    shuffleGanonVar = IntVar()
    shuffleGanonCheckbutton = Checkbutton(checkBoxFrame, text="Include Ganon's Tower and Pyramid Hole in shuffle pool", variable=shuffleGanonVar)

    createSpoilerCheckbutton.pack(expand=True, anchor=W)
    suppressRomCheckbutton.pack(expand=True, anchor=W)
    quickSwapCheckbutton.pack(expand=True, anchor=W)
    fastMenuCheckbutton.pack(expand=True, anchor=W)
    keysanityCheckbutton.pack(expand=True, anchor=W)
    dungeonItemsCheckbutton.pack(expand=True, anchor=W)
    beatableOnlyCheckbutton.pack(expand=True, anchor=W)
    shuffleGanonCheckbutton.pack(expand=True, anchor=W)

    fileDialogFrame = Frame(rightHalfFrame)

    romDialogFrame = Frame(fileDialogFrame)
    baseRomLabel = Label(romDialogFrame, text='Base Rom')
    romVar = StringVar()
    romEntry = Entry(romDialogFrame, textvariable=romVar)

    def RomSelect():
        rom = filedialog.askopenfilename()
        romVar.set(rom)
    romSelectButton = Button(romDialogFrame, text='Select Rom', command=RomSelect)

    baseRomLabel.pack(side=LEFT)
    romEntry.pack(side=LEFT)
    romSelectButton.pack(side=LEFT)

    spriteDialogFrame = Frame(fileDialogFrame)
    baseSpriteLabel = Label(spriteDialogFrame, text='Link Sprite')
    spriteVar = StringVar()
    spriteEntry = Entry(spriteDialogFrame, textvariable=spriteVar)

    def SpriteSelect():
        #sprite = filedialog.askopenfilename()
        #spriteVar.set(sprite)
        SpriteSelector(Toplevel(mainWindow), spriteVar.set)

    spriteSelectButton = Button(spriteDialogFrame, text='Select Sprite', command=SpriteSelect)

    baseSpriteLabel.pack(side=LEFT)
    spriteEntry.pack(side=LEFT)
    spriteSelectButton.pack(side=LEFT)

    romDialogFrame.pack()
    spriteDialogFrame.pack()

    checkBoxFrame.pack()
    fileDialogFrame.pack()

    drowDownFrame = Frame(topFrame)

    modeFrame = Frame(drowDownFrame)
    modeVar = StringVar()
    modeVar.set('open')
    modeOptionMenu = OptionMenu(modeFrame, modeVar, 'standard', 'open', 'swordless')
    modeOptionMenu.pack(side=RIGHT)
    modeLabel = Label(modeFrame, text='Game Mode')
    modeLabel.pack(side=LEFT)

    logicFrame = Frame(drowDownFrame)
    logicVar = StringVar()
    logicVar.set('noglitches')
    logicOptionMenu = OptionMenu(logicFrame, logicVar, 'noglitches', 'minorglitches')
    logicOptionMenu.pack(side=RIGHT)
    logicLabel = Label(logicFrame, text='Game logic')
    logicLabel.pack(side=LEFT)

    goalFrame = Frame(drowDownFrame)
    goalVar = StringVar()
    goalVar.set('ganon')
    goalOptionMenu = OptionMenu(goalFrame, goalVar, 'ganon', 'pedestal', 'dungeons', 'triforcehunt', 'crystals')
    goalOptionMenu.pack(side=RIGHT)
    goalLabel = Label(goalFrame, text='Game goal')
    goalLabel.pack(side=LEFT)

    difficultyFrame = Frame(drowDownFrame)
    difficultyVar = StringVar()
    difficultyVar.set('normal')
    difficultyOptionMenu = OptionMenu(difficultyFrame, difficultyVar, 'easy', 'normal', 'hard', 'expert', 'insane')
    difficultyOptionMenu.pack(side=RIGHT)
    difficultyLabel = Label(difficultyFrame, text='Game difficulty')
    difficultyLabel.pack(side=LEFT)

    timerFrame = Frame(drowDownFrame)
    timerVar = StringVar()
    timerVar.set('none')
    timerOptionMenu = OptionMenu(timerFrame, timerVar, 'none', 'display', 'timed', 'timed-ohko', 'timed-countdown')
    timerOptionMenu.pack(side=RIGHT)
    timerLabel = Label(timerFrame, text='Timer setting')
    timerLabel.pack(side=LEFT)

    progressiveFrame = Frame(drowDownFrame)
    progressiveVar = StringVar()
    progressiveVar.set('on')
    progressiveOptionMenu = OptionMenu(progressiveFrame, progressiveVar, 'on', 'off', 'random')
    progressiveOptionMenu.pack(side=RIGHT)
    progressiveLabel = Label(progressiveFrame, text='Progressive equipment')
    progressiveLabel.pack(side=LEFT)

    algorithmFrame = Frame(drowDownFrame)
    algorithmVar = StringVar()
    algorithmVar.set('balanced')
    algorithmOptionMenu = OptionMenu(algorithmFrame, algorithmVar, 'freshness', 'flood', 'vt21', 'vt22', 'vt25', 'vt26', 'balanced')
    algorithmOptionMenu.pack(side=RIGHT)
    algorithmLabel = Label(algorithmFrame, text='Item distribution algorithm')
    algorithmLabel.pack(side=LEFT)

    shuffleFrame = Frame(drowDownFrame)
    shuffleVar = StringVar()
    shuffleVar.set('full')
    shuffleOptionMenu = OptionMenu(shuffleFrame, shuffleVar, 'vanilla', 'simple', 'restricted', 'full', 'madness', 'insanity', 'dungeonsfull', 'dungeonssimple')
    shuffleOptionMenu.pack(side=RIGHT)
    shuffleLabel = Label(shuffleFrame, text='Entrance shuffle algorithm')
    shuffleLabel.pack(side=LEFT)

    heartbeepFrame = Frame(drowDownFrame)
    heartbeepVar = StringVar()
    heartbeepVar.set('normal')
    heartbeepOptionMenu = OptionMenu(heartbeepFrame, heartbeepVar, 'normal', 'half', 'quarter', 'off')
    heartbeepOptionMenu.pack(side=RIGHT)
    heartbeepLabel = Label(heartbeepFrame, text='Heartbeep sound rate')
    heartbeepLabel.pack(side=LEFT)

    modeFrame.pack(expand=True, anchor=E)
    logicFrame.pack(expand=True, anchor=E)
    goalFrame.pack(expand=True, anchor=E)
    difficultyFrame.pack(expand=True, anchor=E)
    timerFrame.pack(expand=True, anchor=E)
    progressiveFrame.pack(expand=True, anchor=E)
    algorithmFrame.pack(expand=True, anchor=E)
    shuffleFrame.pack(expand=True, anchor=E)
    heartbeepFrame.pack(expand=True, anchor=E)

    bottomFrame = Frame(mainWindow)

    seedLabel = Label(bottomFrame, text='Seed #')
    seedVar = StringVar()
    seedEntry = Entry(bottomFrame, textvariable=seedVar)
    countLabel = Label(bottomFrame, text='Count')
    countVar = StringVar()
    countSpinbox = Spinbox(bottomFrame, from_=1, to=100, textvariable=countVar)

    def generateRom():
        guiargs = Namespace
        guiargs.seed = int(seedVar.get()) if seedVar.get() else None
        guiargs.count = int(countVar.get()) if countVar.get() != '1' else None
        guiargs.mode = modeVar.get()
        guiargs.logic = logicVar.get()
        guiargs.goal = goalVar.get()
        guiargs.difficulty = difficultyVar.get()
        guiargs.timer = timerVar.get()
        guiargs.progressive = progressiveVar.get()
        guiargs.algorithm = algorithmVar.get()
        guiargs.shuffle = shuffleVar.get()
        guiargs.heartbeep = heartbeepVar.get()
        guiargs.create_spoiler = bool(createSpoilerVar.get())
        guiargs.suppress_rom = bool(suppressRomVar.get())
        guiargs.keysanity = bool(keysanityVar.get())
        guiargs.nodungeonitems = bool(dungeonItemsVar.get())
        guiargs.beatableonly = bool(beatableOnlyVar.get())
        guiargs.fastmenu = bool(fastMenuVar.get())
        guiargs.quickswap = bool(quickSwapVar.get())
        guiargs.shuffleganon = bool(shuffleGanonVar.get())
        guiargs.rom = romVar.get()
        guiargs.jsonout = None
        guiargs.sprite = spriteVar.get() if spriteVar.get() else None
        try:
            if guiargs.count is not None:
                seed = guiargs.seed
                for i in range(guiargs.count):
                    main(seed=seed, args=guiargs)
                    seed = random.randint(0, 999999999)
            else:
                main(seed=guiargs.seed, args=guiargs)
        except Exception as e:
            messagebox.showerror(title="Error while creating seed", message=str(e))
        else:
            messagebox.showinfo(title="Success", message="Rom patched successfully")

    generateButton = Button(bottomFrame, text='Generate Patched Rom', command=generateRom)

    seedLabel.pack(side=LEFT)
    seedEntry.pack(side=LEFT)
    countLabel.pack(side=LEFT)
    countSpinbox.pack(side=LEFT)
    generateButton.pack(side=LEFT)

    drowDownFrame.pack(side=LEFT)
    rightHalfFrame.pack(side=RIGHT)
    topFrame.pack(side=TOP)
    bottomFrame.pack(side=BOTTOM)

    if args is not None:
        # load values from commandline args
        createSpoilerVar.set(int(args.create_spoiler))
        suppressRomVar.set(int(args.suppress_rom))
        keysanityVar.set(args.keysanity)
        if args.nodungeonitems:
            dungeonItemsVar.set(int(not args.nodungeonitems))
        beatableOnlyVar.set(int(args.beatableonly))
        fastMenuVar.set(int(args.fastmenu))
        quickSwapVar.set(int(args.quickswap))
        if args.count:
            countVar.set(str(args.count))
        if args.seed:
            seedVar.set(str(args.seed))
        modeVar.set(args.mode)
        difficultyVar.set(args.difficulty)
        timerVar.set(args.timer)
        progressiveVar.set(args.progressive)
        goalVar.set(args.goal)
        algorithmVar.set(args.algorithm)
        shuffleVar.set(args.shuffle)
        heartbeepVar.set(args.heartbeep)
        logicVar.set(args.logic)
        romVar.set(args.rom)
        shuffleGanonVar.set(args.shuffleganon)
        if args.sprite is not None:
            spriteVar.set(args.sprite)

    mainWindow.mainloop()

class SpriteSelector(object):
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback
        parent.wm_title("TAKE ANY ONE YOU WANT")
        parent['padx']=5
        parent['pady']=5

        self.icon_section('Official Sprites', 'sprites/official/*', 'Official Sprites not found. Click "Update Official Sprites" to download them.')
        self.icon_section('Unofficial Sprites', 'sprites/unofficial/*', 'Put sprites in the Sprites/Unofficial folder to have them appear here.')

        frame = Frame(parent)
        frame.pack(side=BOTTOM, fill=X, pady=5)

        button = Button(frame, text="Browse for file...", command=self.browse_for_sprite)
        button.pack(side=RIGHT, padx=(5,0))

        # todo: Actually implement this. Requires a yet-to-be coded API from VT
        button = Button(frame, text="Update Official Sprites")
        button.pack(side=RIGHT, padx=(5,0))

        button = Button(frame, text="Use Default Sprite", command=self.use_default_sprite)
        button.pack(side=LEFT)

    def icon_section(self, frame_label, path, no_results_label):
        frame = LabelFrame(self.parent, text=frame_label, padx=5, pady=5)
        frame.pack(side=TOP, fill=X)

        i=0
        for file in glob(path):
            image = get_image_for_sprite(file)
            if image is None: continue
            button = Button(frame, image=image, command=lambda file=file:self.select_sprite(file))
            button.image=image
            button.grid(row=i//16, column=i%16)
            i+=1

        if i==0:
            label = Label(frame, text="Put sprites in the Sprites/Unoffical folder to have them appear here.")
            label.pack()

    def browse_for_sprite(self):
        sprite = filedialog.askopenfilename()
        self.callback(sprite)
        self.parent.destroy()

    def use_default_sprite(self):
        self.callback("")
        self.parent.destroy()

    def select_sprite(self, spritename):
        self.callback(spritename)
        self.parent.destroy()

def get_image_for_sprite(filename):
    sprite = Sprite(filename)
    image = PhotoImage(height=24, width=16, palette="256/256/256")

    def color_to_hex(color):
        return "#{0:02X}{1:02X}{2:02X}".format(*color)

    def drawsprite(spr, pal_as_colors, offset):
        for y in range(len(spr)):
            for x in range(len(spr[y])):
                pal_index=spr[y][x]
                if pal_index:
                    color=pal_as_colors[pal_index-1]
                    image.put(color_to_hex(color),to=(x+offset[0],y+offset[1]))

    shadow_palette = [(40,40,40)]
    shadow = [
		[0,0,0,1,1,1,1,1,1,0,0,0],
		[0,1,1,1,1,1,1,1,1,1,1,0],
		[1,1,1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1],
		[0,1,1,1,1,1,1,1,1,1,1,0],
		[0,0,0,1,1,1,1,1,1,0,0,0],
	]

    drawsprite(shadow, shadow_palette, (2,17))

    palettes = sprite.decode_palette()
    body = sprite.decode16(0x4C0)
    drawsprite(body, palettes[0], (0,8))
    head = sprite.decode16(0x40)
    drawsprite(head, palettes[0], (0,0))

    return image.zoom(2)

if __name__ == '__main__':
    guiMain()
