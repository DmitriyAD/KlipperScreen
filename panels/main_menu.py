# from email.mime import image
# import gi
# import logging

# gi.require_version("Gtk", "3.0")
# from gi.repository import Gtk, GLib, Pango
# from panels.menu import MenuPanel

# from ks_includes.widgets.graph import HeaterGraph
# from ks_includes.widgets.keypad import Keypad


# def create_panel(*args):
#     return MainPanel(*args)


# class MainPanel(MenuPanel):
#     def __init__(self, screen, title, back=False):
#         super().__init__(screen, title, False)
#         self.items = None
#         self.grid = self._gtk.HomogeneousGrid()
#         self.grid.set_hexpand(True)
#         self.grid.set_vexpand(True)
#         self.devices = {}
#         self.active_heater = None
#         self.h = 1
#     def initialize(self, panel_name, items, extrudercount):
#         logging.info("### Making MainMenu")

#         self.items = items
#         self.create_menu_items()
#         stats = self._printer.get_printer_status_data()["printer"]
#         grid = self._gtk.HomogeneousGrid()
#         if stats["temperature_devices"]["count"] > 0 or stats["extruders"]["count"] > 0:
#             self._gtk.reset_temp_color()
#             # grid.attach(self.create_left_panel(), 0, 0, 1, 1)
#         if self._screen.vertical_mode:
#             self.labels['menu'] = self.arrangeMenuItems(items, 3, True)
#             grid.attach(self.labels['menu'], 0, 1, 1, 1)
#         else:
#             self.labels['menu'] = self.arrangeMenuItems(items, 2, True)
#             grid.attach(self.labels['menu'], 1, 0, 1, 1)
#         self.grid = grid
#         self.content.add(self.grid)
#         self.layout.show_all()


#         eq_grid = Gtk.Grid()
#         eq_grid.set_hexpand(True)
#         eq_grid.set_vexpand(True)
        
#         self.heaters = []

#         i = 0
#         for x in self._printer.get_tools():
#             self.labels[x] = self._gtk.ButtonImage("extruder-"+str(i), self._gtk.formatTemperatureString(0, 0))
#             self.labels[x].connect("clicked", self.menu_item_clicked, "temperature", {
#             "name":  _('Temperature'),
#             "panel": "temperature"
            
#             })
#             self.heaters.append(x)
#             i += 1

#         add_heaters = self._printer.get_heaters()
#         for h in add_heaters:
#             if h == "heater_bed":
#                 self.labels[h] = self._gtk.ButtonImage("bed", self._gtk.formatTemperatureString(0, 0))
#                 self.labels[h].connect("clicked", self.menu_item_clicked, "temperature", {
#                 "name":  _('Temperature'),
#                 "panel": "temperature"
            
#                 })
#             else:
#                 name = " ".join(h.split(" ")[1:])
#                 self.labels[h] = self._gtk.ButtonImage("heat-up", name)
#             self.heaters.append(h)

#         i = 0
#         cols = 3 if len(self.heaters) > 4 else (1 if len(self.heaters) <= 2 else 2)
#         for h in self.heaters:
#             eq_grid.attach(self.labels[h], i % cols, int(i/cols), 1, 1)
#             i += 1

#         self.items = items
#         self.create_menu_items()

#         self.grid = Gtk.Grid()
#         self.grid.set_row_homogeneous(True)
#         self.grid.set_column_homogeneous(True)

#         grid.attach(eq_grid, 0, 0, 1, 1)
#         grid.attach(self.arrangeMenuItems(items, 2, True), 1, 0, 1, 1)

#         self.grid = grid

#         self.target_temps = {
#             "heater_bed": 0,
#             "extruder": 0
#         }

#         self.content.add(self.grid)
#         self.layout.show_all()

#     def activate(self):
#         return

#     def process_update(self, action, data):
#         if action != "notify_status_update":
#             return

#         for x in self._printer.get_tools():
#             self.update_temp(
#                 x,
#                 self._printer.get_dev_stat(x, "temperature"),
#                 self._printer.get_dev_stat(x, "target"),
#                 self._printer.get_dev_stat(x, "power"),
#             )
#         for h in self._printer.get_heaters():
#             self.update_temp(
#                 h,
#                 self._printer.get_dev_stat(h, "temperature"),
#                 self._printer.get_dev_stat(h, "target"),
#                 self._printer.get_dev_stat(x, "power"),
#             )
#         return




import gi
import logging

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, Pango
from panels.menu import MenuPanel

from ks_includes.widgets.graph import HeaterGraph
from ks_includes.widgets.keypad import Keypad


def create_panel(*args):
    return MainPanel(*args)


