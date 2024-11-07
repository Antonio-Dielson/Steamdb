# Extração de Dados de Promoções da SteamDB

Este projeto realiza a extração de dados da página de promoções do SteamDB para armazenamento e análise posterior. Utilizamos as bibliotecas **Selenium** e **BeautifulSoup** para capturar e manipular o conteúdo da página, além da biblioteca **CSV** para salvar os dados em formato tabular.

## URL Utilizado
A URL de origem dos dados é:
[https://steamdb.info/sales/](https://steamdb.info/sales/)

## Bibliotecas Necessárias
As bibliotecas usadas no projeto são:
- **Selenium**: Para automação do navegador e carregamento da página dinâmica.
- **BeautifulSoup**: Para análise e extração de dados da página HTML.
- **CSV**: Para salvar os dados extraídos em um arquivo CSV.
- **Padas**: Analise e transformações dos dados
- **Time**: Definir tempo de execução do navegador

## Transformações e Processamento dos Dados
1. **Extração dos dados brutos**: Extraímos os títulos das colunas e os valores de cada linha da tabela de promoções.
2. **Transformação e limpeza**: Os valores são extraídos e limpos para remoção de espaços desnecessários e uniformização de formato.
3. **Armazenamento em CSV**: Os dados são salvos no arquivo `steam_dados.csv`, podendo ser carregados em ferramentas de análise.

## Integração com Google BigQuery e Google Sheets
Para análises e visualizações adicionais, os dados foram carregados no **Google BigQuery** via csv e posteriormente conectados no **Google Sheets**:
- **Google BigQuery**: Permite consultas SQL para análises mais complexas dos dados.
- **Google Sheets**: Permite compartilhamento e visualização dos dados em uma interface acessível.

### Link de Compartilhamento do Google Sheets
[https://docs.google.com/spreadsheets/d/15pUEI3e0jqh1sy1GXUKyyEl_KYXWfYxyY_s2dIO-zQk/edit?gid=1569104892#gid=1569104892](https://docs.google.com/spreadsheets/d/15pUEI3e0jqh1sy1GXUKyyEl_KYXWfYxyY_s2dIO-zQk/edit?gid=1569104892#gid=1569104892)

## Executando o Script
Para executar o script de extração, você precisará do driver do Chrome e das bibliotecas instaladas. Execute o script Python e o arquivo `steam_dados.csv` será gerado com os dados extraídos.

---
