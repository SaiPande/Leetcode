class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        asteroids.sort()

        for i in asteroids:
            if i<=mass:
                mass += i
            else:
                return False

        return True            