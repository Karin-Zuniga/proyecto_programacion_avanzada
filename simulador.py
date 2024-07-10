import sys
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk,Gio

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #header
        header = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=header)
        self.set_title("Simulador epidemiologico")

        #Box ppal
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20,
            margin_top=20, margin_bottom=20,
            margin_start=20, margin_end=20)
        

        #menu  
        menu = Gio.Menu.new()
        self.popover = Gtk.PopoverMenu()
        self.popover.set_menu_model(menu)
  
        self.menu_popover = Gtk.MenuButton()   
        self.menu_popover.set_popover(self.popover)
        self.menu_popover.set_icon_name("open-menu-symbolic")

        header.pack_end(self.menu_popover)

        #menu about
        about_menu = Gio.SimpleAction.new("about", None)
        about_menu.connect("activate", self.show_about_dialog)
        self.add_action(about_menu)
        menu.append("Acerca de", "win.about")



    def show_about_dialog(self, action, param):
        self.about = Gtk.AboutDialog()
        self.about.set_authors(["Karin Zuñiga"])
        self.about.set_copyright("Copyright 2024 Karin Zuñiga Muñoz")
        self.about.set_license_type(Gtk.License.GPL_3_0)
        self.about.set_visible(True)


class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def do_activate(self):
        print("Aplicación activada")
        active_window = self.props.active_window
        if active_window:
            active_window.present()
        else:
            self.win = MainWindow(application=self)
            self.win.present()

    def do_startup(self):
        print("Aplicación iniciada")
        Gtk.Application.do_startup(self)

    def do_shutdown(self):
        print("Aplicación cerrada")
        Gtk.Application.do_shutdown(self)


app = MyApp()
app.run(sys.argv)

