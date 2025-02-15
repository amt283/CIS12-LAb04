# CIS-12 Lab 04

<b> Reflection </b>

<i>"Reflect on how encapsulation and generalization helped us break down the drawing process for this scene."</i>

Encapsulation was used to reduce repetitive code and make it easier to reuse while improving the code's readability. 
For instance, we created the "draw_jack()" function which was used to draw the Jack'o'lanterns. We technically didn't 
have to do that since we could have just used the "draw_pumpkin()", "draw_eye()" and "draw_mouth()" functions. 
But as you can probably tell, it created a lot of repetitive code that quickly added up and was a chore to read. 
By encapsulating the function calls in draw_jack, four lines of code were reduced to one.

Generalization helped us with the creation of the functions like "draw_jack()" so that nothing was hard-coded. This 
means that everything is dependent on the parameters passed to the function, so if someone wanted a giant pumpkin in 
the sky and a tiny one on the ground, they could easily do so by picking different y-coordinates and radius sizes, but
the function itself will always perform in a reliable way.

