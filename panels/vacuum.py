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
        _ = self.lang.gettext
        self.control_grid = self._gtk.HomogeneousGrid()
        self.control_grid.set_row_homogeneous(True)

        self.control['vacumon'] = self._gtk.ButtonImage('fan',_('Vacuum ON'), 'color1')
        self.control['vacumon'].connect("clicked", self.vac_on)
        self.control['vacumoff'] = self._gtk.ButtonImage('refresh', _('Vacuum OFF'), 'color2')
        self.control['vacumoff'].connect("clicked", self.vac_off)


        self.control_grid.attach(self.control['vacuumon'], 1, 0, 1, 1)
        self.control_grid.attach(self.control['vacuumoff'], 2, 0, 1, 1)
       
        self.content.add(self.control_grid)


    def vac_on(self):
        self._screen._ws.klippy.gcode_script("vac_on")
       

    def vac_off(self):
         self._screen._ws.klippy.gcode_script("vac_off")  

        