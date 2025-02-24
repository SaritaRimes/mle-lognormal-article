from matplotlib.ticker import ScalarFormatter


class ScalarFormatterCustom(ScalarFormatter):
    def _set_format(self):
        self.format = '%1.1f'
