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
        grid = self._gtk.HomogeneousGrid()
        grid.set_row_homogeneous(True)

        vacumon = self._gtk.Image('fan',_('Vacuum ON'), 'color1')
        vacumon.connect("clicked", self.vac_on)
        vacumoff = self._gtk.Button('refresh', _('Vacuum OFF'), 'color2')
        vacumoff.connect("clicked", self.menu_item_clicked, "network",{
                "name": _('Network'),
                "panel": "network"
                })

        grid.attach(vacumoff, 2, 2, 1, 1)
        grid.attach(vacumon, 1, 2, 1, 1)

        self.content.add(grid)


    def vac_on(self):
        self._screen._ws.klippy.gcode_script("vac_on")
       

    def vac_off(self):
         self._screen._ws.klippy.gcode_script("vac_off")  

        