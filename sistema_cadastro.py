
import PySimpleGUI as sg 

class Aluno:

    def __init__(self, nome, matricula, curso, telefone, email, senha):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.telefone = telefone
        self.email = email
        self.senha = senha

    def todos_alunos():
        pass


class Interface:
    def __init__(self):
        layout = [
            [sg.Text('Name        '), sg.Input(key='nome')],
            [sg.Text('Matrícula   '), sg.Input(key='matricula')], 
            [sg.Text('Curso        '), sg.InputCombo(
                ('Ciências da Computação', 'Engenharia da Computação'), key='curso', readonly=True)],
            [sg.Text('Telefone    '), sg.Input(key='telefone')], 
            [sg.Text('Email        '), sg.Input(key='email')],
            [sg.Text('Senha       '), sg.Input(key='senha', password_char='*')], 

            [sg.Button('Cadastrar'), sg.Cancel()]    
            
        ]
        self.window = sg.Window('Cadastro de Alunos', layout)

    def executando(self):
        lista_cadastrados = []

        while(True):
            self.event, self.values = self.window.read()
            if self.event in (None, 'Cancel'):
                break

            if self.event in ('Cadastrar'):
                nome = self.values['nome']
                matricula = self.values['matricula']
                curso = self.values['curso']
                telefone = self.values['telefone']
                email = self.values['email']
                senha = self.values['senha']

                try:
                    aluno = Aluno(nome, matricula, curso, telefone, email, senha)
                    print(self.values)
                    lista_cadastrados.append(aluno)
                    print('Aluno cadastrado!')
                except:
                    print('Erro no cadastro!')            
        
        print('Cadastrados:')
        for cadastrado in lista_cadastrados:
            print(cadastrado.nome)
            
        self.window.close()


if __name__ == "__main__":
    interface_cadastro = Interface()
    interface_cadastro.executando()


