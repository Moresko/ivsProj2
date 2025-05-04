"""
@file calc.py
@package calc
@brief Balík implementujúci GUI a hlavny tok programu.
======== Copyright (c) 2023, FIT VUT Brno, All rights reserved. ============

 Purpose:     IVS 2nd project - package desc

 $NoKeywords: $ivs_project_2 $calc.py
@author $Authors:    Filip Botlo <xbotlo01@stud.fit.vutbr.cz>
 $Date:       $2023-03-13
============================================================================
"""
 # @brief GUI pripojenie na controller 
import tkinter as tk
from tkinter import messagebox
from controller import Controller
#ahoj
 # @brief nastavenie vizuálnej identity knižnice 

## Veľký font písma
LARGE_FONT_STYLE = ("Arial", 40)
## Malý font písma
SMALL_FONT_STYLE = ("Arial", 16)
## Font číslic
DIGITS_FONT_STYLE = ("Arial", 24)
## Základný font
DEFAULT_FONT_STYLE = ("Arial", 20)

## svetlo ruzova farba
LIGHT_PINK = "#FFEBF0"
## svetlo ruzova farba
LIGHT_PINK2 = "#FFEBF0"
#stredne ruzova farba
MEDIUM_PINK = "#FFB3C6"
## Farba písma
LABEL_COLOR = "#25265E"
## tmavo ruzova farba
DARK_PINK = "#FB6F92"

