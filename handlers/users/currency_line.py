import pandas as pd
from loader import dp
import plotly.graph_objects as go
from datetime import datetime, date, time
from aiogram import types
import sqlite3
from kaleido.scopes.plotly import PlotlyScope


@dp.message_handler(text='Динамика курса')
async def command_currency(message: types.Message):
  
  scope = PlotlyScope(
    plotlyjs="https://cdn.plot.ly/plotly-latest.min.js",
  )
  
  try:
    db = sqlite3.connect('bot_data.db')
    cursor = db.cursor()
    query = f'SELECT * FROM currency'
    df = pd.read_sql(query, db)
    cursor.close()
    df = df.dropna()
    fig = go.Figure()
    fig.add_trace(go.Scatter(
      x=df['date'],
      y=df['gold_num'],
      mode='lines+markers',
      name='Курс ₸ на золотой короне',
    )) 
    fig.add_trace(go.Scatter(
      x=df['date'],
      y=df['cash_num'],
      mode='lines+markers',
      name='Среднее в обменниках Алматы',      
    )) 
    
    fig.update_layout(
      title='Курс ₸',
      title_font_color='white',
      font_color="white",
      xaxis=dict(
        showline=True,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',  
      ),
      yaxis=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
       ),
      legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
      ),
      xaxis_title='Дата и время',
      yaxis_title='Цена за ₽',
      xaxis_color = 'white',
      yaxis_color = 'white',
      autosize=False,
      plot_bgcolor='#093145',
      paper_bgcolor='#093145',

      )
    

    with open("line.png", "wb") as f:
      f.write(scope.transform(fig, format="png"))
  except sqlite3.Error as error:
    print('Ошибка', error)
  finally:
    if db:
      db.close()
  photo = types.InputFile('line.png')
  await dp.bot.send_photo(chat_id=message.chat.id, photo=photo)