import tkinter as tk
from tkinter import ttk
import pyautogui
import threading
from tkinter import messagebox

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CLICA-CLICA")
        self.geometry('{}x{}'.format(self.winfo_screenwidth(), self.winfo_screenheight()))

        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#3498db")
        self.style.map("TButton", background=[("active", "#2980b9")])

        self.tab_control = ttk.Notebook(self)
        self.tab_cremer = ttk.Frame(self.tab_control)
        self.tab_speedy = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_cremer, text="Dental Cremer")
        self.tab_control.add(self.tab_speedy, text="Dental Speedy")

        self.tab_control.pack(expand=1, fill="both")

        self.create_cremer_tab()
        self.create_speedy_tab()

        self.loop_cremer_rodando = False
        self.loop_speedy_rodando = False

        self.create_help_button()

    def create_cremer_tab(self):
        frame_cremer = ttk.LabelFrame(self.tab_cremer, text="Aba Dental Cremer")
        frame_cremer.pack(padx=20, pady=20)

        self.botao_iniciar_cremer = ttk.Button(frame_cremer, text="Iniciar Automação Dental Cremer", command=self.iniciar_automacao_cremer)
        self.botao_iniciar_cremer.pack(padx=20, pady=5)

        self.botao_parar_cremer = ttk.Button(frame_cremer, text="Parar Automação Dental Cremer", command=self.parar_automacao_cremer)
        self.botao_parar_cremer.pack(padx=20, pady=5)

    def create_speedy_tab(self):
        frame_speedy = ttk.LabelFrame(self.tab_speedy, text="Aba Dental Speedy")
        frame_speedy.pack(padx=20, pady=20)

        self.botao_iniciar_speedy = ttk.Button(frame_speedy, text="Iniciar Automação Dental Speedy", command=self.iniciar_automacao_speedy)
        self.botao_iniciar_speedy.pack(padx=20, pady=5)

        self.botao_parar_speedy = ttk.Button(frame_speedy, text="Parar Automação Dental Speedy", command=self.parar_automacao_speedy)
        self.botao_parar_speedy.pack(padx=20, pady=5)

    def rodar_loop_cremer(self):
        while self.loop_cremer_rodando:
            pyautogui.PAUSE = 30 
            #abrir navegador
            pyautogui.click(x=1200, y=2097)
            #abrir speedy
            pyautogui.click(x= 1381, y= 2094)
            #atualizar speedy
            pyautogui.click(x=3582, y=278)
            #abrir remoto
            pyautogui.click(x=1522, y=2094)
            pyautogui.click(x=3700, y=2000)
            #minimizar automatico
            pyautogui.click(x=2332, y=24)

    def rodar_loop_speedy(self):
        while self.loop_speedy_rodando:
            pyautogui.PAUSE = 30
            pyautogui.click(x=408, y=747)
            #clicar no speddy
            pyautogui.click(x=459, y=752)
            #ir na primeira tela
            pyautogui.click(x=244, y=663)
            #clicar no speddy
            pyautogui.click(x=459, y=752)
            #ir na segunda tela
            pyautogui.click(x=449, y=661)
            #clicar no speedy
            pyautogui.click(x=459, y=752)
            #ir na terceira tela
            pyautogui.click(x=665, y=663)

    def iniciar_automacao_cremer(self):
        self.loop_cremer_rodando = True
        threading.Thread(target=self.rodar_loop_cremer).start()

    def parar_automacao_cremer(self):
        self.loop_cremer_rodando = False

    def iniciar_automacao_speedy(self):
        self.loop_speedy_rodando = True
        threading.Thread(target=self.rodar_loop_speedy).start()

    def parar_automacao_speedy(self):
        self.loop_speedy_rodando = False

    def create_help_button(self):
        help_button = ttk.Button(self, text="Help", command=self.show_help)
        help_button.place(relx=1, rely=1, anchor="se", x=-10, y=-55)

    def show_help(self):
        help_text = "Para a documentação detalhada acesse: https://github.com/paulofernandodeoliveira/clica-clica.\n(DC)A ordem para o aplicativo funcionar corretamente, deve ser:\nClica-clica -> navegador -> speedy -> speedy remoto\n(DS) A ordem para o aplicativo funcionar corretamente deve seguir: Navegador -> speedy"
        messagebox.showinfo("Ajuda", help_text)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
