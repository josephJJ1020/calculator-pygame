import pygame
import sys

pygame.init()
font = pygame.font.SysFont("rockwell", 100)
opfont = pygame.font.SysFont('arial', 50)

icon = pygame.image.load("calculator.png")

ss = sw, sh = 500, 500

screen = pygame.display.set_mode(ss)
pygame.display.set_caption("Calculator")
pygame.display.set_icon(icon)

operation = ""  # text displayed on calc
result = ""  # answer
size = 100 # size of squares

operators = ['=', 'C', '+', '-', '*', '/', '(', ')', '.']
operatorlist = []

numcolor = pygame.Color("green")

class NumBox:
    def __init__(self, x, y, numcolor, number, l=size, h=size):
        self.x = x
        self.y = y
        self.color = numcolor
        self.number = number
        self.l, self.h = l, h
        self.box = pygame.draw.rect(screen, pygame.Color("green"), (self.x, self.y, self.l, self.h), width=1, border_radius=5)

        num = str(self.number)
        numtext = font.render(num, True, self.color)
        screen.blit(numtext, (self.x + 20, self.y - 10, size, size))

    def collidecheck(self, cursor):
        if self.box.collidepoint(cursor):
            self.color = pygame.Color("white")
            num = str(self.number)
            numtext = font.render(num, True, self.color)
            screen.blit(numtext, (self.x + 20, self.y - 10, size, size))


        else:
            self.color = pygame.Color("green")
            num = str(self.number)
            numtext = font.render(num, True, self.color)
            screen.blit(numtext, (self.x + 20, self.y - 10, size, size))





while True:
    screen.fill(pygame.Color("black"))
    pos = pygame.mouse.get_pos()

    solvearea = pygame.draw.rect(screen, pygame.Color("green"), (0, 0, sw, sh * 0.2), width=1)
    answerarea = pygame.draw.rect(screen, pygame.Color('black'), (sw * 0.6, sh * 0.1, sw * 0.3, (sh * 0.1) - 1))
    numbers = []

    # draw operators
    w, h = sw * 0.6, sh * 0.2
    for i in range(len(operators)):
        if operators[i] == ".":
            operatorlist.append(NumBox(w - 200, (sh * 0.4) + (size * 2), pygame.Color("green"), operators[i]))
        elif i % 2 == 0:
            w = sw * 0.6
            operatorlist.append(NumBox(w, h, pygame.Color("green"), operators[i]))

        else:
            w = w + 100
            operatorlist.append(NumBox(w, h, pygame.Color("green"), operators[i]))
            h += 100



    for i in range(10): # Draw number boxes
        if i > 6:
            numbers.append(NumBox((i -7) * size, sh * 0.2, numcolor, i))

        elif i > 3:
            numbers.append(NumBox((i -4) * size, (sh * 0.2) + size, numcolor, i))
        elif i == 0:
            numbers.append(NumBox(0, (sh * 0.4) + (size * 2), numcolor, i, l= sh*0.4))

        else:
            numbers.append(NumBox((i -1) * size, (sh * 0.2) + (size * 2), numcolor, i))

    for n in numbers:
        n.collidecheck(pos)

    for op in operatorlist:
        op.collidecheck(pos)

    # controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                operation = ""
            elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                print(operation)
                #operation = str(eval(operation))
                result = str(eval(operation))
            elif event.key == pygame.K_BACKSPACE:
                operation = operation[:-1]
            elif event.key == pygame.K_c:
                operation = ""
                result = ""
            elif event.unicode in [str(x) for x in range(10)] or event.unicode in operators:
                operation += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            for num in numbers:
                if num.box.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                    operation += str(num.number)

    operationtxt = opfont.render(operation, True, pygame.Color("green"))
    operationrect = operationtxt.get_rect()

    answertxt = opfont.render(result, True, pygame.Color("green"))

    screen.blit(answertxt, answerarea)
    screen.blit(operationtxt, operationrect)

    pygame.display.update()