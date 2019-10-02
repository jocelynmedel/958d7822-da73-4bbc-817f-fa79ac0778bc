import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

class Cashflow(object):
#Clase para Cashflow

    def __init__(self, **kwargs):
        self.amount = kwargs['amount']
        self.t = kwargs['t']

    def present_value(self, interest_rate):
        pv = self.amount / ((1 + interest_rate) ** self.t)
        return pv

class InvestmentProject (object):
#Clase para investment project
    RISK_FREE_RATE = 0.08

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

        amount_l = []
        t_l = []
        for obj in self.cashflows:
            amount_l.append(obj.amount)
            t_l.append(obj.t)
        fig = plt.figure(1)
        plt.bar(np.arange(len(amount_l)), amount_l)
        plt.xticks(np.arange(len(t_l)), t_l)
        plt.title ('CashFlows Bar Chart')
        plt.xlabel ('t')
        plt.ylabel('Amount')
        if show:
            plt.show()
        return fig



    def net_present_value(self, interest_rate=None):
        """ Net Present Value
        Calculate the net-present value of a list of cashflows.
        :param interest_rate: represents the discount rate.
        :return: a number (currency) representing the net-present value.
        """
        if interest_rate is None:
            interest_rate = self.hurdle_rate
        npv = 0
        for i in self.cashflows:
            npv += i.present_value(interest_rate=interest_rate)
        return npv

    def equivalent_annuity(self, interest_rate=None):
        """ Equivalent Annuity
        Transform a set of cashflows into a constant payment.
        :param interest_rate: represents the interest-rate used with the annuity calculations.
        :return: a number (currency) representing the equivalent annuity.
        """
        if interest_rate is None:
            interest_rate = self.hurdle_rate
        a = (self.net_present_value(interest_rate)*interest_rate)
        b = 1- (1+interest_rate)**(-self.cashflow_max_position)
        c = a/b
        return c

    def describe(self):
        return {
            "irr": self.internal_return_rate,
            "hurdle-rate": self.hurdle_rate,
            "net-present-value": self.net_present_value(interest_rate=None),
            "equivalent-annuity": self.equivalent_annuity(interest_rate=None)
        }