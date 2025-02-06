import webbrowser
import os

# Mensaje de detalle en HTML con un sobre clicable
html = """
<!DOCTYPE html>
<html>
<head>
<title>Un pequeño detalle para ti</title>
<style>
    body { text-align: center; font-family: Arial, sans-serif; margin: 0; padding: 20px; }
    .envelope { cursor: pointer; margin-top: 50px; width: 100%; max-width: 200px; }
    .message { display: none; margin-top: 50px; }
    img { width: 100%; max-width: 250px; }
</style>
<script>
    function openMessage() {
        document.getElementById('message').style.display = 'block';
        document.getElementById('envelope').style.display = 'none';
    }
</script>
</head>
<body>
<h1>🌹Hola Damaris!🌹</h1>
<p>Por favor haga clic en el sobre para abrir el mensaje😉:</p>
<img id="envelope" class="envelope" src="https://i.pinimg.com/736x/b3/4d/34/b34d342d4fd2082809e0d221c82dcef6.jpg" alt="Sobre" onclick="openMessage()">
<div id="message" class="message">
    <p>Espero que este pequeño detalle te saque una sonrisa.😁🌹</p>
    <p>Me alegro de haber podido conocerte y asi mismo poder conversar contigo e intercambair unos pocos mensajes, espero que siempre este bien y siempre cuentas conmigo para lo que necesites. Te agradezco el tiempo que te das para leer y ver este pequeño detalle.</p>
    <p><img src="https://us.123rf.com/450wm/siberianart/siberianart2001/siberianart200100109/138251678-dos-corazones-rojos-con-ni%C3%B1os-y-ni%C3%B1as-charlando-conoci%C3%A9ndose-usando-tel%C3%A9fonos-m%C3%B3viles-ilustraci%C3%B3n.jpg?ver=6" alt="Corazón"></p>
    <p>En lo poco que hemos hablado he notado lo maravillosa que eres, una gran mujer, que es responsables y dedicada por sus estudios, amable y respetuosa con los demas y obviamente la mas hermosa. Algo que no hice antes es agradacerte porhaberme dado la oportunidad de conocerte, ahora la verdad es que no quiero solo conocerte si no que tambien me gustaria conquistarte y demostrarte que me importas y me gustas por que considero que eres unica y asi mismo una mujer por la que vale la pena esperar (espero no tener que esperar tanto jajaj).❤🙌🌹</p>
    <p>Te envio un abrazo, y nunca olvides sonreír y ser la luz que ilumina la vida de todos quienes te conocemos. Mientras llega el momento de encontrarnos, en el que me permitas invitarte a salir, te dejo este pequeño detalle🙌. Espero sea de tu agrado, no olvidesque cuentas siempre conmigo y que espero algun dia me permitas llamarte, talvez podria llamarte para saber si te gusto este pequeño detalle?<br>
    Att: Anthony.😊</p>
    <p>🌹Ты самая красивая и никогда не меняешься.🌹</p>
</div>
</body>
</html>
"""

# Guarda el mensaje en un archivo HTML con codificación UTF-8
with open("detalle_para_damaris.html", "w", encoding="utf-8") as file:
    file.write(html)

# Abre el archivo HTML en una nueva pestaña del navegador
webbrowser.open("file://" + os.path.realpath("detalle_para_damaris.html"))
