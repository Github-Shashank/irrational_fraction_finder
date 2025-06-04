import math

class irr_frac:
    
    def __init__(self, irr_num, min_dtr, max_dtr):
        if min_dtr > max_dtr:
            raise ValueError("min_dtr must be less than or equal to max_dtr")
        self.irr_num = irr_num
        self.min_dtr = min_dtr
        self.max_dtr = max_dtr+1
        self.inp_val = {"irr_num":irr_num,"min_dtr":min_dtr,"max_dtr":max_dtr}
        self.comb = {}
        self.result = self._compute()

    def _compute(self):
        for dnmtr in range(self.min_dtr, self.max_dtr):
            for numtr in range(int(dnmtr * self.irr_num), int(self.max_dtr * self.irr_num)):
                if math.gcd(numtr, dnmtr) != 1:
                    continue
                error = abs(numtr / dnmtr - self.irr_num)
                self.comb[error] = [numtr, dnmtr, numtr / dnmtr, error]
                if numtr / dnmtr > self.irr_num:
                    break
        return self.comb[min(self.comb)]
    
    def __str__(self):
        return str(self.inp_val)
    
    @property
    def best_value(self):
        n, d, approx, error = self.result
        return f"Your irrational number {self.irr_num} ≈ {n}/{d} = {approx}, with error of {error}"
    
    def other_comp(self):
        return list(self.comb.values())
