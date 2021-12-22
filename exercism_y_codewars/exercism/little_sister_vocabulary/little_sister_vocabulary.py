#Este metodo es muy sencillo,devuelve una palabra con el string "un" delante 
def add_prefix_un(word):
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """

    return "un" + word

lista = ['en','close','joy','lighten']

#Este metodo hace lo mismo que el anterior pero con todos los elementos de un array donde el primer elemento sera el prefijo 
def make_word_groups(vocab_words):
    #Aquí guardaremos todo,lo inicializamos en el "en" para ahorrarnos work 
    estring=vocab_words[0] 
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
     #Recirremos la lista proporcionada para todo el rato sumar en+palabra y guardarlo en estring,respetando el patron que pide el ejercicio
    for i in range (1,len(vocab_words)):
        estring+= " :: " +vocab_words[0] + vocab_words[i] 

    #Lo devolvemos
    return estring

#print(make_word_groups(lista))

#Este metodo reemplaza el string ness y sustituye la ultima i por y
def remove_suffix_ness(word):
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """
    #Lo del ness e smuy fácil,simplemente utilizamos un replace
    word = word.replace("ness","")

    #Si la ultima letra de la palabra reemplazada es i
    if(word[-1:] =="i"):
        #Pasamos la palabra a una lista donde cada celda es una letra
        lista=list(word)
        #Y la ultima celda donde hay una i ponemos una y
        lista[-1:]="y"
        #Lo unimos en una palabra con un join
        word="".join(lista)
    #Devolvemos la palabra ya modificada
    return word

#print(remove_suffix_ness("heaviness"))

#Este metodo le quiere devolver un string y sumarle en,ya que transforma de verlo a nombre DE UNA POSICION CONCRETA
def noun_to_verb(sentence, index):
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    #A la frase le quitamos el punto si hay por que estorba
    sentence=sentence.replace(".","")
    #Distribuimos las palabras en una lista con split
    lista = sentence.split(" ")

    #Devolvemos la palabra de la posición que pidio el usuario sumandole el en
    return lista[index] +"en"


#print(noun_to_verb("I need to make that bright.",-1))
#print(noun_to_verb('It got dark as the sun set.', 2))