import pandas as pd
import matplotlib.pyplot as plt

# ================================
# 1. Carregar e preparar os dados
# ================================
df = pd.read_csv('spotify_history.csv')

# Converte o timestamp para datetime
df['ts'] = pd.to_datetime(df['ts'])

# Cria colunas auxiliares
df['date'] = df['ts'].dt.date
df['min_played'] = df['ms_played'] / 60000

# ================================
# 2. Gráfico Diário com Média Móvel
# ================================
# Soma os minutos por dia
daily_play = df.groupby('date')['min_played'].sum()

# Filtra para dias com mais de 1 minuto tocado
daily_play = daily_play[daily_play > 1]

# Média móvel de 7 dias
rolling_avg = daily_play.rolling(window=7).mean()

# Plot
plt.figure(figsize=(12, 6))
plt.plot(daily_play.index, daily_play.values, marker='o', linestyle='-', color='lightblue', alpha=0.5, label='Escuta diária')
plt.plot(rolling_avg.index, rolling_avg.values, color='red', linewidth=2, label='Média móvel (7 dias)')
plt.title('Tempo total de escuta por dia (com média móvel)')
plt.xlabel('Data')
plt.ylabel('Minutos ouvidos')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ================================
# 3. Gráfico Mensal
# ================================
# Reconfigura o índice para agrupar por mês
df.set_index('ts', inplace=True)

# Soma por mês
monthly_play = df['min_played'].resample('M').sum()

# Plot
plt.figure(figsize=(12, 6))
plt.plot(monthly_play.index, monthly_play.values, marker='o', color='green')
plt.title('Tempo total de escuta por mês')
plt.xlabel('Mês')
plt.ylabel('Minutos ouvidos')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

