class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # compute the max altitude
        max_altitude = 0
        current_altitude = 0

        # cummulate and then take max
        for g in gain:
            current_altitude += g
            max_altitude = max(max_altitude, current_altitude)

        return max_altitude
