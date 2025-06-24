import tkinter as tk
from tkinter import messagebox

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
    def continuar_fluxo():
        try:
            tipo = int(entry.get())
            if tipo == 1:
                janela_chat.destroy()
                chat_pessoa_fisica()
            elif tipo == 2:
                janela_chat.destroy()
                chat_pessoa_juridica()
            else:
                label_chat.config(text="Por favor, digite 1 para pessoa física ou 2 para pessoa jurídica.")
        except ValueError:
            label_chat.config(text="Entrada inválida. Por favor, digite 1 ou 2.")

    janela_chat = tk.Toplevel(barra)
    janela_chat.title("LibBot - Assistente Virtual")
    janela_chat.geometry("500x200")
    janela_chat.configure(bg=BG_COLOR)

    label_chat = tk.Label(janela_chat, text="Olá! Para melhor te atender:\nVocê é pessoa física (1) ou jurídica (2)?",
                          font=FONT_TEXTO, bg=BG_COLOR, fg=FG_COLOR, wraplength=480, justify="left")
    label_chat.pack(pady=10)

    entry = tk.Entry(janela_chat, font=FONT_TEXTO)
    entry.pack(pady=5)

    btn_enviar = tk.Button(janela_chat, text="Enviar", command=continuar_fluxo)
    btn_enviar.pack(pady=5)

def chat_pessoa_fisica():
    def enviar_dados():
        nome = entrada_nome.get()
        idade = entrada_idade.get()
        cpf = entrada_cpf.get()
        cep = entrada_cep.get()

        if not idade.isdigit() or int(idade) < 18:
            messagebox.showwarning("Idade inválida", "Não trabalhamos com pessoas menores de 18 anos.")
            return

        idade_int = int(idade)
        atendimento = var_atendimento.get()

        msg = f"Nome: {nome}\nIdade: {idade_int}\nCPF: {cpf}\nCEP: {cep}\n"

        if atendimento == "grupo":
            msg += "Atendimento em grupo selecionado.\n"
        elif atendimento == "casal":
            msg += "Atendimento para casal selecionado.\n"
        elif atendimento == "individual":
            msg += "Atendimento individual selecionado.\n"
         
        msg += "\nAssim que possível, a psicóloga Patrícia Marques entrará em contato com você.\nAgradecemos a preferência!"

        messagebox.showinfo("Dados Recebidos", msg)

    janela = tk.Toplevel()
    janela.title("Pessoa Física")
    janela.geometry("400x400")

    tk.Label(janela, text="Nome:").pack()
    entrada_nome = tk.Entry(janela)
    entrada_nome.pack()

    tk.Label(janela, text="Idade:").pack()
    entrada_idade = tk.Entry(janela)
    entrada_idade.pack()

    tk.Label(janela, text="CPF (ex: 000.000.000-00):").pack()
    entrada_cpf = tk.Entry(janela)
    entrada_cpf.pack()

    tk.Label(janela, text="CEP (ex: 00000-000):").pack()
    entrada_cep = tk.Entry(janela)
    entrada_cep.pack()

    tk.Label(janela, text="Tipo de atendimento:").pack()
    var_atendimento = tk.StringVar(value="individual")
    tk.Radiobutton(janela, text="Grupo", variable=var_atendimento, value="grupo").pack()
    tk.Radiobutton(janela, text="Casal", variable=var_atendimento, value="casal").pack()
    tk.Radiobutton(janela, text="Individual", variable=var_atendimento, value="individual").pack()

    tk.Button(janela, text="Enviar", command=enviar_dados).pack(pady=10)

