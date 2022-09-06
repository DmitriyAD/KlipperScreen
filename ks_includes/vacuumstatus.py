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

class VacuumStatus:
    

           
        
    def chek_n(self):
        if self.vaccheck == 1:
            return True
        elif self.vaccheck == 2:   
            return False  
           
        