class MainPanel(MenuPanel):
    def __init__(self, screen, title, back=False):
        super().__init__(screen, title, False)
        self.items = None
        self.grid = self._gtk.HomogeneousGrid()
        self.grid.set_hexpand(True)
        self.grid.set_vexpand(True)
        self.devices = {}
        # self.graph_update = None
        self.active_heater = None
        self.h = 1

    def initialize(self, panel_name, items, extrudercount):
        logging.info("### Making MainMenu")

        self.items = items
        self.create_menu_items()
        stats = self._printer.get_printer_status_data()["printer"]
        grid = self._gtk.HomogeneousGrid()
        if stats["temperature_devices"]["count"] > 0 or stats["extruders"]["count"] > 0:
            self._gtk.reset_temp_color()
            grid.attach(self.create_left_panel(), 0, 0, 1, 1)
        else:
            self.graph_update = False
        if self._screen.vertical_mode:
            self.labels['menu'] = self.arrangeMenuItems(items, 3, True)
            grid.attach(self.labels['menu'], 0, 1, 1, 1)
        else:
            self.labels['menu'] = self.arrangeMenuItems(items, 2, True)
            grid.attach(self.labels['menu'], 1, 0, 1, 1)
        self.grid = grid
        self.content.add(self.grid)
        self.layout.show_all()

    # def update_graph_visibility(self):
    #     count = 0
    #     for device in self.devices:
    #         visible = self._config.get_config().getboolean(f"graph {self._screen.connected_printer}",
    #                                                        device, fallback=True)
    #         self.devices[device]['visible'] = visible
    #         self.labels['da'].set_showing(device, visible)
    #         if visible:
    #             count += 1
    #             self.devices[device]['name'].get_style_context().add_class(self.devices[device]['class'])
    #             self.devices[device]['name'].get_style_context().remove_class("graph_label_hidden")
    #         else:
    #             self.devices[device]['name'].get_style_context().add_class("graph_label_hidden")
    #             self.devices[device]['name'].get_style_context().remove_class(self.devices[device]['class'])
    #     if count > 0:
    #         self.left_panel.add(self.labels['da'])
    #         self.labels['da'].queue_draw()
    #         self.labels['da'].show()
    #     else:
    #         self.left_panel.remove(self.labels['da'])

    def activate(self):
        return
        # # For this case False != None
        # if self.graph_update is None:
        #     # This has a high impact on load
        #     self.graph_update = GLib.timeout_add_seconds(5, self.update_graph)
        # self.update_graph_visibility()

    def deactivate(self):
        # if self.graph_update:
        #     GLib.source_remove(self.graph_update)
        #     self.graph_update = None
        if self.active_heater is not None:
            self.hide_numpad()

    def add_device(self, device):

        logging.info(f"Adding device: {device}")

        temperature = self._printer.get_dev_stat(device, "temperature")
        if temperature is None:
            return False

        devname = device.split()[1] if len(device.split()) > 1 else device
        # Support for hiding devices by name
        if devname.startswith("_"):
            return False

        if device.startswith("extruder"):
            i = sum(d.startswith('extruder') for d in self.devices)
            image = f"extruder-{i}" if self._printer.extrudercount > 1 else "extruder"
            # class_name = f"graph_label_{device}"
            # dev_type = "extruder"
        elif device == "heater_bed":
            image = "bed"
            devname = " Heater Bed"
            # class_name = "graph_label_heater_bed"
            # dev_type = "bed"
        elif device.startswith("heater_generic"):
            self.h = sum("heater_generic" in d for d in self.devices)
            image = "heater"
            # class_name = f"graph_label_sensor_{self.h}"
            # dev_type = "sensor"
        elif device.startswith("temperature_fan"):
            f = 1 + sum("temperature_fan" in d for d in self.devices)
            image = "fan"
            # class_name = f"graph_label_fan_{f}"
            # dev_type = "fan"
        elif self._config.get_main_config().getboolean("only_heaters", False):
            return False
        else:
            self.h += sum("sensor" in d for d in self.devices)
            image = "heat-up"
            # class_name = f"graph_label_sensor_{self.h}"
            # dev_type = "sensor"

        # rgb = self._gtk.get_temp_color(dev_type)

        can_target = self._printer.get_temp_store_device_has_target(device)
        # self.labels['da'].add_object(device, "temperatures", rgb, False, True)
        # if can_target:
        #     self.labels['da'].add_object(device, "targets", rgb, True, False)

        name = self._gtk.ButtonImage(image, None, None, 1.5, Gtk.PositionType.LEFT, 1)
        if can_target:
            name.connect("clicked", self.show_numpad, device)



        # name.connect("clicked", self.toggle_visibility, device)
        name.set_alignment(.5, .5)
        # visible = self._config.get_config().getboolean(f"graph {self._screen.connected_printer}", device, fallback=True)
        # if visible:
        #     name.get_style_context().add_class(class_name)
        # else:
        #     name.get_style_context().add_class("graph_label_hidden")
        # self.labels['da'].set_showing(device, visible)

        temp = self._gtk.Label("")
        # if can_target:
        #     temp.connect("clicked", self.show_numpad, device)
        
         

        self.devices[device] = {
            # "class": class_name,
            "name": name,
            "temp": temp,
            "can_target": can_target,
            # "visible": visible
        }

        devices = sorted(self.devices)
        pos = devices.index(device) + 1

        self.labels['devices'].insert_row(pos)
        self.labels['devices'].attach(name, temp, pos, 1, 1)
        # self.labels['devices'].attach(temp, 1, pos, 2, 1)
        self.labels['devices'].show_all()
        return True

    # def toggle_visibility(self, widget, device):
    #     self.devices[device]['visible'] ^= True
    #     logging.info(f"Graph show {self.devices[device]['visible']}: {device}")

    #     section = f"graph {self._screen.connected_printer}"
    #     if section not in self._config.get_config().sections():
    #         self._config.get_config().add_section(section)
    #     self._config.set(section, f"{device}", f"{self.devices[device]['visible']}")
    #     self._config.save_user_config_options()

    #     self.update_graph_visibility()

    def change_target_temp(self, temp):

        max_temp = int(float(self._printer.get_config_section(self.active_heater)['max_temp']))
        if temp > max_temp:
            self._screen.show_popup_message(_("Can't set above the maximum:") + f' {max_temp}')
            return
        temp = max(temp, 0)
        name = self.active_heater.split()[1] if len(self.active_heater.split()) > 1 else self.active_heater

        if self.active_heater.startswith('extruder'):
            self._screen._ws.klippy.set_tool_temp(self._printer.get_tool_number(self.active_heater), temp)
        elif self.active_heater == "heater_bed":
            self._screen._ws.klippy.set_bed_temp(temp)
        elif self.active_heater.startswith('heater_generic '):
            self._screen._ws.klippy.set_heater_temp(name, temp)
        elif self.active_heater.startswith('temperature_fan '):
            self._screen._ws.klippy.set_temp_fan_temp(name, temp)
        else:
            logging.info(f"Unknown heater: {self.active_heater}")
            self._screen.show_popup_message(_("Unknown Heater") + " " + self.active_heater)
        self._printer.set_dev_stat(self.active_heater, "target", temp)

    def create_left_panel(self):

        self.labels['devices'] = Gtk.Grid()
        self.labels['devices'].get_style_context().add_class('heater-grid')
        self.labels['devices'].set_vexpand(False)

        name = Gtk.Label("")
        self.labels['devices'].attach(name, 0, 0, 1, 1)
        
        # self.labels['da'] = HeaterGraph(self._printer, self._gtk.get_font_size())
        # self.labels['da'].set_vexpand(True)

        scroll = self._gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scroll.add(self.labels['devices'])

        self.left_panel = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.left_panel.add(scroll)

        for d in self._printer.get_temp_store_devices():
            self.add_device(d)

        return self.left_panel

    def hide_numpad(self, widget=None):
        self.devices[self.active_heater]['name'].get_style_context().remove_class("button_active")
        self.active_heater = None

        if self._screen.vertical_mode:
            self.grid.remove_row(1)
            self.grid.attach(self.labels['menu'], 0, 1, 1, 1)
        else:
            self.grid.remove_column(1)
            self.grid.attach(self.labels['menu'], 1, 0, 1, 1)
        self.grid.show_all()

    def process_update(self, action, data):
        if action != "notify_status_update":
            return

        for x in self._printer.get_tools():
            self.update_temp(
                x,
                self._printer.get_dev_stat(x, "temperature"),
                self._printer.get_dev_stat(x, "target"),
                self._printer.get_dev_stat(x, "power"),
            )
        for h in self._printer.get_heaters():
            self.update_temp(
                h,
                self._printer.get_dev_stat(h, "temperature"),
                self._printer.get_dev_stat(h, "target"),
                self._printer.get_dev_stat(x, "power"),
            )
        return

    def show_numpad(self, widget, device):

        if self.active_heater is not None:
            self.devices[self.active_heater]['name'].get_style_context().remove_class("button_active")
        self.active_heater = device
        self.devices[self.active_heater]['name'].get_style_context().add_class("button_active")

        if "keypad" not in self.labels:
            self.labels["keypad"] = Keypad(self._screen, self.change_target_temp, self.hide_numpad)
        self.labels["keypad"].clear()

        if self._screen.vertical_mode:
            self.grid.remove_row(1)
            self.grid.attach(self.labels["keypad"], 0, 1, 1, 1)
        else:
            self.grid.remove_column(1)
            self.grid.attach(self.labels["keypad"], 1, 0, 1, 1)
        self.grid.show_all()

    # def update_graph(self):
    #     self.labels['da'].queue_draw()
    #     return True