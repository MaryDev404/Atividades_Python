class Livro:
    def __init__(self, titulo, autor, isbn,):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = "sim"
     
    def emprestar(self):
            if self.disponivel == "sim":
                self.disponivel = "não"
                print("Livro emprestado com sucesso!")
            else:
                print("Este livro já está emprestado.")
    
    def devolver(self):
            if self.disponivel == "não":
                self.disponivel = "sim"
                print("Livro devolvido com sucesso!")
            else:
                print("Este livro já está disponível.")


    def descricao(self):
            print("\n--- Descrição do Livro ---")
            print(f"Título: {self.titulo}")
            print(f"Autor: {self.autor}")
            print(f"isbn: {self.isbn}")


livros = [
    Livro("Black Clover", "Yuki Tabata", "001"),
    Livro("Diário de uma Apotecária", "Natsu Hyuga", "002"),
    Livro("Noragami", "Adachitoka", "003"),
    Livro("Bungou Stray Dogs", "Kafka Asagiri", "004")
]


class Usuario:


    def __init__(self, nome):
        self.nome = nome
        self.limite = 1
        self.emprestados = []


    def pegar_livro(self, livro):
        if len(self.emprestados) < self.limite:
            livro.emprestar()
            self.emprestados.append(livro)


class Aluno(Usuario):
     def __init__(self, nome):
          super().__init__(nome)
          self.limite = 2


class Professor(Usuario):
     def __init__(self, nome):
          super().__init__(nome)
          self.limite = 5