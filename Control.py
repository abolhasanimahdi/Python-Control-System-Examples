class ControlClass:
    def __init__(self, Ts, Kp, Ti):
        self.Ts = Ts
        self.Kp = Kp
        self.Ti = Ti

    def Model(self, yk, uk):
        # Model Parameters
        K = 3
        T = 4
        a = -1/T
        b = K/T
        Ts = self.Ts
        #Model Implementation
        yk1 = (1 + a*Ts) * yk + Ts*b*uk
        return yk1

    def Controller(self, y, r, u_prev, e_prev):
        Kp = self.Kp
        Ti = self.Ti
        Ts = self.Ts
        e = r - y
        u = u_prev + Kp*(e - e_prev) + (Kp/Ti)*Ts*e
        return u, e