
class CycleModel:
    def __init__(self, p_initial, t_initial, ratio, cutoff, v_cylinder):
        self.units = self.Units()
        self.air = self.Air()  # the working fluid
        self.air.set(P=p_initial, T=t_initial)  # initial state
        self.p_initial = p_initial
        self.t_initial = t_initial
        self.ratio = ratio  # compression ratio V_BDC/V_TDC
        self.cutoff = cutoff  # cutoff ratio
        self.v_cylinder = v_cylinder
        self.calculate_states()

    def calculate_states(self):
        # Calculate state 1
        self.state1 = self.air.set(P=self.p_initial, T=self.t_initial)
        # State 2: Isoentropic compression to state 2
        self.state2 = self.air.set(v=self.state1.v / self.ratio, s=self.state1.s)
        # State 3: Isobaric heat addition
        self.state3 = self.air.set(P=self.state2.P, v=self.state2.v * self.cutoff)
        # State 4: Isoentropic expansion to state 4
        self.state4 = self.air.set(v=self.state1.v, s=self.state3.s)

    class Units:
        def __init__(self):
            self.SI = True

    class Air:
        def __init__(self):
            self.properties = {}
        
        def set(self, **kwargs):
            for key, value in kwargs.items():
                self.properties[key] = value
            return self.properties

class CycleController:
    def __init__(self, model=None):
        self.model = CycleModel(p_initial=1.0, t_initial=300, ratio=8.0, cutoff=1.5, v_cylinder=0.1) if model is None else model

    def calculate_cycle(self):
        self.model.calculate_states()
        # Additional calculations for work and efficiency can be added here

class CycleView:
    def display_states(self, model):
        for i, state in enumerate(['State1', 'State2', 'State3', 'State4'], start=1):
            print(f'State {i}:', getattr(model, state))

# Main execution
if __name__ == "__main__":
    cycle_model = CycleModel(p_initial=101325, t_initial=300, ratio=8, cutoff=2, v_cylinder=0.01)
    cycle_controller = CycleController(model=cycle_model)
    cycle_view = CycleView()
    cycle_view.display_states(cycle_model)
