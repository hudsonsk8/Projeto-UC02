import tkinter as tk


# Cores e fontes
BG_COLOR = "#f0f8ff"
FG_COLOR = "#003366"
FONT_TITULO = ("Helvetica", 18, "bold")
FONT_TEXTO = ("Helvetica", 12)


def opcao_selecionada(texto):
    label.config(text=texto)


def home():
    opcao_selecionada("Seja bem-vindo(a) ao site de Psicologia. Aqui você encontrará a melhor forma para sua experiência.")


def sobre():
    opcao_selecionada("Finalidade do site: Este é um sistema de atendimento psicológico desenvolvido para melhorar sua saúde mental e bem-estar. Biografia da psicóloga: ...")


def agendamentos():
    opcao_selecionada("Para mais informações e negociações entre em contato ou acesse o ChatBot.")


def atendimentos():
    opcao_selecionada("Tipos de atendimento: adultos, casais, idosos, empresas e grupos interessados, conforme NR-1.")


def outros():
    opcao_selecionada("Acesse nossos artigos sobre psicologia, palestras, bem-estar e desenvolvimento pessoal.")


def chatbot():
    opcao_selecionada("Olá! Seja bem-vindo(a), eu me chamo LibBot. Em que posso lhe ajudar?")


# Criar janela principal
barra = tk.Tk()
barra.title("Menu de Interação")
barra.geometry("700x400")
barra.configure(bg=BG_COLOR)


# Menu horizontal
menu = tk.Menu(barra)
menu.add_command(label="Home", command=home)
menu.add_command(label="Sobre", command=sobre)
menu.add_command(label="Agendamentos", command=agendamentos)
menu.add_command(label="Atendimentos", command=atendimentos)
menu.add_command(label="ChatBot", command=chatbot)
menu.add_command(label="Outros", command=outros)
menu.add_command(label="Sair", command=barra.quit)
barra.config(menu=menu)


# Título
titulo = tk.Label(barra, text="Libélula Psi", font=FONT_TITULO,
                  bg=BG_COLOR, fg=FG_COLOR)
titulo.pack(pady=(10, 0))


# Label de exibição
label = tk.Label(barra, text="Navegue através do nosso menu acima.",
                 font=FONT_TEXTO, bg=BG_COLOR, fg=FG_COLOR, wraplength=650, justify="center")
label.pack(pady=40)


# Rodapé
rodape = tk.Label(barra, text="2025 Psicologia e Bem-Estar. Todos os direitos reservados.",
                  font=("Helvetica", 10), bg=BG_COLOR, fg="#666666")
rodape.pack(side="bottom", pady=10)


# Rodar o app
barra.mainloop()
