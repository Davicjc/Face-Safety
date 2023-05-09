# Este é um programa em Python que usa a biblioteca de reconhecimento facial "face recognition". 
# Ele permite adicionar fotos ao banco de dados,
# excluir pessoas do banco de dados,
# ativar o modo scanner que apresenta o nome da pessoa ao entrar de frente a câmera. 
# O programa pode ser usado para segurança ou controle de acesso caso seja adaptado.
# Feito por Davicjc por meio de pesquisas e estudos de bibliotecas além do estudo de códigos de terceiros.

# "LER NO GITHUB AS INSTRUÇÕES ANTES DE USAR O PROGRAMA. (EM PORTUGUÊS)"

#importa as bibliotecas necessárias
import cv2, os, random, numpy as np, glob, face_recognition, tkinter as tk, webbrowser

# Função que cria a janela principal
def lobby():
    # Cria uma janela
    Lobby = tk.Tk()

    #Bloqueia o redimensionamento da janela
    Lobby.resizable(width=False, height=False)

    # Define o título da janela
    Lobby.title("FACE SAFETY")

    # Define o tamanho da janela
    Lobby.geometry("320x240")

    # Define a cor de fundo da janela
    Lobby.configure(background="black")

    # Define os componentes da janela
    txt_label = tk.Label(Lobby, text="Bem vindo ao Face Safety \no que deseja fazer?", font=("Arial", 18), bg="black", fg="white")
    Badd_button = tk.Button(Lobby, text="Add Pessoa", font=("Arial", 12), bg="black", fg="blue",cursor="hand2" , command=nome)
    Bremv_button = tk.Button(Lobby, text="Rmv Pessoa", font=("Arial", 12), bg="black", fg="red",cursor="hand2" , command=apagar_imagem)
    Scan_button = tk.Button(Lobby, text="Lgr Scanner", font=("Arial", 12), bg="black", fg="green",cursor="hand2" , command=reconhecer)
    cjc_label = tk.Label(Lobby, text="By: Davicjc", font=("Arial", 8), bg="black", fg="blue", cursor="hand2")

    # Posiciona os componentes na janela
    txt_label.pack()
    Badd_button.place(x=10, y=100)
    Bremv_button.place(x=10, y=150)
    Scan_button.place(x=10, y=200)
    cjc_label.place(x=255, y=220)

    #Serve para chamar a função "Davi" quando o botão for clicado
    cjc_label.bind("<Button-1>", lambda event: Davi())

    def Davi():
        webbrowser.open("https://github.com/Davicjc/")

    #Loop da janela
    Lobby.mainloop()

# Função que captura o nome da pessoa
def nome():

    # Cria uma janela
    nome = tk.Tk()

    #Bloqueia o redimensionamento da janela
    nome.resizable(width=False, height=False)

    # Define o título da janela
    nome.title("Seu Nome:")

    # Define o tamanho da janela
    nome.geometry("290x60")

    # Define a cor de fundo da janela
    nome.configure(background="black")

    # Chama a função que captura a imagem e apaga os componentes da janela "nome()"
    def clear():
        namep = nm_entry.get()
        if namep == "":
            name = "Sem Nome-" + str(random.randint(1, 1000)) + ".jpg"
        else:
            name = namep + ".jpg"    
        nome.destroy()
        nova_imagem(name)

    # Define os componentes da janela
    nm_entry = tk.Entry(nome, width=40)
    nm_button = tk.Button(nome, text="OK", font=("Arial", 9), bg="black", fg="white",cursor="hand2" ,command=clear)
    recado_label = tk.Label(nome, text="As fotos serão armazenadas na área de trabalho!", font=("Arial", 9), bg="black", fg="red")

    # Posiciona os componentes na janela
    nm_entry.place(x=5, y=8)
    nm_button.place(x=260, y=5)
    recado_label.place(x=5, y=37)

    #Loop da janela
    nome.mainloop()

