import tkinter as tk

def opcao_selecionada(opcao):
    label.config(text=f" {opcao}")

# Criar janela principal
barra = tk.Tk()
barra.title("Menu de Interação")

# Criar um menu
menu = tk.Menu(barra)

# Criar submenu
submenu = tk.Menu(menu, tearoff=0)
submenu.add_command(label="Home", command=lambda: opcao_selecionada("Seja Bem-vindos ao site de Psicologia, aqui você encontrar a melhora forma para sua experiencia"))
submenu.add_command(label="Sobre", command=lambda: opcao_selecionada("Sobre"))
submenu.add_command(label="Tipos de Atendimentos", command=lambda: opcao_selecionada(" (Palestras, palestra sobre NR-1, Atendimento em grupo e atendimento pessoal)."))
submenu.add_command(label=" Atendimento Especifico", command=lambda: opcao_selecionada("Adultos, casais, senhores (a)  de idade, empresas e grupos interessados."))
submenu.add_command(label="Artigos", command=lambda: opcao_selecionada("Contato"))
submenu.add_command(label="ChatBoat", command=lambda: opcao_selecionada("Olá! Seja Bem - vindo, eu me chamo MatheusGPT, o que posso lhe ajudar?"))
submenu.add_separator()
submenu.add_command(label="Sair", command=barra.quit)

menu.add_cascade(label="Menu", menu=submenu)

# Configurar a janela para usar o menu
barra.config(menu=menu)

# Label para mostrar a opção selecionada
label = tk.Label(barra, text=" Navegar através do nosso menu ao lado.", font=("Arial", 12))
label.pack(pady=20)

# Executar a aplicação
barra.mainloop()
