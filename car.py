# sreeram paladugu
# note - used distance keyword insted of range keyword


#baseclass
class Vehicle():
    def __init__(self, color):
        self.color = color
    def description(self):
        print("I'm a", self.color, "Vehicle")
        
        
        
        
        
#-----------------------------------------------------------------------------------------------------        
        




#class car is inherited from class vechicle
#child class for vehicle
class Car(Vehicle):
    def __init__(self, numcar, model, speed, color):
        self.numcar_model = numcar
        self.model = model
        self.speed = 0
        super().__init__(color) #calling vechiles init

    def set_numcar_model(self, numcar):
        self.numcar_model = numcar

    def set_model(self, model):
        self.model = model

    def set_speed(self, speed):
        self.speed = 0
        
    def set_color(self, color):
        self.color = color
    
    def get_numcar_model(self):
        return self.numcar_model

    def get_model(self):
        return self.model

    def get_speed(self):
        return self.speed

    #methods
    def accelerate(self):
        self.speed +=5

    def decelerate(self):
        self.speed -=5

    def get_speed(self):
        return self.speed
    
    def print(self):
        print(" carnumber :", self.numcar_model, "\n","car model :",  self.model, "\n", "car speed :", self.speed, "\n", "color :",  self.color,"\n", )
        
        
        
        
        
        
#-------------------------------------------------------------------------------------------------------------        






#child class for car
class EV(Car):
    def __init__(self, numcar, model, speed, color, distance, gen):
        self.numcar_model = numcar
        self.model = model
        self.speed = 0
        self.color = color
        self.distance = distance
        self.gen = gen
    
    def get_distance(self):
         return self.distance
     
    def get_gen(self):
         return self.gen  
     
    def set_distance(self, distance):
         self.distance = distance
     
    def set_gen(self, gen):
         self.gen = gen  
      
    def print(self):
        print(" carnumber :", self.numcar_model, "\n","car model :",  self.model, "\n", "car speed :", self.speed, "\n", "color :",  self.color,"\n", "range is :",  self.distance,"\n", "car generation is ",  self.gen)
        
            
            
#---------------------------------------------------------------------------------------------------------------------------------



             
def main():
    
    # passing variable to vehicle class and calling its function
    v = Vehicle("red")
    v.description()


    print("select the type of car \n")
    
    for i in range(0,1):
        
        #option selection
        print('1. normal car \n')
        print('2. electric car\n')
        
        choice = int(input('Enter your choice:'))

        if (choice == 1):
            numcar = input('Enter the car number: ')
            model = input('Enter the car model: ')
            color = input('Enter the car color: ')
            speed = 0

            mycar = Car(numcar, model, speed, color)
            mycar.description()
            
            #accelerate    
            for x in range(3):
                mycar.accelerate()
                print('speed: ', mycar.get_speed())

            #decelerate
            for x in range(2):
                mycar.decelerate()
                print('speed: ', mycar.get_speed())
            
            #printing car object attributes
            mycar.print()

        if (choice == 2):
            numcar = input('Enter the car number: ')
            model = input('Enter the car model: ')
            color = input('Enter the car color: ')
            speed = 0
            distance = input('Enter the range of the car: ')
            gen= input('Enter the car generation: ')
            
            ecar = EV(numcar, model, speed, color, distance, gen)
            
            
            #accelerate methord inherited from car class   
            for x in range(3):
                ecar.accelerate()
                print('speed: ', ecar.get_speed())
            
             #decelerate methord inherited from car class   
            for x in range(2):
                ecar.decelerate()
                print('speed: ', ecar.get_speed())
            
            #printing electric car object attributes    
            ecar.print()
#Call the main function
main()
