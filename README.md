# Satellite-Control-System
Principle of Satellite Motion and Control Mechanisms:<br>

Satellites orbiting the Earth are subject to various forces that can cause deviations from their prescribed trajectories or desired orientations. To address these challenges, satellites are equipped with thrusters that provide control inputs in the radial and tangential directions. These thrusters serve as critical control mechanisms, enabling altitude adjustments and station-keeping to maintain the satellite's intended orbit.<br/>

The motion of a satellite can be modeled mathematically by considering it as a particle moving in the Earth's equatorial plane. Using Newton's laws, the satellite's equations of motion are derived in terms of forces acting along the coordinate axes. For enhanced convenience and clarity, these equations are often expressed in polar coordinates, with parameters such as radial distance and angular displacement offering intuitive insights into the satellite's behavior and dynamics.<br>

!. Mathematical Modelling:<br>

The satellite is modeled as a particle $P$ of mass $𝑚$ moving in the Earth's equatorial plane. Its motion is described using Newton's laws in rectangular coordinates $(x,y)$, with forces $f_x$ and $f_y$ acting along the respective axes.<br>

To simplify the analysis, the equations are converted to polar coordinates $(r,θ)$, where $x = r cosθ$ and $y=r sinθ$. therefore, under the influence of external forces, the equations of motion in polar coordinates become:<br>

* Radial motion: $m \dot{\dot{r}} - mr \dot{θ}^2 +\frac{k}{r^2} = u_1$
* Angular motion: $2m \dot{r}\dot{θ} + m r \dot{\dot{θ}} = u_2$

Here, $u_1$ and $u_2$ represent the control inputs provided by radial and tangential thrusters, respectively, and $k$ represents the strength of the central force, such as the gravitational force between the satellite and the Earth.<br>

2. Linearization:<br>

A change of variables is introduced to transform the equations of motion into a system of four first-order nonlinear differential equations in state-space representation. The new variables $x_1$, $x_2$, $x_3$, and $x_4$ relate to the satellite's radial and angular dynamics, while the control inputs $u_$1 and $u_2$ account for external forces.

The state-space equations are expressed as:<br>

$$\frac{dx}{dt} = f(x,u)$$<br>

where $x(t)$ is in $R^4$ and $u(t)$ is in $R^2$.<br>

Here, $f$ is a vector function with nonlinear components depending on the state $x$ and controls $u$.<br>

Now the nonlinear system is linearized around the equilibrium point $(x = 0, u = 0)$ to simplify analysis. The linearized system takes the form:<br>

$$\frac{dx}{dt} = Ax + Bu$$<br>

A represents the system dynamics and B represents the control influence<br>
This linearized form allows for standard control system analysis and design.<br>

3. Controllability Analysis: Using Kalman’s controllability test to determine system stability.

 💻 Implementation<br>

 This repository includes Python code for:<br>
 1. Solving differential equations using scipy.integrate.odeint
 2. Computing state transition matrices
 3. Simulating satellite motion
 4. Performing control system analysis

 🔗 References<br>

1. Ordinary Differential Equations - Principles and Applications (Nandakumaran A.K., Datti P.S., Raju K. George)
2. Finite Dimensional Linear Systems (R.W. Brockett)
3. Controllability of Nonlinear Systems (Joshi M.C., George R.K.)

