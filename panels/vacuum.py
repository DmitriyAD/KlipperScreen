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

        self.labels['vacumon'] = self._gtk.ButtonImage('fan',_('Vacuum ON'), 'color1')
        self.labels['vacumon'].connect("clicked", self.vac_on)
        self.labels['vacumoff'] = self._gtk.ButtonImage('fan',_('Vacuum OFF'), 'color3')
        self.labels['vacumoff'].connect("clicked", self.vac_off)
        self.labels['test'] = self._gtk.ButtonImage('refresh', _('Vacuum OFF'), 'color2')
        self.labels['test'].connect("clicked", self.menu_item_clicked, "network",{
                "name": _('Network'),
                "panel": "network"
                })

        grid.attach(self.labels['vacumoff'], 2, 2, 1, 1)
        grid.attach(self.labels['vacumon'], 1, 2, 1, 1)
        grid.attach(self.labels['test'], 3, 2, 1, 1)

        self.content.add(grid)
def vac_on(self):
    self._screen._ws.klippy.gcode_script("VAC_ON")
       

def vac_off(self):
    self._screen._ws.klippy.gcode_script("VAC_OFF")     

        