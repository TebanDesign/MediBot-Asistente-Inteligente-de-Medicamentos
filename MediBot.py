import json


def guardar_json(datos, filename):
    """Creación de función para guardar
    diccionario de conocimiento en formato json"""
    with open(filename, "w") as archivo:
        json.dump(datos, archivo, indent=4)


biblioteca = {
    "intents": [
        # Saludos
        {
            "tag": "saludo",
            "patterns": ["Hola", "¿Cómo estás?", "Buenos días", "¡Hola!", "¡Qué tal!"],
            "responses": [
                "¡Hola! ¿En qué puedo ayudarte hoy?",
                "¡Hola! ¿Cómo puedo asistirte con tu consulta sobre medicamentos?",
            ],
        },
        # Despedidas
        {
            "tag": "despedida",
            "patterns": [
                "Adiós",
                "Hasta luego",
                "Nos vemos",
                "Hasta pronto",
                "Hasta luego, gracias",
            ],
            "responses": [
                "¡Hasta luego! Que tengas un excelente día.",
                "¡Adiós! Si necesitas más información, aquí estaré.",
            ],
        },
        # Información de medicamentos
        {
            "tag": "informacion_medicamento_paracetamol",
            "patterns": [
                "¿Qué es el medicamento Paracetamol?",
                "¿Para qué sirve el Paracetamol?",
                "Cuéntame sobre Paracetamol",
                "¿Qué hace el Paracetamol?",
            ],
            "responses": [
                "El Paracetamol es un analgésico y antipirético comúnmente usado para aliviar el dolor leve a moderado y reducir la fiebre. Es efectivo para dolores de cabeza, musculares y de muelas.",
                "Paracetamol es utilizado para aliviar dolores leves y reducir la fiebre. No se recomienda exceder la dosis diaria de 4 gramos, ya que puede causar daño hepático.",
            ],
        },
        {
            "tag": "informacion_medicamento_mejoral",
            "patterns": [
                "¿Qué es el medicamento Mejoral?",
                "¿Para qué sirve el Mejoral?",
                "Cuéntame sobre Mejoral",
                "¿Qué hace el Mejoral?",
            ],
            "responses": [
                "Mejoral es un medicamento que combina aspirina y paracetamol, utilizado principalmente para aliviar dolores como dolores de cabeza, musculares o articulares. También ayuda a reducir la fiebre.",
                "Mejoral es eficaz para aliviar dolores leves y moderados, además de reducir la fiebre. Es una opción común para aliviar dolores como los de cabeza y musculares.",
            ],
        },
        {
            "tag": "informacion_medicamento_alkaseltzer",
            "patterns": [
                "¿Qué es el medicamento Alka-Seltzer?",
                "¿Para qué sirve Alka-Seltzer?",
                "Cuéntame sobre Alka-Seltzer",
                "¿Qué hace el Alka-Seltzer?",
            ],
            "responses": [
                "Alka-Seltzer es un medicamento efervescente utilizado para aliviar la acidez estomacal, indigestión y malestar estomacal. También es eficaz para reducir el dolor causado por estas molestias.",
                "Alka-Seltzer se utiliza comúnmente para aliviar problemas digestivos, como la acidez estomacal o la indigestión, proporcionando alivio rápido.",
            ],
        },
        {
            "tag": "informacion_medicamento_tabcin",
            "patterns": [
                "¿Qué es el medicamento Tabcin?",
                "¿Para qué sirve el Tabcin?",
                "Cuéntame sobre Tabcin",
                "¿Qué hace el Tabcin?",
            ],
            "responses": [
                "Tabcin es un medicamento utilizado para aliviar los síntomas del resfriado, como la congestión nasal, la tos y el malestar general. Contiene un antihistamínico y descongestionante.",
                "Tabcin es eficaz para tratar los resfriados comunes, ayudando a reducir la congestión nasal y otros síntomas molestos relacionados con resfriados.",
            ],
        },
        {
            "tag": "informacion_medicamento_vickvaporub",
            "patterns": [
                "¿Qué es el medicamento Vick VapoRub?",
                "¿Para qué sirve el Vick VapoRub?",
                "Cuéntame sobre Vick VapoRub",
                "¿Qué hace el Vick VapoRub?",
            ],
            "responses": [
                "Vick VapoRub es una pomada tópica utilizada para aliviar la congestión nasal, la tos y los dolores musculares. Contiene mentol, alcanfor y aceite de eucalipto.",
                "Vick VapoRub es muy útil para aliviar la congestión respiratoria y los dolores musculares. Se aplica directamente sobre el pecho o la garganta.",
            ],
        },
        {
            "tag": "informacion_medicamento_intestinomicina",
            "patterns": [
                "¿Qué es el medicamento Intestinomicina?",
                "¿Para qué sirve la Intestinomicina?",
                "Cuéntame sobre Intestinomicina",
                "¿Qué hace la Intestinomicina?",
            ],
            "responses": [
                "Intestinomicina es un medicamento utilizado para tratar infecciones intestinales, como la diarrea infecciosa o bacteriana. Actúa eliminando bacterias dañinas en el intestino.",
                "Intestinomicina es eficaz para el tratamiento de infecciones intestinales y problemas digestivos causados por bacterias, ayudando a restaurar el equilibrio intestinal.",
            ],
        },
        {
            "tag": "informacion_medicamento_panadol",
            "patterns": [
                "¿Qué es el medicamento Panadol?",
                "¿Para qué sirve el Panadol?",
                "Cuéntame sobre Panadol",
                "¿Qué hace el Panadol?",
            ],
            "responses": [
                "Panadol es un analgésico utilizado para aliviar dolores leves a moderados, como dolores de cabeza, dolor muscular, dolor de muelas, o fiebre.",
                "Panadol es eficaz para el alivio rápido de dolores comunes y fiebre, al igual que el paracetamol, pero es una de las marcas más reconocidas.",
            ],
        },
        {
            "tag": "informacion_medicamento_salandrews",
            "patterns": [
                "¿Qué es el medicamento Sal Andrews?",
                "¿Para qué sirve la Sal Andrews?",
                "Cuéntame sobre Sal Andrews",
                "¿Qué hace la Sal Andrews?",
            ],
            "responses": [
                "Sal Andrews es un medicamento efervescente utilizado para tratar la acidez estomacal y la indigestión, aliviando la sensación de ardor en el estómago.",
                "La Sal Andrews ayuda a neutralizar el ácido estomacal, proporcionando alivio rápido para las molestias causadas por la acidez o la indigestión.",
            ],
        },
        {
            "tag": "informacion_medicamento_pildorin",
            "patterns": [
                "¿Qué es el medicamento Pildorín?",
                "¿Para qué sirve el Pildorín?",
                "Cuéntame sobre Pildorín",
                "¿Qué hace el Pildorín?",
            ],
            "responses": [
                "Pildorín es un anticonceptivo oral utilizado para prevenir embarazos no deseados. Contiene hormonas que controlan el ciclo menstrual y previenen la ovulación.",
                "Pildorín es una opción de pastillas anticonceptivas que ayuda a regular el ciclo menstrual y evita la fertilización.",
            ],
        },
        {
            "tag": "informacion_medicamento_cafiaspirina",
            "patterns": [
                "¿Qué es el medicamento Cafiaspirina?",
                "¿Para qué sirve la Cafiaspirina?",
                "Cuéntame sobre Cafiaspirina",
                "¿Qué hace la Cafiaspirina?",
            ],
            "responses": [
                "Cafiaspirina es un medicamento combinado de cafeína y aspirina, utilizado para aliviar dolores de cabeza, migrañas y dolores musculares.",
                "Cafiaspirina actúa combatiendo el dolor de cabeza y mejorando la circulación sanguínea, gracias a la acción conjunta de la cafeína y la aspirina.",
            ],
        },
        {
            "tag": "informacion_medicamento_atamel",
            "patterns": [
                "¿Qué es el medicamento Atamel?",
                "¿Para qué sirve el Atamel?",
                "Cuéntame sobre Atamel",
                "¿Qué hace el Atamel?",
            ],
            "responses": [
                "Atamel es un medicamento que contiene paracetamol, utilizado para aliviar dolores de cabeza, fiebre y dolores musculares.",
                "Atamel es similar al Paracetamol, con propiedades analgésicas y antipiréticas, efectivo para reducir dolores y fiebre.",
            ],
        },
        {
            "tag": "informacion_medicamento_dramamine",
            "patterns": [
                "¿Qué es el medicamento Dramamine?",
                "¿Para qué sirve el Dramamine?",
                "Cuéntame sobre Dramamine",
                "¿Qué hace el Dramamine?",
            ],
            "responses": [
                "Dramamine, también conocido como 'El Drama', es un medicamento utilizado para prevenir y tratar los mareos, náuseas y vómitos causados por el movimiento, como en los viajes en automóvil, barco o avión.",
                "Dramamine es un antihistamínico utilizado para combatir los síntomas del mareo y las náuseas, especialmente en viajes largos o en situaciones de mareo por movimiento.",
            ],
        },
        {
            "tag": "informacion_medicamento_bicarbonato",
            "patterns": [
                "¿Qué es el medicamento Bicarbonato?",
                "¿Para qué sirve el Bicarbonato?",
                "Cuéntame sobre Bicarbonato",
                "¿Qué hace el Bicarbonato?",
            ],
            "responses": [
                "El Bicarbonato, conocido también como 'El Bicarbo', es un medicamento utilizado para aliviar la acidez estomacal y la indigestión. Neutraliza el exceso de ácido en el estómago.",
                "El Bicarbonato se usa comúnmente para reducir la acidez estomacal y aliviar los síntomas de la indigestión. También puede ser útil en algunos problemas de acidez gástrica.",
            ],
        },
        {
            "tag": "informacion_medicamento_dolex",
            "patterns": [
                "¿Qué es el medicamento Dolex?",
                "¿Para qué sirve el Dolex?",
                "Cuéntame sobre Dolex",
                "¿Qué hace el Dolex?",
            ],
            "responses": [
                "Dolex es un analgésico utilizado para aliviar dolores de cabeza, dolores musculares y dolores leves a moderados. Contiene paracetamol como principio activo.",
                "Dolex es comúnmente usado para tratar dolores de cabeza, musculares y otros dolores menores, ofreciendo alivio rápido y efectivo.",
            ],
        },
        {
            "tag": "informacion_medicamento_lemisol",
            "patterns": [
                "¿Qué es el medicamento Lemisol?",
                "¿Para qué sirve Lemisol?",
                "Cuéntame sobre Lemisol",
                "¿Qué hace Lemisol?",
            ],
            "responses": [
                "Lemisol, o 'El Lemi', es un medicamento utilizado como antiséptico para tratar heridas y quemaduras leves. Se aplica tópicamente para prevenir infecciones en la piel.",
                "Lemisol es un antiséptico eficaz para limpiar y desinfectar heridas, cortaduras y quemaduras menores, ayudando a prevenir infecciones.",
            ],
        },
        {
            "tag": "informacion_medicamento_tachipirin",
            "patterns": [
                "¿Qué es el medicamento Tachipirín?",
                "¿Para qué sirve el Tachipirín?",
                "Cuéntame sobre Tachipirín",
                "¿Qué hace el Tachipirín?",
            ],
            "responses": [
                "Tachipirín es un medicamento utilizado para tratar la fiebre en niños. Contiene paracetamol, lo que ayuda a reducir la fiebre y aliviar dolores leves a moderados.",
                "Tachipirín es un medicamento especialmente formulado para niños, utilizado para bajar la fiebre y aliviar dolores causados por resfriados o infecciones comunes.",
            ],
        },
        {
            "tag": "informacion_medicamento_alkad",
            "patterns": [
                "¿Qué es el medicamento Alka-D?",
                "¿Para qué sirve el Alka-D?",
                "Cuéntame sobre Alka-D",
                "¿Qué hace el Alka-D?",
            ],
            "responses": [
                "Alka-D es un medicamento utilizado para aliviar la acidez estomacal y el malestar causado por la indigestión. Actúa neutralizando el exceso de ácido en el estómago.",
                "Alka-D se usa para tratar problemas digestivos como la acidez y el malestar estomacal, proporcionando alivio rápido y efectivo.",
            ],
        },
        {
            "tag": "informacion_medicamento_enteroguanil",
            "patterns": [
                "¿Qué es el medicamento Enteroguanil?",
                "¿Para qué sirve Enteroguanil?",
                "Cuéntame sobre Enteroguanil",
                "¿Qué hace Enteroguanil?",
            ],
            "responses": [
                "Enteroguanil, o 'La Guanil', es un medicamento utilizado para tratar la diarrea. Ayuda a reducir la frecuencia y la intensidad de las evacuaciones intestinales.",
                "Enteroguanil es eficaz en el tratamiento de la diarrea aguda, especialmente en casos causados por infecciones intestinales, restaurando el equilibrio digestivo.",
            ],
        },
        {
            "tag": "informacion_medicamento_dolofin",
            "patterns": [
                "¿Qué es el medicamento Dolofin?",
                "¿Para qué sirve Dolofin?",
                "Cuéntame sobre Dolofin",
                "¿Qué hace Dolofin?",
            ],
            "responses": [
                "Dolofin, o 'El Dolo', es un medicamento utilizado para aliviar dolores leves a moderados, como dolores musculares y de cabeza. Contiene paracetamol como principio activo.",
                "Dolofin es utilizado para aliviar dolores como los de cabeza, musculares y otras molestias menores, proporcionando un alivio rápido y efectivo.",
            ],
        },
        {
            "tag": "informacion_medicamento_neosaldina",
            "patterns": [
                "¿Qué es el medicamento Neosaldina?",
                "¿Para qué sirve Neosaldina?",
                "Cuéntame sobre Neosaldina",
                "¿Qué hace Neosaldina?",
            ],
            "responses": [
                "Neosaldina, o 'La Neo', es un medicamento utilizado para tratar migrañas y dolores de cabeza intensos. Contiene principios activos que ayudan a aliviar el dolor y reducir la inflamación.",
                "Neosaldina es muy eficaz para aliviar las migrañas y dolores de cabeza severos, proporcionando un alivio rápido y eficaz.",
            ],
        },
        {
            "tag": "informacion_medicamento_amoxil",
            "patterns": [
                "¿Qué es el medicamento Amoxil?",
                "¿Para qué sirve Amoxil?",
                "Cuéntame sobre Amoxil",
                "¿Qué hace Amoxil?",
            ],
            "responses": [
                "Amoxil, o 'La Amoxilina', es un antibiótico utilizado para tratar infecciones bacterianas, como infecciones respiratorias, del tracto urinario y otras infecciones comunes.",
                "Amoxil es un medicamento antibiótico que combate infecciones bacterianas al interferir con la producción de las paredes celulares de las bacterias, ayudando a eliminarlas.",
            ],
        },
        {
            "tag": "norespuesta",
            "patterns": [
                "",
                "no entiendo",
                "no sé qué decir",
                "no tengo una respuesta",
                "no entiendo la pregunta",
            ],
            "responses": [
                "Lo siento, no pude entender tu pregunta. ¿Podrías reformularla?",
                "No estoy seguro de cómo responder eso. ¿Podrías ser más específico?",
                "No reconozco esa solicitud. Si necesitas información sobre medicamentos, por favor, pregúntame de nuevo.",
            ],
        },
    ]
}

