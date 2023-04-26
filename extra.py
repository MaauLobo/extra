import sqlite3
import tkinter as tk
from tkinter import messagebox

class BancoDeDados:
    """
    Classe responsável pela conexão e manipulação do banco de dados SQLite
    """
    def __init__(self, db):
        """
        Inicia a conexão com o banco de dados e cria a tabela de alunos, caso ainda não exista
        """
        self.conexao = sqlite3.connect(db)
        self.cursor = self.conexao.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)")
        self.conexao.commit()

    def __del__(self):
        """
        Encerra a conexão com o banco de dados
        """
        self.conexao.close()

    def inserir_aluno(self, nome, idade):
        """
        Insere um aluno no banco de dados
        :param nome: nome do aluno
        :param idade: idade do aluno
        """
        self.cursor.execute("INSERT INTO alunos VALUES (NULL, ?, ?)", (nome, idade))
        self.conexao.commit()

    def atualizar_aluno(self, id, nome, idade):
        """
        Atualiza os dados de um aluno no banco de dados
        :param id: ID do aluno a ser atualizado
        :param nome: novo nome do aluno
        :param idade: nova idade do aluno
        """
        self.cursor.execute("UPDATE alunos SET nome = ?, idade = ? WHERE id = ?", (nome, idade, id))
        self.conexao.commit()

    def excluir_aluno(self, id):
        """
        Exclui um aluno do banco de dados
        :param id: ID do aluno a ser excluído
        """
        self.cursor.execute("DELETE FROM alunos WHERE id = ?", (id,))
        self.conexao.commit()

    def listar_alunos(self):
        """
        Retorna todos os alunos cadastrados no banco de dados
        """
        self.cursor.execute("SELECT * FROM alunos")
        return self.cursor.fetchall()

class JanelaCadastroAluno(tk.Tk):





    def cadastrar(self):
        """ Cadastra um novo aluno no banco de dados"""

        nome = self.ent_nome.get()
        idade = self.ent_idade.get()

        try:
            idade = int(idade)
            self.banco_de_dados.inserir_aluno(nome, idade)
            self.ent_nome.delete(0, tk.END)
            self.ent_idade.delete(0, tk.END)
            tk.messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        except ValueError:
            tk.messagebox.showerror("Erro", "A idade deve ser um número inteiro!")
    """
    Classe responsável pela interface gráfica de cadastro de aluno
    """
    def __init__(self, banco_de_dados):
        """
        Inicia a janela de cadastro de aluno
        :param banco_de_dados: instância da classe BancoDeDados para manipulação do banco de dados
        """
        super().__init__()
        self.title("Cadastro de Aluno")
        self.banco_de_dados = banco_de_dados

        # Criando widgets
        self.lbl_nome = tk.Label(self, text="Nome:")
        self.ent_nome = tk.Entry(self)
        self.lbl_idade = tk.Label(self, text="Idade:")
        self.ent_idade = tk.Entry(self)
        self.btn_cadastrar = tk.Button(self, text="Cadastrar", command=self.cadastrar)

        
        # Posicionando widgets
        self.lbl_nome.grid(row=0, column=0, padx=5, pady=5)
        self.ent_nome.grid(row=0, column=1, padx=5, pady=5)
        self.lbl_idade.grid(row=1, column=0, padx=5, pady=5)
        self.ent_idade.grid(row=1, column=1, padx=5, pady=5)
        self.btn_cadastrar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

class JanelaListagemAlunos(tk.Tk):
    """
    Classe responsável pela interface gráfica de listagem de alunos
    """
    def __init__(self, banco_de_dados):
        """
        Inicia a janela de listagem de alunos
        :param banco_de_dados: instância da classe BancoDeDados para manipulação do banco de dados
        """
        super().__init__()
        self.title("Listagem de Alunos")
        self.banco_de_dados = banco_de_dados

        # Criando widgets
        self.lst_alunos = tk.Listbox(self)
        self.btn_excluir = tk.Button(self, text="Excluir", command=self.excluir)

        # Posicionando widgets
        self.lst_alunos.pack(padx=5, pady=5)
        self.btn_excluir.pack(padx=5, pady=5)

        # Carregando os alunos cadastrados no banco de dados na lista
        alunos = self.banco_de_dados.listar_alunos()
        for aluno in alunos:
            self.lst_alunos.insert(tk.END, f"{aluno[0]} - {aluno[1]} ({aluno[2]} anos)")

    def excluir(self):
        """
        Exclui o aluno selecionado da lista e do banco de dados
        """
        index = self.lst_alunos.curselection()
        if index:
            id_aluno = int(self.lst_alunos.get(index)[0])
            self.banco_de_dados.excluir_aluno(id_aluno)
            self.lst_alunos.delete(index)




    def cadastrar(self):
        """ Cadastra um novo aluno no banco de dados"""

        nome = self.ent_nome.get()
        idade = self.ent_idade.get()

        try:
            idade = int(idade)
            self.banco_de_dados.inserir_aluno(nome, idade)
            self.ent_nome.delete(0, tk.END)
            self.ent_idade.delete(0, tk.END)
            tk.messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        except ValueError:
            tk.messagebox.showerror("Erro", "A idade deve ser um número inteiro!")


class JanelaListagemAlunos(tk.Tk):
    """
    Classe responsável pela interface gráfica de listagem de alunos
    """
    def __init__(self, banco_de_dados):
        """
        Inicia a janela de listagem de alunos
        :param banco_de_dados: instância da classe BancoDeDados para manipulação do banco de dados
        """
        super().__init__()
        self.title("Listagem de Alunos")
        self.banco_de_dados = banco_de_dados

        # Criando widgets
        self.lst_alunos = tk.Listbox(self)
        self.btn_excluir = tk.Button(self, text="Excluir", command=self.excluir)

        # Posicionando widgets
        self.lst_alunos.pack(padx=5, pady=5)
        self.btn_excluir.pack(padx=5, pady=5)

        # Carregando os alunos cadastrados no banco de dados na lista
        alunos = self.banco_de_dados.listar_alunos()
        for aluno in alunos:
            self.lst_alunos.insert(tk.END, f"{aluno[0]} - {aluno[1]} ({aluno[2]} anos)")

    def excluir(self):
        """
        Exclui o aluno selecionado da lista e do banco de dados
        """
        index = self.lst_alunos.curselection()
        if index:
            id_aluno = int(self.lst_alunos.get(index)[0])
            self.banco_de_dados.excluir_aluno(id_aluno)
            self.lst_alunos.delete(index)
            tk.messagebox.showinfo("Sucesso", "Aluno excluído com sucesso!")
        else:
            tk.messagebox.showerror("Erro", "Selecione um aluno para excluir!")



class Principal:
    """
    Classe responsável por iniciar a aplicação
    """
    def __init__(self):
        self.bd = BancoDeDados("alunos.db")
        self.janela_cadastro = JanelaCadastroAluno(self.bd)
        self.janela_listagem = JanelaListagemAlunos(self.bd)
        self.janela_cadastro.mainloop()
        self.janela_listagem.mainloop()
    

if __name__ == '__main__':
    app = Principal()

