import matplotlib.pyplot as plt
import seaborn as sns

# Superclass for Literally Everything
class Strategy:
    def __init__(self, title: str, net_premium: float):
        self.title = title
        self.net_premium = net_premium
        self.premium_type = 'credit' if net_premium > 0 else 'debit'

    def _show_plot(self, payoff: list[tuple[float, float]]):
        xs, ys = zip(*payoff)

        # Setting Seaborn Globals
        sns.set_theme(style='darkgrid')
        plt.axhline(0, color='black')

        # Plotting Payoff and Profit
        sns.lineplot(
            x=xs,
            y=ys,
            color='green',
            linestyle='--',
            label=f'Payoff (before {self.premium_type})',
            linewidth=2.5
        )
        sns.lineplot(
            x=xs,
            y=[y + self.net_premium for y in ys],
            color='green',
            linestyle='-',
            label=f'Profit (after {self.premium_type})',
            linewidth=2.5
        )
        plt.title(self.title)
        plt.ylabel('P&L')
        plt.show()

    def plot_delta_exposure(self):
        pass

    def plot_gamma_exposure(self):
        pass

    def plot_vega_exposure(self):
        pass

    def plot_theta_exposure(self):
        pass
