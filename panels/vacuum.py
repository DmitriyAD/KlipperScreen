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

        _ = self.lang.gettext
        grid = Gtk.Grid()

        self.labels['vacumon'] = self._gtk.ButtonImage('vac-on',_('Vacuum ON'), 'color1')
        self.labels['vacumon'].connect("clicked", self.vac_on)
        self.labels['vacumoff'] = self._gtk.ButtonImage('vac-off',_('Vacuum OFF'), 'color3')
        self.labels['vacumoff'].connect("clicked", self.vac_off)
    

        grid.attach(self.labels['vacumoff'], 2, 2, 1, 1)
        grid.attach(self.labels['vacumon'], 1, 2, 1, 1)
        self.content.add(grid)

    def vac_on(self, widget):
        self._screen._ws.klippy.gcode_script("vac_on")
    def vac_off(self, widget):
        value = self._screen._ws.klippy.gcode_script(" SEARCH_VARS s='output_pin _vacuum'")
        if value == 1:
            logging.info("value1 =: %s" % value)
        if value == 0: 
            logging.info("value0 =: %s" % value)

        # vac= self._screen.printer.get_config_section("output_pin _vacuum")
        # if "value" in vac:
        #     a = int(vac['value'])
        #     logging.info("a =: %s" % a)
        # return a
        # self._screen._ws.klippy.gcode_script("vac_off") 
        # ln = {}
        # a = 45
        # ln = self._printer.get_vac_state()
        # logging.info("123: %s" % ln)
        # if "value" in ln:
        #     a = int(ln['value'])
        #     logging.info("a =: %s" % a)
        # return ln