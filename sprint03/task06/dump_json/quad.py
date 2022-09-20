"""
DESCRIPTION
Create a script with a function quad() that takes three numbers (a , b , and c ),
and returns a JSON string with information about a quadratic equation with these values.
The result must be indented with three levels. If one of the arguments is not an integer or a ﬂoat, or a  is equal to 0,
then the function must return 'Cannot generate a quadratic equation.'
The resulting object must have two ﬁelds: "equation" and "solution".
The value of "equation" must be a string representing the equation.
The value of the "solution" must be an object with the ﬁelds: "discriminant", with the value of the discriminant of the equation,
and "x", with the value of x for the equation. Both the discriminant and value(s) of x must be outputted as ﬂoats,
rounded to three decimal places (rounding only affects the JSON output, not the calculations).
Also, make sure you don't have any negative zeros in your output.
Your function must only calculate real solutions.
In case the solutions are complex (hint: when the discriminant is negative),
the value of "x" must be null. If there are two real solutions for x, the value of the ﬁeld "x" must be a sorted array of the two solutions.
Otherwise (one real solution), just a number with the value of x.
"""


def quad(a, b, c):
    import json
    import math

    try:
        float(a), float(b), float(c)
        if a != 0:
            # Quadratic formular
            "formular = ax2 + bx + c = 0"

            # Step 2: Calculate discriminant
            D = (b**2) - (4 * a *c)

            # Step 3: Find roots of quadratic equation using Python (value of x)
            '''
            if the discriminant is positive b^{2}-4ac> 0   , then the quadratic equation has two solutions.
            if the discriminant is equal b^{2}-4ac= 0   , then the quadratic equation has one solution.
            if the discriminant is negative b^{2}-4ac< 0   , then the quadratic equation has no solution. '''

            # If the discriminant is greater
            # than 0, then 2 solutions (real and different roots)
            if D > 0 :
                sq_root_D = math.sqrt(D)
                x1 = (-b + sq_root_D)/(2 * a)
                x2 = (-b - sq_root_D)/(2 * a)
                rx1 = round(x1, 3)
                rx2 = round(x2, 3)
                list_arr = [rx1, rx2]
                dictionary = {"equation": f"{a}x^2 + {b}x + {c}=0", "solution": {"discriminant": D, "x": list_arr }}
                json_object = json.dumps(dictionary, indent = 4)
                return json_object

            # If the discriminant is equal 0,
            # then 1 solutions (real and same roots)
            elif D == 0 :
                x = -b / (2 * a)
                rx = round(x, 3)
                dictionary = {"equation": f"{a}x^2 + {b}x + {c}=0", "solution": {"discriminant": D, "x": rx }}
                json_object = json.dumps(dictionary, indent = 4)
                return json_object

            # Elif the discriminant is less
            # than 0, then value of x is null (Complex Roots)
            elif D < 0 :

                dictionary = {"equation": f"{a}x^2 + {b}x + {c}=0", "solution": {"discriminant": D, "x": 'null' }}
                json_object = json.dumps(dictionary, indent = 4)
                return json_object



        else:
            return f"Cannot generate a quadratic equation."

    except:
        return f"Cannot generate a quadratic equation."












