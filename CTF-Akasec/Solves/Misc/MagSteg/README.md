Para solucionar este desafio ridiculo ->

1. Abrir o .wav no audacity, e entrar no modo ESPECTOGRAMA, no fim do audio tem algumas letras

2. Dar o seguinte comando

```bash
steghid --extract -sf [audio.wav]
```

Com a senha sendo as letras adquiridas la

3. Pegar o arquivo adquirido e inverter o hex de cada linha dele

4. Pegar o novo audio e colocar em um WAV2PNG