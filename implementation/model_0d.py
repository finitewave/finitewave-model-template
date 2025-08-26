from model_template import ops


class Stimulation:
    def __init__(self, t_start: float, t_end: float, duration: float, amplitude: float):
        self.t_start = t_start
        self.t_end = t_end
        self.duration = duration
        self.amplitude = amplitude

    def stim(self):
        pass


class Model0D:
    def __init__(self, dt: float, stimulation: Stimulation):
        self.dt = dt
        self.stimulation = stimulation
        self.variables = None
        self.parameters = None

    def step(self):
        pass

    def run(self, t_max: float):
        pass