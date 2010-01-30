# $begin runge_kutta_4_cpp.py$$ $newlinech #$$
# $spell
#	runge_kutta
#	numpy
#	pycppad
#	def
#	dt
#	yi
#	yf
# $$
# $index example, runge_kutta_4$$
# $index C++ speed, python function$$
# $index speed, python function$$
# $index tape, python function$$
# $index runge_kutta_4, evaluate solution$$
#
# $section runge_kutta_4 With C++ Speed: Example and Test$$
#
# $head Discussion$$
# Define $latex y : \B{R}^2 \times \B{R} \rightarrow \B{R}^n$$ by
# $latex \[
#	\begin{array}{rcl}
#	y(x, 0)            & = & x_0 
#	\\
#	\partial_t y(x, t) & = & x_1 y(x, t)
#	\end{array}
# \] $$ 
# It follows that 
# $latex \[
#	y(x, t) = x_0 \exp ( x_1 t )
# \] $$
# Suppose we want to compute values for the function 
# $latex g : \B{R}^2 \rightarrow \B{R} $$ defined by
# $latex \[
#	g(x) = y(x, 1)
# \] $$
# In this example we compare the execution time for doing this in pure Python
# with using a pycppad function object to compute $latex g(x)$$ in C++.  
#
# $head Source Code$$
#
# $code
# $verbatim%example/runge_kutta_4_cpp.py%0%# BEGIN CODE%# END CODE%1%$$
# $$
# $end
# BEGIN CODE
from pycppad import *
import time
def pycppad_test_runge_kutta_4_cpp() :
	x_1 = 0;   # used to switch x_1 between float and ad(float)
	def fun(t , y) :
		f     = x_1 * y
		return f
	ti = 0.    # initial time
	tf = 1.    # finial time
	M  = 1000  # number of times steps to take
	
	# declare a_x to be the independent variable vector
	x    = numpy.array( [2., .5] )
	a_x  = independent( numpy.array( x ) )

	# initial value for y(t); i.e., y(0), is the first component of a_x
	a_y = numpy.array( [ a_x[0] ] )
	# x_1 is the second component of a_x
	x_1 = a_x[1]

	# use M times steps to approximate the solution
	s0 = time.time()
	dt = (tf - ti) / M
	t  = ti
	for k in range(M) :
		a_y = runge_kutta_4(fun, t, a_y, dt)
		t   = t + dt
	s1 = time.time()
	# number of seconds to solve the ODE using python ad(float)
	tape_sec = s1 - s0

	# define the AD function g : x -> y(tf)
	g = adfun(a_x, a_y)

	# time using C++ version of integrator
	s0      = time.time()
	y       = g.forward(0, x)
	s1      = time.time()
	# number of seconds to solve the ODE using the pycppad function object g
	cpp_sec = s1 - s0

	# check solution is correct
	assert( abs( y[0] - x[0] * exp( x[1] * tf ) ) < 1e-10 ) 

	# time using doulbe precision version of integrator
	s0  = time.time()
	y   = numpy.array( [ x[0] ] ); 
	x_1 = x[1];
	t   = ti
	for k in range(M) :
		y = runge_kutta_4(fun, t, y, dt)
	s1         = time.time()
	# number of seconds to solve the ODE using python float
	python_sec =  s1 - s0

	# check solution is correct
	assert( abs( y[0] - x[0] * exp( x[1] * tf ) ) < 1e-10 ) 
	
	# check that C++ is always more than 20 times faster
	assert( 20. * cpp_sec <= python_sec )

	# Actual factor is ~ 100 for debug ~ 300 for optimized build
	# uncomment the print statement below to see it for your machine / build.
	format = 'cpp_sec = %8f, python_sec/cpp_sec = %4.0f'
	format = format + ', tape_sec/cpp_sec = %4.0f'
	# print format % ( cpp_sec, python_sec/cpp_sec, tape_sec/cpp_sec )

# END CODE
