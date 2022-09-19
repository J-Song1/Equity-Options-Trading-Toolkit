import matplotlib.pyplot as plt
import seaborn as sns

# Superclass for Literally Everything
class Strategy:
    def __init__(self, title: str, net_premium: float):
        self.title = title
        self.net_premium = net_premium
        self.premium_type = 'credit' if net_premium > 0 else 'debit'

    def _show_plot(self, payoff: list[tuple[float, float]], save_path='tmp.jpg'):
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
        plt.savefig(save_path)
        plt.clf()
        #plt.show()
        return save_path

    _ERROR_MSG = "is a virtual method in class Strategy"

    def get_price(self):
        raise NotImplementedError(f"get_price {self._ERROR_MSG}")

    def get_delta(self):
        raise NotImplementedError(f"get_net_delta_exposure {self._ERROR_MSG}")

    def get_gamma(self):
        raise NotImplementedError(f"get_net_gamma_exposure {self._ERROR_MSG}")

    def get_theta(self):
        raise NotImplementedError(f"get_net_theta_exposure {self._ERROR_MSG}")

    def get_vega(self):
        raise NotImplementedError(f"get_net_vega_exposure {self._ERROR_MSG}")

    def get_rho(self):
        raise NotImplementedError(f"get_net_rho_exposure {self._ERROR_MSG}")
