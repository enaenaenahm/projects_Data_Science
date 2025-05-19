import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../ex03')))

from financial import get_financial_data

def test_total_revenue_msft():
    result = get_financial_data('MSFT', 'Total Revenue')
    assert isinstance(result, tuple)
    assert any("Total Revenue" in val or val.replace(",", "").isdigit() for val in result)

def test_return_type():
    result = get_financial_data('AAPL', 'Operating Income')
    assert isinstance(result, tuple)

def test_invalid_ticker():
    with pytest.raises(Exception):
        get_financial_data('INVALIDTICKER', 'Total Revenue')

def test_invalid_field():
    with pytest.raises(Exception):
        get_financial_data('MSFT', 'NotARealField')
