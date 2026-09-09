class Solution:
    def countCommas(self, n: int) -> int:
        totalcommas = 0
        thousandgrp = 1000

        while (thousandgrp <= n):
            totalcommas += n - thousandgrp + 1
            thousandgrp*= 1000
        return totalcommas                             