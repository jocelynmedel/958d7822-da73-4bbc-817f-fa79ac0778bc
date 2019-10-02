import fire
import json 

from util import InvestmentProject

class Main(object):
    
    @staticmethod
    def describe_investment(filepath, hurdle_rate=None):
        investment_project = InvestmentProject.from_csv(filepath=filepath, hurdle_rate=hurdle_rate)
        description = investment_project.describe()
        print(json.dumps(description, indent=4))
        print('First, we have to understand this rates, the hurdle rate is the minimum rate that the someone expects to earn when investing')
        print('and the IRR, is the interest rate at which the net present value of all cash flows is zero. ')
        print('So, when the internal-rate of return is greater of equal than the hurdle rate, the investment is likely to be profit-making  ')
        print('')
        print('The net present value cant be negative, since is a sum of positive values,which are positive because the cashflow is a positive number divided by another positive number elevated to a positive time periods')
        print('Investments must have a positive net present value, so is worth more today than the costs')

    @staticmethod
    def plot_investment(filepath, save="", show=False):
        print('JMR')
        investment = InvestmentProject.from_csv(filepath=filepath)
        fig = investment.plot(show=show)
        if save:
            fig.savefig("pic.png")
        return

if __name__ == "__main__":
    fire.Fire(Main)
