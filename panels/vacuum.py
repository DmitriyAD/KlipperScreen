import gi
import logging

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib, Pango

from ks_includes.KlippyGcodes import KlippyGcodes
from ks_includes.screen_panel import ScreenPanel
from panels.base_panel import BasePanel



def create_panel(*args):
    return VacuumPanel(*args)


class VacuumPanel(ScreenPanel):

    def __init__(self, screen, title, back=True, action_bar=True, printer_name=True):
        super().__init__(screen, title, back, action_bar, printer_name)
        self.vaccheck = 0
    

    def initialize(self, panel_name):
        _ = self.lang.gettext
        
        grid = Gtk.Grid()

        self.labels['vacumon'] = self._gtk.ButtonImage('fan',_('Vacuum ON'), 'color1')
        self.labels['vacumon'].connect("clicked", self.vac_on)
        self.labels['vacumoff'] = self._gtk.ButtonImage('fan',_('Vacuum OFF'), 'color3')
        self.labels['vacumoff'].connect("clicked", self.vac_off)
    

        grid.attach(self.labels['vacumoff'], 2, 2, 1, 1)
        grid.attach(self.labels['vacumon'], 1, 2, 1, 1)
       
        self.content.add(grid)

    def vac_on(self, widget):
        self._screen._ws.klippy.gcode_script("vac_on")
        BasePanel.update_imgVacuumON()
        
    def vac_off(self, widget):
        self._screen._ws.klippy.gcode_script("vac_off") 
        BasePanel.update_imgVacuumOFF()

           
        
    def chek_n(self):
        if self.vaccheck == 1:
            return self.vaccheck
        elif self.vaccheck == 2:   
            return self.vaccheck
           
        