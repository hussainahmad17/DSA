class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        n=len(asteroids)

        for i in range(0,n):
            if asteroids[i]>0:
                stack.append(asteroids[i])
            else:
                while len(asteroids)!=0 and stack[-1]>0 and stack[-1]<abs(asteroids[i]):
                    stack.pop()
                    if len(asteroids)!=0 and stack[-1]==abs(asteroids[i]):
                        stack.pop()
                    elif len(asteroids) == 0 or stack[-1]<0:
                        stack.append(asteroids[i])
        return stack