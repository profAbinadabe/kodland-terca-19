def summarization(text, num_sentences):

  # Separar o texto em frases
  sentences = sent_tokenize(text, language="portuguese")

  # Carregar os stopwords em português
  stop_words = set(stopwords.words('portuguese'))

  # Separar o texto em palavras
  words = word_tokenize(text, language="portuguese")

  # Limpar as palavras
  words = [word.lower() for word in words if word.isalpha()]
  words = [word for word in words if word not in stop_words]

  # Calcular a frequencia das palavras
  frequencia = FreqDist(words)

  # Calcular uma pontuação para cada frase
  ponto_sentenca = {}

  for i, sentence in enumerate(sentences):
    sentence_palavra = word_tokenize(sentence.lower(), language="portuguese")
    sentence_ponto = sum([frequencia[word] for word in sentence_palavra if word in frequencia])
    ponto_sentenca[i] = sentence_ponto

  # Ordenar as frases pela pontuacao
  ponto_sorte = sorted(ponto_sentenca.items(), key=lambda x: x[1], reverse=True)

  # Selecionar a quantidade de frases desejada
  selecao = ponto_sorte[:num_sentences]

  #Reordenar as frases selecionadas na ordem original do texto
  selecao = sorted(selecao)

  # Montamos o resumo final
  sumario = ' '.join([sentences[i] for i, _ in selecao])

  return sumario
