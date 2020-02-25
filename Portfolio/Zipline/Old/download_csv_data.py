{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from collections import OrderedDict\n",
    "import pytz\n",
    "\n",
    "# необходимые функции zipline\n",
    "from zipline.api import (order, record, symbol, set_benchmark, order_target_percent, get_open_orders, order_target, \n",
    "                        schedule_function, date_rules, time_rules, order_percent, symbols)\n",
    "\n",
    "# комиссии\n",
    "from zipline.finance import commission\n",
    "\n",
    "# выбор календаря по которому происходит торговля\n",
    "from trading_calendars.always_open import AlwaysOpenCalendar\n",
    "\n",
    "import zipline\n",
    "\n",
    "# графика\n",
    "import matplotlib.pyplot as plt\n",
    "from matplotlib import style\n",
    "\n",
    "# работа с временем\n",
    "from datetime import datetime\n",
    "\n",
    "# aинансовые данные\n",
    "from yahoofinancials import YahooFinancials\n",
    "\n",
    "# ignore warnings\n",
    "import warnings\n",
    "\n",
    "# отчёт\n",
    "import pyfolio as pf\n",
    "\n",
    "# import helper functions \n",
    "import qf_helper_functions as qf\n",
    "\n",
    "import pypfopt\n",
    "from pypfopt.efficient_frontier import EfficientFrontier\n",
    "from pypfopt import risk_models\n",
    "from pypfopt import expected_returns\n",
    "\n",
    "import pylab"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.style.use('seaborn')\n",
    "plt.rcParams['figure.figsize'] = [16, 9]\n",
    "plt.rcParams['figure.dpi'] = 200\n",
    "warnings.simplefilter(action='ignore', category=FutureWarning)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def download_csv_data(ticker, start_date, end_date, freq, path):\n",
    "    \n",
    "    yahoo_financials = YahooFinancials(ticker)\n",
    "\n",
    "    df = yahoo_financials.get_historical_price_data(start_date, end_date, freq)\n",
    "    df = pd.DataFrame(df[ticker]['prices']).drop(['date'], axis=1) \\\n",
    "            .rename(columns={'formatted_date':'date'}) \\\n",
    "            .loc[:, ['date','open','high','low','close','volume']] \\\n",
    "            .set_index('date')\n",
    "    df.index = pd.to_datetime(df.index)\n",
    "    df['dividend'] = 0\n",
    "    df['split'] = 1\n",
    "\n",
    "    # save data to csv for later ingestion\n",
    "    df.to_csv(path, header=True, index=True)\n",
    "\n",
    "    # plot the time series\n",
    "    df.close.plot(title='{} prices --- {}:{}'.format(ticker, start_date, end_date), color='green');"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
