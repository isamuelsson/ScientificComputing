# ScientificComputing-Python-

OrdinaryDifferentialEquations.py - Uses Euler’s method to solve for the motion of an object in free fall and to compute the motion of a projectile in the presence of drag. 

    - initial conditions: 𝑦0 = 12.0𝑚, 𝑣0 = 35.0𝑚/𝑠, 𝑔  = 9.8𝑚/𝑠2
    - determines the height for times  0≤𝑡≤8𝑠
    - graph of y versus t
    - relative error in the height at  𝑡=8𝑠



DifferentialEquationSolver.py - Comparison of the RK2 solver and Euler's method. Uses the RK2 solver to compute the relative error at the last time point for different resolutions. 

    - computes the relative error in RK2 code when the number of time steps is set to nts=100
    - finds the (approximate) number of time steps required for Euler to give a result with comparable error



RK2Solver.py - Uses the RK2 solver for differential equations.


ScipyOdientIntegrator.py - Uses the scipy odeint integrator to solve a nuclear decay problem.

    - plot comparing the results of the scipy obtained solution with the analytic result, the RK2 result, and the Euler result     (for nts=5)
