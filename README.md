RechnungsGenerator
==================

Simple python script which generates 1st grade math exercises for my son and exports them as PDF

It uses reportlab for the creation of PDF files.
In order to build reportlab on Mac OS X, I followed this recipe:

    ARCHFLAGS='-arch i386' LDFLAGS="-L. -L/usr/lib/" python setup.py install

from http://whitetailsoftware.com/2011/05/installing-reportlab-on-mac-os-x-10-5/.