# Guardado de diccionario de conocimiento en formato json.
guardar_json(biblioteca, "intents.json")
biblioteca


import nltk
import json
import random
import numpy as np
from nltk.stem import PorterStemmer
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from tensorflow.keras.models import Sequential  # type: ignore
from tensorflow.keras.layers import Dense  # type: ignore
from tensorflow.keras.optimizers import Adam  # type: ignore


# Cargar el archivo JSON
with open("intents.json") as file:
    intents = json.load(file)

    # Inicializar el stemmer y el encoder
stemmer = PorterStemmer()
encoder = LabelEncoder()  # Similar al Integer Encoding

# Preparar los datos
patterns = []  # Base de conocimientos por cada intención
responses = []  # Respuesta de la intención
tags = []  # Intents

# Llenar las listas con los datos del JSON
for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        responses.append(intent["responses"])
        tags.append(intent["tag"])  # Intent

        # Tokenización y Stemming


def tokenize_and_stem(sentence):
    words = nltk.word_tokenize(sentence)
    words = [stemmer.stem(w.lower()) for w in words if w.isalnum()]
    return words


# Crear el Bag of Words
all_words = []
for pattern in patterns:
    words = tokenize_and_stem(pattern)
    all_words.extend(words)

all_words = sorted(list(set(all_words)))

