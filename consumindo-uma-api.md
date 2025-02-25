# 📌 Função Simples para Consultar CEP usando API do ViaCEP

Esta função Python consome a API pública do **ViaCEP** para buscar informações de um CEP fornecido.

## 📜 **Código:**
```python
import requests

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        return resposta.json()  # Retorna os dados em formato de dicionário
    else:
        return {"erro": "CEP inválido ou não encontrado"}

# Exemplo de uso
cep_info = buscar_cep("01001000")  # CEP válido de São Paulo
print(cep_info)
```

---

## 🔍 **Explicação do Código:**

1. **`requests.get(url)`** → Faz uma requisição HTTP para a API do ViaCEP.
2. **Verifica `status_code == 200`** → Se a resposta for bem-sucedida, os dados são retornados como um dicionário.
3. **Retorno JSON** → Caso o CEP seja encontrado, os dados são retornados em formato de JSON.
4. **Caso de erro** → Se a requisição falhar, retorna um dicionário com uma mensagem de erro.

---

## 📝 **Exemplo de Saída:**

Se o CEP for **"01001000"**, a API pode retornar o seguinte JSON:
```json
{
    "cep": "01001-000",
    "logradouro": "Praça da Sé",
    "complemento": "lado ímpar",
    "bairro": "Sé",
    "localidade": "São Paulo",
    "uf": "SP",
    "ibge": "3550308",
    "gia": "1004",
    "ddd": "11",
    "siafi": "7107"
}
```

---

## 🚀 **Benefícios:**
✅ Código simples e direto.  
✅ Fácil de entender para iniciantes.  
✅ Usa a API pública do ViaCEP, sem necessidade de autenticação.  