class Calculator:
    """ @brief Trieda reprezentujúca GUI.
    """

    def __init__(self):
        """@brief Inicializácia GUI
        """
        self.controller = Controller()
        self.window = tk.Tk()
        self.window.geometry("400x700")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        
        title_frame = tk.Frame(self.window, bg=LIGHT_PINK, height=30)
        title_frame.pack(fill="x")
        title_label = tk.Label(title_frame, text="", fg="white", bg=LIGHT_PINK, font=("Helvetica", 14))
        title_label.pack(side="left", padx=10)
        help_button = tk.Button(title_frame, text="?", bg=DARK_PINK, fg="white", activebackground=LIGHT_PINK2, activeforeground="white", command=self.show_help)
        help_button.pack(side="right", padx=10)
        
        self.cely_vyraz = ""
        self.vyraz = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()
        self.digits = {
            7: (2, 1), 8: (2, 2), 9: (2, 3),
            4: (3, 1), 5: (3, 2), 6: (3, 3),
            1: (4, 1), 2: (4, 2), 3: (4, 3),
            0: (5, 2), '.': (5, 1)
        }
        self.operations = {"%" : "%", "/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self. brackets = {"(" : "(", ")" : ")"}
        self.spec_ops = {"!" : "!", "^" : "^", "\u221a" : "\u221a" }
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_bracket_buttons()
        self.create_spec_ops()
        self.create_special_buttons()
        self.klavesnica()
    
        
    def show_help(self):
        """@brief Help správa na pouzitie kalkulačky
        """
        help_window = tk.Toplevel(self.window)
        help_window.title("Help")
        help_text = tk.Label(help_window, text="Vitajte v aplikácii kalkulačka!\n\nTu sú jednoduché pokyny, ako používať kalkulačku:\n\n1. Do prvého pola napíšte alebo vyberte prvé číslo, s ktorým chcete pracovať.\n2. Do druhého pola napíšte alebo vyberte druhé číslo, s ktorým chcete pracovať.\n3. Vyberte medzi nimi operáciu, ktorú chcete použiť z rozbaľovacieho menu.\n 4. Pri výpočtoch s jedným operandom zadajte operand ako prvý.\n5. Stlačte tlačidlo 'Vypočítaj' a zobrazí sa vám výsledok.")
        help_text.pack(padx=20, pady=20)
        
    def klavesnica(self):
        """ @brief Pisanie na klavesnici.
        """
        self.window.bind("<Return>", lambda event: self.evaluate())
        
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit = key: self.add_to_expression(digit))
        
        for key in self.operations:
            self.window.bind(str(key), lambda event, op = key: self.add_to_expression(op))
            
        for key in self.brackets:
            self.window.bind(str(key), lambda event, br = key: self.add_to_expression(br))
        
        for key in list(self.spec_ops.keys())[0:2]:
            self.window.bind(str(key), lambda event, so = key: self.add_to_expression(so))
            
        self.window.bind("<BackSpace>", lambda event: self.back())    
        

    def create_special_buttons(self):
        """@brief Inicializácia špeciálnych tlačidiel.
        """
        self.create_clear_button()
        self.create_equals_button()
        self.create_back_button()

    def create_display_labels(self):
        """@brief Inicializácia zobrazovania výsledkov.
        """
        total_label = tk.Label(self.display_frame, text=self.cely_vyraz, anchor=tk.E, bg=LIGHT_PINK,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.vyraz, anchor=tk.E, bg=LIGHT_PINK,
                         fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        """@brief Inicializácia okna zobrazovania výsledkov.
        """
        frame = tk.Frame(self.window, height=150, bg=LIGHT_PINK)
        frame.pack(expand=True, fill="both")
        return frame
    
    def add_to_expression(self, value):
        """@brief Aktualizácia zobrazeného výsledku.
        @param Pridaný charakter k výsledku
        """
        self.vyraz += str(value)
        self.update_label()
        
    def create_digit_buttons(self):
        """@brief Inicializácia číselných tlačidiel.
        """
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=LIGHT_PINK2, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                            borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
            
    def append_operator(self,operator):
        """@brief Pridanie operátora do výrazu.

        Args:
            @param operator: pridávaný operátor.
        """
        self.vyraz += operator
        self.cely_vyraz += self.vyraz
        self.vyraz = ""
        self.update_total_label()
        self.update_label()
        
    def create_operator_buttons(self):
        """@brief Inicializácia tlačidiel operátorov.
        """
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=MEDIUM_PINK, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command = lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        """@brief Vyčistenie zobrazených výsledkov.
        """
        self.vyraz = ""
        self.cely_vyraz=""
        self.update_label()
        self.update_total_label()
    
    def create_clear_button(self):
        """@brief Inicializácia čistiaceho tlačidla.
        """
        button = tk.Button(self.buttons_frame, text="C", bg=DARK_PINK, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)
        
    def back(self):
        """@brief Odmazanie posledného znaku zo zobrazeného výsledku
        """
        if len(self.vyraz) > 0:
            self.vyraz = self.vyraz[:-1] # remove last character
            self.update_label()
     
    def create_back_button(self):
        """@brief Inicializácia tlačidla odmazávania.
        """
        button = tk.Button(self.buttons_frame, text="<", bg=LIGHT_PINK, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command = self.back)
        button.grid(row=5, column=3, sticky=tk.NSEW)

    def create_spec_ops(self):
        """@brief Inicializácia tlačidiel špeciálnych operátorov.
        """
        i = 0
        for operator, symbol in self.spec_ops.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=MEDIUM_PINK, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command = lambda x=operator: self.append_operator(x))
            button.grid(row=1, column=i+ 1, sticky=tk.NSEW)
            i += 1    

    def evaluate(self):
        """@brief Výpočet výrazu.

        Funkcia pre výpočet cez inštanciu triedz controller.Controller volá funkciu controller.Controller.calc().
        """
        
        self.cely_vyraz += self.vyraz
        self.update_total_label()
        
        result = self.controller.calc(str(self.cely_vyraz))
        self.vyraz = str(result)[:12]
        self.update_label()
        self.cely_vyraz = ""

    def create_equals_button(self):
        """@brief Inicializácia tlačidla výpočtu.
        """
        button = tk.Button(self.buttons_frame, text="=", bg=DARK_PINK, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command = self.evaluate)
        button.grid(row=5, column=4, sticky=tk.NSEW)
        
    def append_bracket(self, bracket):
        """@brief Pridanie zátvorky na koniec výrazu.

        Args:
            @param bracket: pridávaná zátvorka
        """
        self.vyraz += bracket
        self.cely_vyraz += self.vyraz
        self.vyraz = ""
        self.update_total_label()
        self.update_label()

    def create_bracket_buttons(self):
        """@brief Inicializácia tlačidiel zátvoriek.
        """
        i = 0
        for bracket, symbol in self.brackets.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=MEDIUM_PINK, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command = lambda x=bracket: self.append_bracket(x))
            button.grid(row=0, column=i+2, sticky=tk.NSEW)
            i += 1
        
    def create_buttons_frame(self):
        """@brief Inicializácia podkladu pre tlačidlá kalkulačky.
        """
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    
    def update_total_label(self):
        """@brief Aktualizácia zobrazeného výsledku.
        """
        self.total_label.config(text=self.cely_vyraz)
    
    def update_label(self):
        """@brief Aktualizácia zobrazeného čiastočného výsledku.
        """
        self.label.config(text=self.vyraz)
        
    def run(self):
        """@brief Spustenie GUI.
        """
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
