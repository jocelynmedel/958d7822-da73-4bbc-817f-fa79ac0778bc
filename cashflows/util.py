import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Flow(object):
#Clase para Cashflow

    def __init__(self, **kwargs):
        self.amount = kwargs['amount']
        self.t = kwargs['t']

    def present_value(self, interest_rate):
        pv = self.amount / ((1 + interest_rate) ** self.t)
        return pv

class InvestmentProject (object):
#Clase para investment project

    def __init__(self, cashflows, hurdle_rate=RISK_FREE_RATE):
        cashflows_positions = {str(flow.t): flow for flow in cashflows}
        self.cashflow_max_position = max((flow.t for flow in cashflows))
        self.cashflows = []
        for t in range(self.cashflow_max_position + 1):
            self.cashflows.append(cashflows_positions.get(str(t), Cashflow(t=t, amount=0)))
        self.hurdle_rate = hurdle_rate if hurdle_rate else InvestmentProject.RISK_FREE_RATE

    @staticmethod
    def from_csv(filepath, hurdle_rate=RISK_FREE_RATE):
        cashflows = [Cashflow(**row) for row in pd.read_csv(filepath).T.to_dict().values()]
        return InvestmentProject(cashflows=cashflows, hurdle_rate=hurdle_rate)

    @property
    def internal_return_rate(self):
        return np.irr([flow.amount for flow in self.cashflows])

    def plot(self, show=False):
        """Plot Cashflows
        The `plot` function creates a bar plot (fig) where x=t and y=amount.
        :param show: boolean that represents whether to run `plt.show()` or not.
        :return: matplotlib figure object.
        """
        # TODO: implement plot method
        raise NotImplementedError


    def net_present_value(self, interest_rate=None):
        """ Net Present Value
        Calculate the net-present value of a list of cashflows.
        :param interest_rate: represents the discount rate.
        :return: a number (currency) representing the net-present value.
        """
        # TODO: implement net_present_value method
        raise NotImplementedError

    def equivalent_annuity(self, interest_rate=None):
        """ Equivalent Annuity
        Transform a set of cashflows into a constant payment.
        :param interest_rate: represents the interest-rate used with the annuity calculations.
        :return: a number (currency) representing the equivalent annuity.
        """
        # TODO: implement equivalent_annuity methdo
        raise NotImplementedError
