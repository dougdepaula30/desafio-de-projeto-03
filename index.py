class Heroi:
    # Construtor da classe Heroi, inicializa os atributos nome, idade e tipo
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    # Método que define o ataque do herói com base no tipo
    def atacar(self):
        # Dicionário que associa cada tipo de herói a uma forma de ataque
        ataques = {
            'mago': 'magia',
            'guerreiro': 'espada',
            'monge': 'artes marciais',
            'ninja': 'shuriken'
        }
        # Recupera o ataque baseado no tipo do herói ou define um ataque padrão
        ataque = ataques.get(self.tipo, 'realizou um ataque')
        # Exibe o tipo do herói e o ataque que ele realizou
        print(f"O {self.tipo} atacou usando {ataque}")

# Instanciando objetos da classe Heroi com diferentes atributos
heroi1 = Heroi("Aragorn", 30, "guerreiro")
heroi2 = Heroi("Gandalf", 1000, "mago")
heroi3 = Heroi("Bruce Lee", 32, "monge")
heroi4 = Heroi("Hattori Hanzo", 25, "ninja")

# Chamando o método atacar para cada herói criado
heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()