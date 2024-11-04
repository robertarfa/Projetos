import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
# Definindo a carteira de ações
carteira_yf = ['BBAS3.SA', 'SANB11.SA', 'AURE3.SA', 'TAEE11.SA', 'ITSA4.SA',
               'PETR4.SA', 'RENT3.SA', 'SUZB3.SA', 'VALE3.SA', 'WEGE3.SA']

# Carregando os dados da carteira
df = yf.download(carteira_yf, start="2022-08-01", end="2023-08-01")

# Passando os ativos para o multindex do df
cotacoes = df.stack(level=1)

# Resetando os índices e renomenado a coluna dos ativos
cotacoes = cotacoes.reset_index().rename(columns={'Ticker': 'Ativo'})

# Organizando o df
dataset = cotacoes[["Ativo", "Date", "Open", "High", "Low", "Close"]]
dataset.head()
dataset.info()


# del carteira_yf, df
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
# Configurações iniciais de fonte
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams["font.sans-serif"] = 'Verdana'


def plot_candlestick(df, ticker_column='Ativo', date_column='Date', open_column='Open', high_column='High', low_column='Low', close_column='Close'):
    """
    Plots candlestick chart from a DataFrame.

    Args:
        df: Pandas DataFrame containing the data.
        ticker_column: Name of the column containing the ticker symbol.
        date_column: Name of the column containing the dates.
        open_column: Name of the column containing the open prices.
        high_column: Name of the column containing the high prices.
        low_column: Name of the column containing the low prices.
        close_column: Name of the column containing the close prices.
    """

    # Ensure correct data types
    df[date_column] = pd.to_datetime(df[date_column])
    df = df.set_index(date_column)  # Set date as index for plotting


    for ticker in df[ticker_column].unique():
        df_ticker = df[df[ticker_column] == ticker]


        fig, ax = plt.subplots(figsize=(12, 6))

        # Plot Candlestick
        ax.vlines(df_ticker.index, df_ticker[low_column], df_ticker[high_column], color='black', linewidth=0.7)
        ax.bar(df_ticker.index, df_ticker[open_column] - df_ticker[close_column], width=1.0, bottom=df_ticker[close_column], color='green', align='center', alpha=0.95)

        ax.set_title(f'Candlestick Chart for {ticker}')
        ax.set_xlabel('Date')
        ax.set_ylabel('Price')

        # Customize the plot (important!)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        plt.grid(True, linestyle='--', alpha=0.7)

        plt.show()


plot_candlestick(dataset)

# Assuming your DataFrame is named 'df'
# Example usage:
# try: 
  # Load your data (replace 'your_data.csv' with your file)
# except FileNotFoundError:
#   print("Error: 'your_data.csv' not found. Please provide a valid file path.")
# except Exception as e:
#   print(f"An error occurred: {e}")