def chat_pessoa_juridica():
    def enviar_dados():
        nome_emp = entrada_nome.get()
        cnpj = entrada_cnpj.get()
        cep = entrada_cep.get()
        espac_audi = var_espaco.get()
        tipo_evento = var_evento.get()

        if not nome_emp or not cnpj or not cep:
            messagebox.showwarning("Dados incompletos", "Por favor, preencha todos os campos.")
            return

        msg = f"Empresa: {nome_emp}\nCNPJ: {cnpj}\nCEP: {cep}\n"
        msg += f"Espaço para apresentações: {'Sim' if espac_audi == 1 else 'Não'}\n"

        eventos_dict = {
            1: "Workshop presencial sobre norma NR-1",
            2: "Workshop online sobre norma NR-1",
            3: "Palestra presencial",
            4: "Palestra online"
        }

        if tipo_evento not in eventos_dict:
            messagebox.showwarning("Erro", "Selecione um tipo de evento válido.")
            return

        msg += f"Evento: {eventos_dict[tipo_evento]}\n"

        # Campos adicionais para alguns eventos
        if tipo_evento in [1, 2, 3, 4]:
            quant_pessoas = entrada_quant.get()
            if not quant_pessoas.isdigit() or int(quant_pessoas) <= 0:
                messagebox.showwarning("Erro", "Informe uma quantidade válida de pessoas.")
                return
            msg += f"Quantidade de pessoas: {quant_pessoas}\n"

        if tipo_evento in [2, 4]:  # eventos online - escolher app
            app = var_app.get()
            apps = {1: "Microsoft Teams", 2: "Google Meet", 3: "WhatsApp"}
            app_nome = apps.get(app, "Nenhum")
            msg += f"Aplicativo preferido: {app_nome}\n"

        if tipo_evento in [3,4]:  # palestras - assunto
            assunto = entrada_assunto.get()
            if not assunto.strip():
                messagebox.showwarning("Erro", "Informe o assunto da palestra.")
                return
            msg += f"Assunto da palestra: {assunto}\n"

        msg += "\nAssim que possível a psicóloga Patrícia Marques entrará em contato com você.\nObrigado pela preferência!"

        messagebox.showinfo("Cadastro Finalizado", msg)
        janela.destroy()

    janela = tk.Toplevel()
    janela.title("Pessoa Jurídica")
    janela.geometry("400x450")

    tk.Label(janela, text="Nome da empresa:").pack()
    entrada_nome = tk.Entry(janela)
    entrada_nome.pack()

    tk.Label(janela, text="CNPJ (ex: 00.000.000/0000-00):").pack()
    entrada_cnpj = tk.Entry(janela)
    entrada_cnpj.pack()

    tk.Label(janela, text="CEP (ex: 00000-000):").pack()
    entrada_cep = tk.Entry(janela)
    entrada_cep.pack()

    tk.Label(janela, text="Sua empresa possui espaço para apresentações?").pack()
    var_espaco = tk.IntVar(value=2)
    tk.Radiobutton(janela, text="Sim", variable=var_espaco, value=1).pack()
    tk.Radiobutton(janela, text="Não", variable=var_espaco, value=2).pack()

    tk.Label(janela, text="Qual evento melhor atende às suas necessidades?").pack()
    var_evento = tk.IntVar(value=0)
    tk.Radiobutton(janela, text="Workshop presencial sobre norma NR-1", variable=var_evento, value=1).pack()
    tk.Radiobutton(janela, text="Workshop online sobre norma NR-1", variable=var_evento, value=2).pack()
    tk.Radiobutton(janela, text="Palestra presencial", variable=var_evento, value=3).pack()
    tk.Radiobutton(janela, text="Palestra online", variable=var_evento, value=4).pack()

    tk.Label(janela, text="Para quantas pessoas será a apresentação?").pack()
    entrada_quant = tk.Entry(janela)
    entrada_quant.pack()

    tk.Label(janela, text="Assunto da palestra (se aplicável):").pack()
    entrada_assunto = tk.Entry(janela)
    entrada_assunto.pack()

    tk.Label(janela, text="Aplicativo preferido (para eventos online):").pack()
    var_app = tk.IntVar(value=0)
    tk.Radiobutton(janela, text="Microsoft Teams", variable=var_app, value=1).pack()
    tk.Radiobutton(janela, text="Google Meet", variable=var_app, value=2).pack()
    tk.Radiobutton(janela, text="WhatsApp", variable=var_app, value=3).pack()

    tk.Button(janela, text="Enviar", command=enviar_dados).pack(pady=10)


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
