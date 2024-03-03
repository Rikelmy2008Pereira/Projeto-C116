# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Matheus" # escreva seu nome
    idade = "10" # escreva sua idade

    return render_template('index.html' , name = nome , age = idade)

# defina a rota para a página do pai

@app.route("/pai")
def father():
    
    nome = "Miguel"
    idade = "48"
    
    return render_template("pai.html", nome = nome, idade = idade)

# defina a rota para a página da mãe


@app.route("/mae")
def mother():
    
    nome = "Emilly"
    idade = "32"
    
    return render_template("mae.html", nome = nome, idade = idade)

# defina a rota para a página do amigo


@app.route("/amigo")
def friend():
    
    nome = "Marcos"
    idade = "10"
    
    return render_template("amigo.html", nome = nome , idade = idade)

# adicione outras rotas, se você quiser

# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
