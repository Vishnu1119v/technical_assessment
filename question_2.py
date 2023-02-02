class validate:
    def validate_triangle(self,a,b,c):
        if a+b>=c and b+c>=a and c+a>=b:
            print("valid triangle")
        else:
            print("invalid triangle")
    def validate_rectangle(self,a,b,c,d):
        if (a==b and c==d) or (a==c and b==d) or (a==d and b==c):
            print("valid rectangle")
        else:
            print("Invalid rectangle")
obj1=validate()
obj1.validate_triangle(4,5,6)
obj1.validate_rectangle(1,2,2,1)