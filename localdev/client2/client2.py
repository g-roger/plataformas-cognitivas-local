import requests
import pandas as pd


if __name__ == "__main__":
    url = requests.get('https://us-central1-emf-teacher.cloudfunctions.net/function-aulas-getclient?qtde=1000')
    raw_data = url.json()
    data = pd.DataFrame.from_dict(raw_data)

    filtrados = data.sample(10)

    url = "http://localhost:8080/modelo02"
    headers = {'Content-Type': 'application/json'}
    conteudo = filtrados.to_json()

    response = requests.request("POST", url, headers=headers, data=conteudo)
    print("Resposta da API:")
    print(response.text.encode('utf8').decode())
    pass
