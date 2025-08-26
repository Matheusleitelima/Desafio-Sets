# 🚀 Desafio com `Sets` em Python

## 📌 Descrição
O objetivo deste desafio é praticar o uso de **conjuntos (`sets`)** em Python para organizar informações de funcionários de acordo com algumas condições específicas.

Você deverá criar um programa que gera **3 listas diferentes**, separando os funcionários conforme os critérios abaixo:

- **Lista 1** ➝ Funcionários que **têm carro** e **trabalham à noite**  
- **Lista 2** ➝ Funcionários que **têm carro** e **trabalham durante o dia**  
- **Lista 3** ➝ Funcionários que **não têm carro**

---

## 🛠️ Regras do Desafio
1. Usar **conjuntos (`set`)** para armazenar e manipular os dados.  
2. Criar as listas finais com base nas condições descritas.  
3. Exibir as três listas no final do programa.

---

## 📂 Estrutura esperada
O código deve seguir a seguinte lógica:
1. Criar conjuntos de funcionários que:
   - Trabalham **de dia**
   - Trabalham **à noite**
   - Possuem **carro**
   - Não possuem **carro**
2. Usar **operações de conjuntos** como `&` (interseção) e `-` (diferença) para gerar as listas.
3. Exibir as listas formatadas para melhor visualização.

---

## 💡 Exemplo de Entrada
Suponha os seguintes conjuntos:

```python
trabalham_dia = {"Ana", "Carlos", "Maria"}
trabalham_noite = {"João", "Paula", "Carla"}
tem_carro = {"Ana", "João", "Paula"}
nao_tem_carro = {"Carlos", "Maria", "Carla"}
```

---

## 📤 Saída Esperada
```text
Lista 1 (Funcionários com carro e trabalham à noite): {'João', 'Paula'}
Lista 2 (Funcionários com carro e trabalham durante o dia): {'Ana'}
Lista 3 (Funcionários que não têm carro): {'Carlos', 'Maria', 'Carla'}
```

---

## 🎯 Objetivo de Aprendizado
- Praticar **operações com `set`** em Python  
- Trabalhar com **interseção** e **diferença** de conjuntos  
- Organizar dados em estruturas de forma lógica e eficiente  

---

## ✅ Desafio Extra
- Permitir que o usuário cadastre os funcionários manualmente.  
- Exibir as listas em ordem alfabética.  
- Salvar as listas em um arquivo `.txt` ou `.csv`.

---
