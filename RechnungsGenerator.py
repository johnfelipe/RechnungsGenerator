#!/usr/bin/env python
# vim: set fileencoding=latin-1 :

import sys
import random
import traceback
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

"""
input:
	rechenart: +,-,*,/
	anzahl elemente (1 unbekannte)
	mit übertrag?
"""


class RechnungsGenerator(object):
    spalten = 3
    zeilen  = 19
    rand    = 50 ;# [points]

    def __init__(self):
        print("Willkommen zum RechenaufgabenGenerator")
        self.nGesamt   = 76
        self.nElemente = 2
        self.maxVal    = 100
        #self.nGesamt   = int(input("Wie viele Rechnungen willst Du? "))
        #self.nElemente = int(input("Wie viele Elemente soll eine Rechnung enthalten? "))
        #self.maxVal = int(input("Was soll der größte Zahlenwert der Aufgaben sein? "))
        if self.nElemente > 2:
            self.spalten = 3
        self.macheAlleRechnungen()


    def macheRechnung(self):
            c = [random.randint(0, self.maxVal)]
            ergebnis = random.randint(0, self.maxVal)
            for i in range(self.nElemente - 2):
                sumC = sum(c) - ergebnis
                c.append(random.randint(-self.maxVal + sumC, self.maxVal - sumC))
            c.append(ergebnis - sum(c))
            c.append(ergebnis)
            return c

    def macheAlleRechnungen(self):
        self.items = []
        while(len(self.items) < self.nGesamt):
            a = self.macheRechnung()
            if a not in self.items:
                self.items.append(a)

    def formatiereRechnung(self, i):
        s = ["%d" % i[0]]
        for e in i[1:-1]:
            s.append(e>=0 and '+' or '-')
            s.append(str(abs(e)))
        s.append("=")
        s.append("%d" % i[-1])
        if random.random() > 0.4: 
            # 60% in der form "x + y = __"
            s[-1] = "__"
        else:
            # 40%
            # x + __ = z
            # x __ y = z
            # __ + y = z
            idx = random.randint(0,len(s)-3)
            s[idx] = "__"
        return " ".join(s)

    def fillPDF(self, c):
        i = 0
        for _x in range(self.spalten):
            for _y in range(self.zeilen):
                try:
                    s = self.formatiereRechnung(self.items.pop())
                except Exception, e:
                    print "Exception", e
                    traceback.print_exc(file=sys.stdout)
                    break
                slen = c.stringWidth(s)
                x = _x * (A4[0]-self.rand) / self.spalten + self.rand
                y = _y * (A4[1]-self.rand) / self.zeilen  + self.rand
                c.drawString(x, y, s)
            if not len(self.items):
                break

    def producePDF(self):
        c = canvas.Canvas("Rechnungen.pdf", bottomup=0, verbosity=1)
        c.setFont(   "Helvetica",18)
        c.setAuthor( "Dieter Schoen")
        c.setCreator("RechenAufgabenGenerator")
        c.setPageSize(A4)
        self.fillPDF(c)
        c.showPage()
        c.save()

if __name__ == '__main__':
    rg = RechnungsGenerator()
    rg.producePDF()
