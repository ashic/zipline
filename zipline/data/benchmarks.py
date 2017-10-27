#
# Copyright 2013 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pandas_datareader.data as pd_reader


def get_benchmark_returns(symbol, first_date, last_date):
    """
    Get a Series of benchmark returns from Yahoo associated with `symbol`.
    Default is `GSPC`.

    Parameters
    ----------
    symbol : str
        Benchmark symbol for which we're getting the returns.
    first_date : pd.Timestamp
        First date for which we want to get data.
    last_date : pd.Timestamp
        Last date for which we want to get data.

    `first_date` is **not** included because we need the close from
    day N - 1 to compute the returns for day N.
    """
    data = pd_reader.DataReader(
        symbol,
        'yahoo',
        first_date,
        last_date
    )

    data = data['Adj Close']

    return data.sort_index().tz_localize('UTC').pct_change(1).iloc[1:]
