from cmath import log
import gi
import logging

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib, Pango

from ks_includes.KlippyGcodes import KlippyGcodes
from ks_includes.screen_panel import ScreenPanel



def create_panel(*args):
    return VacuumPanel(*args)


class VacuumPanel(ScreenPanel):
    def initialize(self, panel_name):
        self.config = None
        _ = self.lang.gettext
        grid = Gtk.Grid()

        self.labels['vacumon'] = self._gtk.ButtonImage('vac-on',_('Vacuum ON'), 'color1')
        self.labels['vacumon'].connect("clicked", self.vac_on)
        self.labels['vacumoff'] = self._gtk.ButtonImage('vac-off',_('Vacuum OFF'), 'color3')
        self.labels['vacumoff'].connect("clicked", self.vac_off)
        self.labels['vacuminfo'] = self._gtk.ButtonImage('vac-off',_('Vacuum INFO'), 'color3')
        self.labels['vacuminfo'].connect("clicked", self.vac_info)
    

        grid.attach(self.labels['vacumoff'], 2, 2, 1, 1)
        grid.attach(self.labels['vacumon'], 1, 2, 1, 1)
        grid.attach(self.labels['vacuminfo'], 0, 2, 1, 1)
        self.content.add(grid)
    def vac_info(self,widget):
        self._screen._ws.klippy.gcode_script("z_info")
        
        
    def vac_on(self, widget):
        self._screen._ws.klippy.gcode_script("vac_on")
    def vac_off(self, widget):
        self._screen._ws.klippy.gcode_script("vac_off")
      