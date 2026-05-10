"""
3.3PP Functions: Distance Required to Stop
"""

__author__ = "Zhibing Song"

#Add any imports here:nothing

#Define your new function here
def calculate_distance (velocity:float ,time:float )-> float :
    """
    This function calculates the distance to stop the vehicle.
    args:
        velocity:The velocity of the distance as a float.
        time:The time of the distance as a float.
        
    return:
        The calculated distance as a float.
    """
    
    velocity: float 
    time: float 
    distance: float 
    
    FRICTION = 0.7
    GRAVITY = 9.81
    
    distance =velocity*time+(velocity**2)/(2*FRICTION*GRAVITY)
    
    return distance 

def main():

    print("Distance to stop1")
    distance1= calculate_distance(22.22,1.75)
    print (f"{distance1:.2f}")
    
    print("Distance to stop2")
    distance2= calculate_distance(8.33,3.3)
    print(f"{distance2:.2f}")

    velocity= float(input("Input initial velocity:"))
    time= float(input("Input reaction time: "))
    
    distance3= calculate_distance(velocity,time)
    print (f"{distance3:.2f}")

if __name__ == "__main__":
    main()