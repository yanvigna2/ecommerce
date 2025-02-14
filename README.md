# 📊 Análise de E-commerce Brasileiro - Olist

[![GitHub License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![MySQL Version](https://img.shields.io/badge/mysql-8.0%2B-orange)](https://www.mysql.com/)

## 📌 Tabela de Conteúdo
- [Objetivos](#-objetivos)
- [Stack Tecnológica](#-stack-tecnológica)
- [Principais Descobertas](#%EF%B8%8F-principais-descobertas)
- [Instalação](#-instalação)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Fluxo de Análise](#%EF%B8%8F-fluxo-de-análise)
- [Visualizações Chave](#-visualizações-chave)
- [Como Contribuir](#-como-contribuir)
- [Licença](#-licença)
- [Contato](#-contato)

## 🎯 Objetivos
1. Identificar padrões de compra geográficos
2. Analisar impacto do frete nas vendas
3. Otimizar mix de produtos por sazonalidade
4. Reduzir taxas de cancelamento em 20%
5. Criar dashboard estratégico para tomada de decisão

## 💻 Stack Tecnológica
| Ferramenta          | Uso Principal           | Badge                                                                 |
|---------------------|-------------------------|-----------------------------------------------------------------------|
| Python 3.10         | Análise e Visualização  | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python)     |
| MySQL 8.0           | Modelagem de Dados      | ![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql)        |
| Pandas              | Manipulação de Dados    | ![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas)     |
| Seaborn/Matplotlib  | Visualizações           | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?logo=image%2Fpng) |

## 🧩 Principais Descobertas
- **Geografia das Vendas:** 58% das vendas concentradas em SP e RJ
- **Impacto do Frete:** Produtos com frete > R$50 têm 30% mais cancelamentos
- **Métodos de Pagamento:** Cartão de crédito: 73%, Boleto: 19%, Outros: 8%
- **Top Categorias:** 
  ```python
  ['cama_mesa_banho', 'esporte_lazer', 'beleza_saude']

  
---

## 🛠️ Instalação

### Pré-requisitos
- Python 3.8+
- MySQL 8.0+
- Jupyter Notebook

### Passo a Passo
```bash
# 1. Clonar repositório
git clone https://github.com/seu_usuario/olist_ecommerce_analysis.git

# 2. Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Importar dados para MySQL
mysql -u root -p < sql/create_tables.sql

# 5. Executar pipeline de dados
python scripts/data_processing.py
```

### Seção 7: Estrutura do Projeto 
### O que fazer:
```olist_ecommerce_analysis/
├── data/
│ ├── raw/ # Dados brutos do Kaggle
│ ├── processed/ # Dados limpos (CSV/Parquet)
│ └── outputs/ # Gráficos e relatórios
│
├── notebooks/
│ ├── 01_etl.ipynb # Pipeline de limpeza
│ └── 02_analise.ipynb # Análise exploratória
│
├── scripts/
│ ├── database.py # Conexão com MySQL
│ └── analysis.py # Funções de análise
│
├── sql/
│ ├── ddl/ # Schemas do banco
│ └── queries/ # Consultas analíticas
│
└── docs/ # Documentação técnica
```

## 🔄 Fluxo de Análise

1. **Extração:** Dados brutos do Kaggle  
2. **Carga:** Importação para MySQL  
3. **Transformação:** Limpeza com Pandas  
4. **Análise:** Estatísticas e correlações  
5. **Visualização:** Gráficos com Seaborn  
6. **Deploy:** Relatório executivo em Excel  


---

### Seção 8: Licença e Contato

📧 Contato

**Yan Vigna** - [LinkedIn](https://www.linkedin.com/in/yan-vigna/) - pstlooc@gmail.com

**Repositório:** [github.com/seu-usuario/olist-analysis](https://github.com/yanvigna2/ecommerce)
