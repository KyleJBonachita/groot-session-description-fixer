from importlib.metadata import distribution
import os
import json
import re
import shutil
from pathlib import Path
from tkinter import *
from tkinter import ttk, filedialog, messagebox, scrolledtext
from threading import Thread
import tkinter.font as tkFont

class SessionFixer:
    def __init__(self, root):
        self.root = root
        self.root.title("GR00T Session Description Fixer")
        self.root.geometry("1000x800")
        self.task_descriptions = {
            "braid_unbraid": {
                "LI_1": "use both hands to braid the [yarn/ribbon]",
                "LI_2": "use both hands to unbraid the [yarn/ribbon]"
            },
            "charge_uncharge_airpods": {
                "LI_1": "use both hands to plug in the AirPods case",
                "LI_2": "use both hands to unplug the AirPods case"
            },
            "deal_gather_cards": {
                "LI_1": "use both hands to deal the cards",
                "LI_2": "use both hands to gather the cards"
            },
            "fry_bread": {
                "LI_1": "fry the bread on the stove until cooked",
                "LI_2": "remove the fried bread from the stove and place it on a plate"
            },
            "assemble_disassemble_furniture_bench_chair": {
                "LI_1": "use both hands to assemble the chair on the bench",
                "LI_2": "use both hands to disassemble the chair from the bench"
            },
            "assemble_disassemble_furniture_bench_drawer": {
                "LI_1": "use both hands to assemble the drawer unit on the bench",
                "LI_2": "use both hands to disassemble the drawer unit from the bench"
            },
            "assemble_disassemble_furniture_bench_square_table": {
                "LI_1": "use both hands to assemble the square table on the bench",
                "LI_2": "use both hands to disassemble the square table from the bench"
            },
            "fold_unfold_paper_basic": {
                "LI_1": "use both hands to fold the sheet of paper",
                "LI_2": "use both hands to unfold the folded paper"
            },
            "insert_remove_furniture_bench_cabinet": {
                "LI_1": "use both hands to insert the cabinet into the furniture bench",
                "LI_2": "use both hands to remove the cabinet from the furniture bench"
            },
            "gather_roll_dice": {
                "LI_1": "use right hand to gather the dice",
                "LI_2": "use right hand to roll the gathered dice"
            },
            "insert_remove_airpods": {
                "LI_1": "use both hands to insert the AirPods into their case",
                "LI_2": "use both hands to remove the AirPods from their case"
            },
            "insert_remove_drawer": {
                "LI_1": "use both hands to insert the drawer into the cabinet",
                "LI_2": "use both hands to remove the drawer from the cabinet"
            },
            "insert_remove_shirt_in_tube": {
                "LI_1": "use both hands to insert the shirt into the tube",
                "LI_2": "use both hands to remove the shirt from the tube"
            },
            "insert_remove_usb": {
                "LI_1": "use both hands to insert the USB into the port",
                "LI_2": "use both hands to remove the USB from the port"
            },
            "load_dispense_ice": {
                "LI_1": "use both hands to load ice into the container",
                "LI_2": "use both hands to dispense ice from the container"
            },
            "open_close_insert_remove_tupperware": {
                "LI_1": "use both hands to open the tupperware and insert items, then close it",
                "LI_2": "use both hands to open the tupperware"
            },
            "pick_up_and_put_down_case_or_bag": {
                "LI_1": "use both hands to pick up the [case/bag]",
                "LI_2": "use both hands to put down the [case/bag]"
            },
            "put_away_set_up_board_game": {
                "LI_1": "use both hands to set up the board game",
                "LI_2": "use both hands to put away the board game"
            },
            "screw_unscrew_fingers_fixture": {
                "LI_1": "use your fingers on both hands to screw the fixture",
                "LI_2": "use your fingers on both hands to unscrew the fixture"
            },
            "sleeve_unsleeve_cards": {
                "LI_1": "use both hands to sleeve the cards",
                "LI_2": "use both hands to unsleeve the cards"
            },
            "stack_unstack_cups": {
                "LI_1": "use both hands to stack the cups",
                "LI_2": "use both hands to unstack the cups"
            },
            "thread_unthread_bead_necklace": {
                "LI_1": "use both hands to thread the bead onto the necklace",
                "LI_2": "use both hands to unthread the bead from the necklace"
            },
            "tie_and_untie_shoelace": {
                "LI_1": "use both hands to tie the shoelace",
                "LI_2": "use both hands to untie the shoelace"
            },
            "insert_remove_tennis_ball": {
                "LI_1": "use both hands to insert the tennis ball into the container",
                "LI_2": "use both hands to remove the tennis ball from the container"
            },
            "open_close_insert_remove_case": {
                "LI_1": "use both hands to open the case and insert items, then close it",
                "LI_2": "use both hands to open the case"
            },
            "pick_place_food": {
                "LI_1": "use both hands to pick up the food",
                "LI_2": "use both hands to place the food down"
            },
            "put_in_take_out_glasses": {
                "LI_1": "use both hands to put in the glasses into the case",
                "LI_2": "use both hands to take out the glasses from the case"
            },
            "screw_unscrew_allen_fixture": {
                "LI_1": "use both hands to screw the Allen fixture",
                "LI_2": "use both hands to unscrew the Allen fixture"
            },
            "set_up_clean_up_chessboard": {
                "LI_1": "use both hands to set up the chessboard",
                "LI_2": "use both hands to clean up the chessboard"
            },
            "slot_batteries": {
                "LI_1": "use both hands to slot the batteries into the device",
                "LI_2": "use both hands to remove the batteries from the device"
            },
            "stack_unstack_bowls": {
                "LI_1": "use both hands to stack the bowls",
                "LI_2": "use both hands to unstack the bowls"
            },
            "stack_unstack_tupperware": {
                "LI_1": "use both hands to stack the tupperware containers",
                "LI_2": "use both hands to unstack the tupperware containers"
            },
            "throw_collect_objects": {
                "LI_1": "use right hand to throw objects",
                "LI_2": "use right hand to collect the thrown objects"
            },
            "vertical_pick_place": {
                "LI_1": "use right hand to pick up objects and place them vertically on the [rack/shelf]",
                "LI_2": "use right hand to remove the objects from the [rack/shelf]"
            },
            "wash_put_away_dishes": {
                "LI_1": "use both hands to wash the dishes",
                "LI_2": "use both hands to put away the washed dishes"
            },
            "add_remove_lid": {
                "LI_1": "use both hands to add the lid to the container",
                "LI_2": "use both hands to remove the lid from the container"
            },
            "arrange_topple_dominoes": {
                "LI_1": "use both hands to arrange the dominoes",
                "LI_2": "use both hands to topple the arranged dominoes"
            },
            "assemble_disassemble_legos": {
                "LI_1": "use both hands to assemble the Lego pieces",
                "LI_2": "use both hands to disassemble the Lego pieces"
            },
            "assemble_disassemble_soft_legos": {
                "LI_1": "use both hands to assemble the soft Lego pieces",
                "LI_2": "use both hands to disassemble the soft Lego pieces"
            },
            "assemble_disassemble_structures": {
                "LI_1": "use both hands to assemble the building structures",
                "LI_2": "use both hands to disassemble the building structures"
            },
            "assemble_disassemble_tiles": {
                "LI_1": "use both hands to assemble the tiles",
                "LI_2": "use both hands to disassemble the tiles"
            },
            "boil_serve_egg": {
                "LI_1": "use both hands to boil the egg",
                "LI_2": "use both hands to serve the boiled egg on a plate"
            },
            "build_unstack_lego": {
                "LI_1": "use both hands to build a Lego tower",
                "LI_2": "use both hands to unstack the Lego tower"
            },
            "charge_uncharge_device": {
                "LI_1": "use both hands to plug in the device",
                "LI_2": "use both hands to unplug the device"
            },
            "clip_unclip_papers": {
                "LI_1": "use both hands to clip the papers together",
                "LI_2": "use both hands to unclip the papers"
            },
            "crumple_flatten_paper": {
                "LI_1": "use both hands to crumple the sheet of paper",
                "LI_2": "use both hands to flatten the crumpled paper"
            },
            "fry_egg": {
                "LI_1": "use both hands to fry the egg",
                "LI_2": "use both hands to remove the fried egg from the pan"
            },
            "assemble_disassemble_furniture_bench_desk": {
                "LI_1": "use both hands to assemble the desk on the bench",
                "LI_2": "use both hands to disassemble the desk from the bench"
            },
            "assemble_disassemble_furniture_bench_lamp": {
                "LI_1": "use both hands to assemble the lamp on the bench",
                "LI_2": "use both hands to disassemble the lamp from the bench"
            },
            "assemble_disassemble_furniture_bench_stool": {
                "LI_1": "use both hands to assemble the stool on the bench",
                "LI_2": "use both hands to disassemble the stool from the bench"
            },
            "fold_stack_unstack_unfold_cloths": {
                "LI_1": "use both hands to fold the clothes, and stack the folded clothes",
                "LI_2": "use both hands to unstack the clothes, and unfold the clothes"
            },
            "fold_unfold_paper_origami": {
                "LI_1": "use both hands to fold the origami paper",
                "LI_2": "use both hands to unfold the origami paper"
            },
            "insert_remove_furniture_bench_round_table": {
                "LI_1": "use both hands to insert the round table into the furniture bench",
                "LI_2": "use both hands to remove the round table from the furniture bench"
            },
            "insert_remove_bagging": {
                "LI_1": "use both hands to insert items into the bag",
                "LI_2": "use both hands to remove items from the bag"
            },
            "insert_remove_cups_from_rack": {
                "LI_1": "use both hands to insert cups into the rack",
                "LI_2": "use both hands to remove cups from the rack"
            },
            "insert_remove_plug_socket": {
                "LI_1": "use right hand to insert the plug into the socket",
                "LI_2": "use right hand to remove the plug from the socket"
            },
            "insert_remove_utensils": {
                "LI_1": "use both hands to insert utensils into the holder",
                "LI_2": "use both hands to remove utensils from the holder"
            },
            "lock_unlock_key": {
                "LI_1": "use right hand to lock the padlock",
                "LI_2": "use right hand to unlock the padlock"
            },
            "open_close_insert_remove_box": {
                "LI_1": "use both hands to insert the cabinet into the furniture bench",
                "LI_2": "use both hands to remove the cabinet from the furniture bench"
            },
            "scoop_dump_ice": {
                "LI_1": "use right hand to scoop ice into the container",
                "LI_2": "use right hand to dump ice out of the container"
            },
            "screw_unscrew_bottle_cap": {
                "LI_1": "use right hand to screw the bottle cap onto the bottle",
                "LI_2": "use right hand to unscrew the bottle cap from the bottle"
            },
            "setup_cleanup_table": {
                "LI_1": "use both hands to set up the table",
                "LI_2": "use both hands to clean up the table"
            },
            "stock_unstock_fridge": {
                "LI_1": "use both hands to stock items in the fridge",
                "LI_2": "use both hands to unstock items from the fridge"
            },
            "stack_unstack_plates": {
                "LI_1": "use both hands to stack the plates",
                "LI_2": "use both hands to unstack the plates"
            },
            "throw_and_catch_ball": {
                "LI_1": "use both hands to throw the ball",
                "LI_2": "use both hands to catch the thrown ball"
            },
            "tie_untie_rubberband": {
                "LI_1": "use both hands to tie the rubber band around an object",
                "LI_2": "use both hands to untie the rubber band from the object"
            },
            "wrap_unwrap_food": {
                "LI_1": "use both hands to wrap the food",
                "LI_2": "use both hands to unwrap the food"
            },
            "zip_unzip_bag": {
                "LI_1": "use both hands to zip the bag",
                "LI_2": "use both hands to unzip the bag"
            },
            "zip_unzip_case": {
                "LI_1": "use both hands to zip the case",
                "LI_2": "use both hands to unzip the case"
            },
            "assemble_disassemble_jigsaw_puzzle": {
                "LI_1": "use both hands to assemble the jigsaw puzzle pieces",
                "LI_2": "use both hands to disassemble the jigsaw puzzle pieces"
            },
            "stack_unstack_tetra_board": {
                "LI_1": "use both hands to stack the tetra board pieces",
                "LI_2": "use both hands to unstack the tetra board pieces"
            },
            "stack_remove_jenga": {
                "LI_1": "use both hands to stack the Jenga blocks",
                "LI_2": "use both hands to remove the Jenga blocks"
            },
            "insert_dump_blocks": {
                "LI_1": "use both hands to insert blocks into the container",
                "LI_2": "use both hands to dump the blocks out of the container"
            },
            "rake_smooth_zen_garden": {
                "LI_1": "use both hands to rake the sand in the zen garden",
                "LI_2": "use both hands to smooth the sand in the zen garden"
            },
            "play_reset_connect_four": {
                "LI_1": "use both hands to play Connect Four",
                "LI_2": "use both hands to reset the Connect Four game"
            },
            "insert_remove_bookshelf": {
                "LI_1": "use both hands to insert items into the bookshelf",
                "LI_2": "use both hands to remove items from the bookshelf"
            },
        }
        self.session_path = ""
        self.is_processing = False
        
        self.setup_ui()
        self.create_menu()

    def create_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about, accelerator="F1")
        self.root.bind('<F1>', lambda e: self.show_about())

    def show_about(self):
        about_window = Toplevel(self.root)
        about_window.title("About GR00T Session Fixer")
        about_window.geometry("500x750")
        about_window.resizable(False, False)
        about_window.configure(bg='#2c3e50')
        about_window.transient(self.root)
        about_window.grab_set()
        header = Frame(about_window, bg='#16a085', height=80)
        header.pack(fill=X)
        header.pack_propagate(False)
        icon_font = tkFont.Font(family="Segoe UI Emoji", size=38)
        Label(header, text="🤖", font=icon_font, bg='#16a085', fg='white').pack(pady=10)
        content = Frame(about_window, bg='white', padx=30, pady=25)
        content.pack(fill=BOTH, expand=True)
        title_font = tkFont.Font(family="Arial", size=18, weight="bold")
        Label(content, text="GR00T Session Description Fixer", 
              font=title_font, bg='white', fg='#2c3e50').pack(pady=(0, 5))
        version_frame = Frame(content, bg='#3498db', relief=FLAT)
        version_frame.pack(pady=5)
        Label(version_frame, text="Version 1.0", font=("Arial", 9, "bold"), 
              bg='#3498db', fg='white', padx=12, pady=4).pack()
        separator = Frame(content, height=2, bg='#ecf0f1')
        separator.pack(fill=X, pady=15)
        desc_text = "A specialized tool for automating session data\norganization and description standardization in\nGR00T robotics data collection workflows."
        Label(content, text=desc_text, font=("Arial", 10), bg='white', 
              fg='#34495e', justify=CENTER).pack(pady=10)
        features_frame = Frame(content, bg='#ecf0f1', relief=FLAT, bd=1)
        features_frame.pack(fill=X, pady=15)
        features = [
            "✓ Automated episode segregation (LI 1 & LI 2)",
            "✓ Metadata description validation & correction",
            "✓ User-friendly GUI for easy navigation and operation.",
            "✓ Real-time logging of operations for transparency.",
            "✓ Supports a wide range of predefined task descriptions."
        ]
        for feature in features:
            Label(features_frame, text=feature, font=("Arial", 9), bg='#ecf0f1', fg='#2c3e50', anchor=W).pack(padx=15, pady=3, fill=X)
        separator = Frame(content, height=2, bg='#ecf0f1')
        separator.pack(fill=X, pady=15)
        dev_frame = Frame(content, bg='white')
        dev_frame.pack(pady=(15, 10))
        Label(dev_frame, text="Developed by:", font=("Arial", 9, "bold"), bg='white', fg='#7f8c8d').pack()
        developers = ["Kyle Josef Bonachita"]
        Label(dev_frame, text="  |  ".join(developers), font=("Arial", 11, "bold"), bg='white', fg='#16a085').pack(pady=2)
        Label(dev_frame, text="Data Collector", font=("Arial", 9), bg='white', fg='#7f8c8d').pack()
        Label(dev_frame, text="HCL Technologies Philippines", font=("Arial", 9), bg='white', fg='#7f8c8d').pack()
        Label(dev_frame, text="NVIDIA GR00T Robotics AI Project", font=("Arial", 9, "bold"), bg='white', fg='#3498db').pack(pady=2)
        btn_frame = Frame(content, bg='white')
        btn_frame.pack(pady=(10, 0))
        close_btn = Button(btn_frame, text="Close", command=about_window.destroy, bg='#16a085', fg='white', font=("Arial", 10, "bold"), relief=FLAT, padx=40, pady=10, cursor="hand2", activebackground='#138d75', activeforeground='white')
        close_btn.pack()
        def on_enter(e):
            close_btn['bg'] = '#138d75'
        def on_leave(e):
            close_btn['bg'] = '#16a085'
        close_btn.bind('<Enter>', on_enter)
        close_btn.bind('<Leave>', on_leave)
        footer = Frame(about_window, bg='#34495e', height=35)
        footer.pack(fill=X, side=BOTTOM)
        footer.pack_propagate(False)
        Label(footer, text="© 2026 | For NVIDIA GR00T Project PH Use Only", font=("Arial", 8), bg='#34495e', fg='#95a5a6').pack(pady=8)

    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(N, S, E, W))
        ttk.Label(main_frame, text="GR00T Session Description Fixer", font=("Arial", 16, "bold"), anchor="center", justify="center").grid(row=0, column=0, columnspan=3, sticky=(E, W), pady=(0, 10))
        ttk.Label(main_frame, text="Session Folder Path:", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky=W, pady=5)
        path_frame = ttk.Frame(main_frame)
        path_frame.grid(row=2, column=0, columnspan=3, sticky=(E, W), pady=5)
        self.path_var = StringVar()
        self.path_entry = ttk.Entry(path_frame, textvariable=self.path_var, width=60)
        self.path_entry.pack(side=LEFT, fill=BOTH, expand=True)   
        ttk.Button(path_frame, text="Browse", command=self.select_session_path).pack(side=LEFT, padx=5)
        
        ttk.Separator(main_frame, orient=HORIZONTAL).grid(row=3, column=0, columnspan=3, sticky=(E, W), pady=10)
        
        ttk.Label(main_frame, text="STEP 1: Segregate Folders", font=("Arial", 11, "bold")).grid(row=4, column=0, sticky=W, pady=5)
        ttk.Button(main_frame, text="▶ Create LI 1 & LI 2 Folders and Segregate Episodes", command=self.segregate_folders).grid(row=5, column=0, columnspan=2, sticky=(E, W), pady=5)
        
        ttk.Separator(main_frame, orient=HORIZONTAL).grid(row=6, column=0, columnspan=3, sticky=(E, W), pady=10)
        
        ttk.Label(main_frame, text="STEP 2: Fix Descriptions", font=("Arial", 11, "bold")).grid(row=7, column=0, sticky=W, pady=5)
        ttk.Label(main_frame, text="Task Name:", font=("Arial", 10, "bold")).grid(row=8, column=0, sticky=W, padx=20)
        self.task_var = StringVar()
        task_dropdown = ttk.Combobox(main_frame, textvariable=self.task_var, values=list(self.task_descriptions.keys()), state="readonly", width=60)
        task_dropdown.grid(row=8, column=1, sticky=W, padx=5)
        task_dropdown.bind("<<ComboboxSelected>>", self.on_task_selected)
        
        ttk.Label(main_frame, text="LI 1 Correct Description:", font=("Arial", 10, "bold")).grid(row=9, column=0, sticky=(W, N), padx=20, pady=(10, 0))
        self.li1_text = scrolledtext.ScrolledText(main_frame, height=3, width=70)
        self.li1_text.grid(row=9, column=1, columnspan=2, sticky=(E, W, N, S), padx=5, pady=5)
        ttk.Label(main_frame, text="LI 2 Correct Description:", font=("Arial", 10, "bold")).grid(row=10, column=0, sticky=(W, N), padx=20, pady=(10, 0))
        self.li2_text = scrolledtext.ScrolledText(main_frame, height=3, width=70)
        self.li2_text.grid(row=10, column=1, columnspan=2, sticky=(E, W, N, S), padx=5, pady=5)
        ttk.Button(main_frame, text="▶ Start Description Fix", command=self.start_fix_descriptions).grid(row=11, column=0, columnspan=2, sticky=(E, W), pady=10)
        
        ttk.Separator(main_frame, orient=HORIZONTAL).grid(row=12, column=0, columnspan=3, sticky=(E, W), pady=10)
        
        ttk.Label(main_frame, text="Processing Log:", font=("Arial", 10, "bold")).grid(row=13, column=0, sticky=W, pady=5)
        self.log_text = scrolledtext.ScrolledText(main_frame, height=15, width=100)
        self.log_text.grid(row=14, column=0, columnspan=3, sticky=(E, W, N, S), pady=5)
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(14, weight=1)
    
    def log(self, message):
        self.log_text.insert(END, message + "\n")
        self.log_text.see(END)
        self.root.update()
    
    def select_session_path(self):
        path = filedialog.askdirectory(title="Select Session Folder")
        if path:
            self.path_var.set(path)
            self.log(f"✅ Selected: {path}")
    
    def on_task_selected(self, event=None):
        task_name = self.task_var.get()
        if task_name in self.task_descriptions:
            li1_desc = self.task_descriptions[task_name]["LI_1"]
            li2_desc = self.task_descriptions[task_name]["LI_2"]
            
            self.li1_text.delete(1.0, END)
            self.li1_text.insert(1.0, li1_desc)
            
            self.li2_text.delete(1.0, END)
            self.li2_text.insert(1.0, li2_desc)
            
            self.log(f"📝 Task '{task_name}' selected with default descriptions")
    
    def segregate_folders(self):
        if not self.path_var.get():
            messagebox.showerror("Error", "Please select a session folder")
            return
        
        session_path = Path(self.path_var.get())
        
        if not session_path.exists():
            messagebox.showerror("Error", f"Path does not exist: {session_path}")
            return
        
        self.log("\n" + "="*60)
        self.log("🔍 Starting folder segregation...")
        self.log("="*60 + "\n")
        
        try:
            li1_parent = session_path / "LI 1"
            li2_parent = session_path / "LI 2"
            li1_parent.mkdir(exist_ok=True)
            li2_parent.mkdir(exist_ok=True)
            self.log(f"✅ Created folders: LI 1 and LI 2")
            
            session_name = session_path.name
            operator = self.get_operator_from_metadata(session_path)
            
            if not operator:
                self.log("⚠️ Warning: Could not find operator in metadata.json")
                operator = "unknown"
            
            li1_session = li1_parent / f"{session_name} - {operator}"
            li2_session = li2_parent / f"{session_name} - {operator}"
            
            li1_session.mkdir(exist_ok=True)
            li2_session.mkdir(exist_ok=True)
            self.log(f"✅ Created session subfolders with operator: {operator}")
            
            episodes = sorted([d for d in session_path.iterdir() if d.is_dir() and d.name not in ["LI 1", "LI 2", "logs"]])
            
            if not episodes:
                self.log("⚠️ No episode folders found")
                return
            
            self.log(f"📂 Found {len(episodes)} episodes\n")
            
            for episode in episodes:
                parts = episode.name.split("-")
                if len(parts) >= 2:
                    try:
                        episode_num = int(parts[-1])
                        
                        if episode_num % 2 == 1:  
                            # Odd episodes
                            dest = li1_session / episode.name
                            self.log(f"📁 Moving (odd)  {episode.name} → LI 1")
                        else:  
                            # Even episodes
                            dest = li2_session / episode.name
                            self.log(f"📁 Moving (even) {episode.name} → LI 2")
                        
                        if dest.exists():
                            shutil.rmtree(dest)
                        shutil.move(str(episode), str(dest))
                    except ValueError:
                        self.log(f"⚠️ Skipped {episode.name} (cannot parse episode number)")
            
            logs_path = session_path / "logs"
            if logs_path.exists():
                self.log(f"\n📂 Copying logs folder to both LI 1 and LI 2")

                li1_logs_dest = li1_session / "logs"
                if li1_logs_dest.exists():
                    shutil.rmtree(li1_logs_dest)
                shutil.copytree(str(logs_path), str(li1_logs_dest))
                self.log(f"✅ Copied logs to LI 1") 

                li2_logs_dest = li2_session / "logs"
                if li2_logs_dest.exists():
                    shutil.rmtree(li2_logs_dest)
                shutil.copytree(str(logs_path), str(li2_logs_dest))
                self.log(f"✅ Copied logs to LI 2")

                shutil.rmtree(logs_path)
                self.log(f"🗑️ Removed original logs folder\n")
            
            self.log("\n" + "="*60)
            self.log("✨ Folder segregation complete!")
            self.log("="*60)
            messagebox.showinfo("Success", "Folders have been segregated successfully!")
            
        except Exception as e:
            self.log(f"\n❌ Error: {str(e)}")
            messagebox.showerror("Error", str(e))
    
    def get_operator_from_metadata(self, session_path):
        for item in session_path.rglob("metadata.json"):
            try:
                with open(item, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if "config" in data and "operator" in data["config"]:
                        return data["config"]["operator"]
            except:
                pass
        return None
    
    def start_fix_descriptions(self):
        if not self.path_var.get():
            messagebox.showerror("Error", "Please select a session folder")
            return
        
        if not self.task_var.get():
            messagebox.showerror("Error", "Please select a task name")
            return
        
        li1_desc = self.li1_text.get(1.0, END).strip()
        li2_desc = self.li2_text.get(1.0, END).strip()
        
        if not li1_desc or not li2_desc:
            messagebox.showerror("Error", "Please fill in both LI 1 and LI 2 descriptions")
            return
        
        self.is_processing = True
        thread = Thread(target=self.fix_descriptions_worker, args=(li1_desc, li2_desc))
        thread.daemon = True
        thread.start()
    
    def fix_descriptions_worker(self, li1_desc, li2_desc):
        session_path = Path(self.path_var.get())
        
        self.log("\n" + "="*60)
        self.log("🔧 Starting description fix...")
        self.log("="*60 + "\n")
        
        try:
            li1_path = session_path / "LI 1"
            if li1_path.exists():
                self.log("📝 Processing LI 1 descriptions...\n")
                li1_result = self.fix_episode_descriptions(li1_path, li1_desc)
                self.log(li1_result)
            
            li2_path = session_path / "LI 2"
            if li2_path.exists():
                self.log("\n📝 Processing LI 2 descriptions...\n")
                li2_result = self.fix_episode_descriptions(li2_path, li2_desc)
                self.log(li2_result)
            
            self.log("\n" + "="*60)
            self.log("✨ Description fix complete!")
            self.log("="*60)
            messagebox.showinfo("Success", "Descriptions have been fixed successfully!")
            
        except Exception as e:
            self.log(f"\n❌ Error: {str(e)}")
            messagebox.showerror("Error", str(e))
        
        finally:
            self.is_processing = False
    
    def fix_episode_descriptions(self, li_path, correct_desc):
        result_log = ""
        updated_count = 0
        skipped_count = 0
        error_count = 0
        
        session_folders = [d for d in li_path.iterdir() if d.is_dir()]
        
        for session_folder in session_folders:
            result_log += f"📁 Session: {session_folder.name}\n"
            
            episodes = sorted([d for d in session_folder.iterdir() if d.is_dir() and d.name != "logs"])
            
            for episode in episodes:
                metadata_path = episode / "metadata.json"
                
                if not metadata_path.exists():
                    result_log += f"   ⏭️  {episode.name} - No metadata.json\n"
                    skipped_count += 1
                    continue
                
                try:
                    with open(metadata_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    json_data = json.loads(content)
                    
                    normalized_correct = self.normalize_text(correct_desc)
                    
                    session_desc = json_data.get("session", {}).get("description", "")
                    config_desc = json_data.get("config", {}).get("description", "")
                    
                    normalized_session = self.normalize_text(session_desc)
                    normalized_config = self.normalize_text(config_desc)
                    
                    session_matches = normalized_session == normalized_correct
                    config_matches = normalized_config == normalized_correct
                    
                    if session_matches and config_matches:
                        result_log += f"   ✅ {episode.name} - Already correct (skipped)\n"
                        skipped_count += 1
                        continue
                    
                    updated = False
                    
                    if not session_matches and session_desc:
                        content = self.replace_description(content, "session", session_desc, correct_desc)
                        updated = True
                        result_log += f"   🔄 {episode.name} - Updated session description\n"
                    elif session_matches:
                        result_log += f"   ⏭️  {episode.name} - Session already correct (skipped)\n"
                    
                    if not config_matches and config_desc:
                        content = self.replace_description(content, "config", config_desc, correct_desc)
                        updated = True
                        result_log += f"   🔄 {episode.name} - Updated config description\n"
                    elif config_matches:
                        result_log += f"   ⏭️  {episode.name} - Config already correct (skipped)\n"
                    
                    if updated:
                        with open(metadata_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        updated_count += 1
                    
                except Exception as e:
                    result_log += f"   ❌ {episode.name} - Error: {str(e)}\n"
                    error_count += 1
        
        result_log += f"\n{'─'*50}\n"
        result_log += f"✅ Updated: {updated_count}\n"
        result_log += f"⏭️  Skipped: {skipped_count}\n"
        result_log += f"❌ Errors: {error_count}\n"
        
        return result_log
    
    def normalize_text(self, text):
        return text.lower().replace("  ", " ").strip()
    
    def replace_description(self, content, section, old_desc, new_desc):
        escaped_old = re.escape(old_desc)
        
        pattern = rf'("{section}"\s*:\s*\{{[^}}]*"description"\s*:\s*)"({escaped_old})"'
        
        replacement = rf'\1"{new_desc}"'
        
        return re.sub(pattern, replacement, content, flags=re.DOTALL)

if __name__ == "__main__":
    root = Tk()
    app = SessionFixer(root)
    root.mainloop()

# ================================================================================
# Version 1.0 (Beta)
# © 2025 Kyle Josef Bonachita. All rights reserved.
# Proprietary and Confidential.
# For internal use by the NVIDIA Gear GR00t PH Collections Project.
# Unauthorized distribution prohibited.
# ================================================================================