# Crear el Bag of Words (BoW)
vectorizer = CountVectorizer(vocabulary=all_words)
X_train = vectorizer.transform(patterns).toarray()

# Codificar las etiquetas
y_train = encoder.fit_transform(tags)

# Crear la red neuronal
model = Sequential()
model.add(Dense(128, input_shape=(X_train.shape[1],), activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(len(set(tags)), activation="softmax"))

# Compilar el modelo
model.compile(
    loss="sparse_categorical_crossentropy", optimizer=Adam(), metrics=["accuracy"]
)

# Entrenar el modelo
model.fit(X_train, y_train, epochs=200, batch_size=5, verbose=1)


# Función para obtener la respuesta más probable
def chatbot_response(text):
    # Preprocesar el texto de entrada
    text_words = tokenize_and_stem(text)
    bow = np.zeros(len(all_words))

    for word in text_words:
        if word in all_words:
            bow[all_words.index(word)] = 1

    # Predecir la categoría
    prediction = model.predict(np.array([bow]))[0]
    tag = encoder.inverse_transform([np.argmax(prediction)])

    # Buscar una respuesta dentro de la categoría
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

        # Probar el chatbot


print("¡Hola! Soy MediBot. Escribe 'salir' para terminar.")
while True:
    user_input = input("Tú: ")
    if user_input.lower() == "salir":
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")