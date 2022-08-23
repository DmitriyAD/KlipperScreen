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
        vacuum_status =0
        grid = self._gtk.HomogeneousGrid()
        grid.set_row_homogeneous(True)

        vacumon = self._gtk.ButtonImage('vac-on', None, None, 1)
        vacumon.connect("clicked", self.vac_on)
        vacumon.set_vexpand(False)
        vacumoff = self._gtk.ButtonImage('vac-off', None, None, 1)
        vacumoff.connect("clicked", self.vac_off)
        vacumoff.set_vexpand(False)


        grid.attach(vacumoff, 3, 2, 1, 1)
        grid.attach(vacumon, 1, 2, 1, 1)
    
        self.content.add(grid)


    def vac_on(self):
       self._ws.klippy.gcode_script("vac_on")
       

    def vac_off(self):
        self._ws.klippy.gcode_script("vac_off")  

        