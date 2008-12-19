# ifndef PYTHON_CPPAD_ADFUN_INCLUDED
# define PYTHON_CPPAD_ADFUN_INCLUDED

# include "setup.hpp"

namespace python_cppad {
	// -------------------------------------------------------------
	// class ADFun_double
	//
	class ADFun_double {
	private:
		CppAD::ADFun<double> f_;
	public:
		// constructor
		ADFun_double(array& x_array, array& y_array);
		// member function Forward
		array Forward(int p, array& xp);
	};
	// -------------------------------------------------------------
	// class ADFun_AD_double
	//
	class ADFun_AD_double {
	private:
		CppAD::ADFun<AD_double> f_;
	public:
		// constructor
		ADFun_AD_double(array& x_array, array& y_array);
		// member function Forward
		array Forward(int p, array& xp);
	};
}

# endif
