import gi
import logging
import configparser
import gettext
import os
import json
import re
import copy
import pathlib

from io import StringIO

from os import path

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib, Pango

from ks_includes.KlippyGcodes import KlippyGcodes
from ks_includes.screen_panel import ScreenPanel



def create_panel(*args):
    return VacuumPanel(*args)


class VacuumPanel(ScreenPanel):
    def initialize(self, panel_name):
        _ = self.lang.gettext
        self.vaccheck = 0
        grid = Gtk.Grid()

        self.labels['vacumon'] = self._gtk.ButtonImage('fan',_('Vacuum ON'), 'color1')
        self.labels['vacumon'].connect("clicked", self.vac_on)
        self.labels['vacumoff'] = self._gtk.ButtonImage('fan',_('Vacuum OFF'), 'color3')
        self.labels['vacumoff'].connect("clicked", self.vac_off)
    

        grid.attach(self.labels['vacumoff'], 2, 2, 1, 1)
        grid.attach(self.labels['vacumon'], 1, 2, 1, 1)
       
        self.content.add(grid)

    def vac_on(self, widget):
        self.vaccheck = 1
        self._screen._ws.klippy.gcode_script("vac_on")
        logging.info("self vac_on return %d" % self.vaccheck)
        return self.vaccheck

        
    def vac_off(self, widget):
        self.vaccheck = 2
        self._screen._ws.klippy.gcode_script("vac_off") 
        logging.info("self vac_off return %d" % self.vaccheck)
        return self.vaccheck

           
        
    def chek_n(self):
        if self.vaccheck == 1:
            return True
        elif self.vaccheck == 2:   
            return False  
           
        