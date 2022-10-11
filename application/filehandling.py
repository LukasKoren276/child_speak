import json
import tkinter as tk
from tkinter import filedialog


class Files:
    
    @staticmethod
    def open_file(path):
        with open(path, 'r') as file:
            for word in file:
                yield word.strip()
                
    @staticmethod
    def save_to_file(what, path):
        with open(path, 'w', encoding='utf-8') as file:
            file.write(what)
            
    @staticmethod
    def load_json(path):  
        with open(path, "r") as read_file:
            data = json.load(read_file)
        return data
    
    @staticmethod
    def write_json(what, path):
        with open(path, "w") as write_file:
            json.dump(what, write_file, indent=4)
            
    @staticmethod
    def dialog_file_picker(filetype='', init_dir=''):
        root = tk.Tk()
        if filetype == 'csv':
            ft = [('CSV Files', '*.csv')]
            de = '.csv'
        elif filetype == 'joblib':
            ft = [('joblib files', '*.joblib')]
            de ='.joblib'
        elif filetype == 'txt':
            ft = [("text files","*.txt")]
            de =".txt"
        else:
            ft = ''
            de = ''
        file_path = filedialog.askopenfilename(
            filetypes=ft, 
            defaultextension=de, 
            initialdir = init_dir)
        root.destroy()
        return file_path