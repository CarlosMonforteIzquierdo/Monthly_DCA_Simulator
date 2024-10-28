import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import io
import base64
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def set_data():
    if request.method == 'GET':
        return render_template('set_data.html')
    else:
        ticker = request.form.get('ticker')
        amount = request.form.get('amount')
        start_year = request.form.get('start_year')
        end_year = request.form.get('end_year')
        return redirect(url_for('calculateDCA', ticker=ticker, amount=int(amount), start_year=start_year, end_year=end_year))
        

@app.route('/monthlyDCA/<ticker>/<int:amount>/<int:start_year>/<int:end_year>')
def calculateDCA(ticker, amount, start_year,end_year):
    
    start_date = str(start_year)+'-01-01'
    end_date = str(end_year)+'-01-01'
    interval = '1M'
    
    # Obtiene los datos de yfinance
    data = yf.download(ticker, start=start_date, end=end_date)
    data = data.dropna()
    resampled_data = data.resample(interval).first()

    total_investment = 0
    total_shares = 0
    dca_log = []

    for date, row in resampled_data.iterrows():
        price = row['Adj Close']
        total_shares += amount / price
        total_investment += amount

        dca_log.append({
            'Date': date.strftime('%d/%m/%Y'),
            'Price': price,
            'Total Shares': total_shares,
            'Total Investment': total_investment,
            'Portfolio Value': total_shares * price
        })

    dca_df = pd.DataFrame(dca_log)
    final_portfolio_value = total_shares * data.iloc[-1]['Adj Close']
    total_profit = final_portfolio_value - total_investment

    #Retornar datos como JSON
    return render_template('graphic.html',
                           dates=dca_df['Date'].tolist(),
                           portfolio_values=dca_df['Portfolio Value'].tolist(),
                           invested_amounts=dca_df['Total Investment'].tolist(),
                           ticker=ticker,
                           total_investment=int(total_investment),
                           final_portfolio_value=int(final_portfolio_value),
                           total_profit=int(total_profit),
                           amount_per_month=int(amount))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)