# Função que captura a imagem da câmera com o nome da pessoa
def nova_imagem(name):
    # Define o nome da pasta onde as fotos serão salvas
    folder_name = "Fotos Data 'Face Safety'"

    # Define o caminho completo da pasta na área de trabalho
    desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    folder_path = os.path.join(desktop_path, folder_name)

    # Verifica se a pasta já existe, caso contrário, cria a pasta
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Captura a imagem da câmera
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # Aguarda o usuário apertar qualquer tecla para tirar a sua foto
    while True:
        ret, frame = cap.read()
        cv2.imshow("Captura Rosto - 'Aperte Qualquer Tecla'", frame)
        if cv2.waitKey(1) != -1:
            break

    # Salva a imagem capturada na pasta criada
    file_path = os.path.join(folder_path, name)
    cv2.imwrite(file_path, frame)

    # Libera a câmera e fecha a janela
    cap.release()
    cv2.destroyAllWindows()

# Função que apaga a imagem da pessoa
def apagar_imagem():

    # Cria uma janela
    apgrt = tk.Tk()

    #Bloqueia o redimensionamento da janela
    apgrt.resizable(width=False, height=False)

    # Define o título da janela
    apgrt.title("Apagar Pessoa: ")

    # Define o tamanho da janela
    apgrt.geometry("360x200")

    # Define a cor de fundo da janela
    apgrt.configure(background="black")

    # Apagar a imagem selecionada
    esc_label = tk.Label(apgrt, text="Escreva o nome que deseja apagar:", font=("Arial", 9), bg="black", fg="white")
    esc_label.place(x=145, y=5)

    def apagar():
        namep = esc_entry.get()
        name = namep + ".jpg"
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        folder_path = os.path.join(desktop_path, "Fotos Data 'Face Safety'")
        files = os.listdir(folder_path)
        for i in range(len(files)):
            if files[i] == name:
                os.remove(folder_path + "\\" + name)
                break

    # Mensagem e avisos
    avs_label = tk.Label(apgrt, text="Reinicie a aba para atualizar a lista", bg="black", fg="red")
    avs_label.place(x=160, y=180)

    # Campo de texto para digitar o nome da pessoa
    esc_entry = tk.Entry(apgrt, width=30)
    esc_entry.place(x=150, y=30)

    # Seleciona a imagem da pessoa
    esc_Button = tk.Button(apgrt, text="Apagar", font=("Arial", 9), bg="black", fg="white",cursor="hand2", command=apagar)
    esc_Button.place(x=150, y=60)

    #  Lista de nomes das pessoas
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    folder_path = os.path.join(desktop_path, "Fotos Data 'Face Safety'")
    files = os.listdir(folder_path)
    string = ', '.join(files)
    print(string)
    string = string.split(".jpg")
    for i in range(len(string)):
        string[i] = string[i].replace(", ", "")


    # criar um quadro para conter a lista
    frame = tk.Frame(apgrt)
    frame.pack(side="left", fill="y")

    # criar uma barra de rolagem vertical
    scrollbar = tk.Scrollbar(frame, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    # conectar a lista à barra de rolagem
    lista = tk.Listbox(frame, yscrollcommand=scrollbar.set)
    for apgrt in string:
        lista.insert("end", apgrt)
    lista.pack(side="left", fill="y")
    scrollbar.config(command=lista.yview)

# Função que reconhece a pessoa 
def reconhecer():
    # Obtém o caminho para a área de trabalho do usuário atual
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    # Concatena o caminho da pasta "Fotos Data 'Face Safety'" na área de trabalho
    data_folder_path = os.path.join(desktop_path, "Fotos Data 'Face Safety'")

    # Cria um objeto PastaOrganizador
    sfr = PastaOrganizador()

    # Carrega as imagens codificadas de faces conhecidas
    sfr.load_encoding_images(data_folder_path)

    # Resto do código é igual ao anterior
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        ret, frame = cap.read()
        face_locations, face_names = sfr.detect_known_faces(frame)

        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        cv2.imshow("Aperte 'ESC' para sair do modo Scanner", frame)

        key = cv2.waitKey(1)

        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# Função que reconhece a pessoa dentro de uma pasta
class PastaOrganizador:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path):

        images_path = glob.glob(os.path.join(images_path, "*.*"))

        print("{} imagens foram encontradas.".format(len(images_path)))

        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)

            img_encoding = face_recognition.face_encodings(rgb_img)[0]


            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)
        print("Images encontrdas: ", self.known_face_names)

    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)

        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            face_names.append(name)

        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names


lobby()
