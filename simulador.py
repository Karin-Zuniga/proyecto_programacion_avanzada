import sys
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk,Gio
import pandas as pd
class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_default_size(800, 600)

        # header
        header = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=header)
        self.set_title("Simulador epidemiologico")

        #Box ppal
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_child(self.main_box)

        #botones adelantar y retroceder
        self.current_index = 2
        button_box = Gtk.Box(spacing=6)
        self.main_box.append(button_box)


        prev_button = Gtk.Button(label="Anterior")
        prev_button.connect("clicked", self.on_prev_clicked)
        button_box.append(prev_button)

        next_button = Gtk.Button(label="Siguiente")
        next_button.connect("clicked", self.on_next_clicked)
        button_box.append(next_button)

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
        

        #scroll
        
        self.liststore = None
        self.treeview = Gtk.TreeView()
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_child(self.treeview)
        self.main_box.append(scrolled_window)
        scrolled_window.set_vexpand(True)

        file = f"archivo_{self.current_index}.csv"
        self.mostrar_csv(file)

    def show_about_dialog(self, action, param):
        self.about = Gtk.AboutDialog()
        self.about.set_authors(["Karin Zuñiga"])
        self.about.set_copyright("Copyright 2024 Karin Zuñiga Muñoz")
        self.about.set_license_type(Gtk.License.GPL_3_0)
        self.about.set_visible(True)

    def mostrar_csv(self, file):
        
   
        df = pd.read_csv(file)

        if self.liststore:
            self.treeview.set_model(None)
            self.remove_all_columns()
        column_types = (int,int, str,str,str,str,int,int)
        self.liststore = Gtk.ListStore(*column_types)

        for i, column_title in enumerate(df.columns):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)



        for row in df.itertuples(index=False):
            self.liststore.append(list(row))
        
        self.treeview.set_model(self.liststore)

    
        self.main_box.append(self.treeview)
        
        
    
    def on_prev_clicked(self, button):
        if self.current_index > 0:
            self.current_index -= 1
            self.mostrar_csv(f"archivo_{self.current_index}.csv")

    def on_next_clicked(self, button):
        if self.current_index > 0:
            self.current_index += 1
            self.mostrar_csv(f"archivo_{self.current_index}.csv")


    def remove_all_columns(self):
       
        columns = self.treeview.get_columns()
        for column in columns:
            self.treeview.remove_column(column)





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




