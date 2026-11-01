class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #If position if greater but time of one before is less then add to fleet
        fleets = 0
        cars = []
        for i in range(len(position)):
            time = (target - position[i])/speed[i]
            cars.append((position[i], time))
        
        sorted_cars = sorted(cars, key=lambda item: item[0])

        stack = []
        for pos, time in sorted_cars:
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)