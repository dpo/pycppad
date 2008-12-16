from cppad import *
ok = True
# declare level one independent variable vector and start level one recording
level = 1
ad_x = array( [ ad_double(2) , ad_double(3) ] )
independent(ad_x, level)
# declare level two independent variable vector and start level two recording
level = 2
ad_ad_x = array( [ ad_ad_double(ad_x[0]) , ad_ad_double(ad_x[1]) ] )
independent(ad_ad_x, level)
# declare level 2 dependent variable vector and stop level 2 recording
ad_ad_y = array( [ 2. * ad_ad_x[0] * ad_ad_x[1] ] )
ad_f = adfun_ad_double(ad_ad_x, ad_ad_y) # f(x0, x1) = 2. * x0 * x1
# evaluate the function f(x) using level one independent variable vector
p  = 0
ad_fp = array( [ ad_double(0.) ] )  # kludge to pass back fp
ad_f.forward(p, ad_x, ad_fp)
ok = ok and (ad_fp == 2. * ad_x[0] * ad_x[1])
# evaluate the partial of f with respect to the first component
p  = 1
ad_xp = array( [ ad_double(1.) , ad_double(0.) ] )
ad_f.forward(p, ad_xp, ad_fp)
ok = ok and (ad_fp == 2. * ad_x[1])
# declare level 1 dependent variable vector and stop level 1 recording 
ad_y = 2. * ad_fp
g = adfun_double(ad_x, ad_y) # g(x0, x1) = 2. * partial_x0 f(x0, x1) = 4 * x1
# evaluate the function g(x) at x = (4,5)
p  = 0
x  = array( [ 4. , 5. ] )
gp = g.forward(p, x)
ok = ok and (gp == 4. * x[1])
# evaluate the partial of g with respect to x0
p  = 1
xp = array( [ 1. , 0. ] )
gp = g.forward(p, xp)
ok = ok and (gp == 0.)
# evaluate the partial of g with respect to x1
p  = 1
xp = array( [ 0. , 1. ] )
gp = g.forward(p, xp)
ok = ok and (gp == 4.)
if( ok ) :
	print 'OK:    example_2: using ad_ad_double'
else :
	print 'Error: example_2: using ad_ad_double'