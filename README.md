# Satellite-Control-System
Principle of Satellite Motion and Control Mechanisms:<br>

Satellites orbiting the Earth are subject to various forces that can cause deviations from their prescribed trajectories or desired orientations. To address these challenges, satellites are equipped with thrusters that provide control inputs in the radial and tangential directions. These thrusters serve as critical control mechanisms, enabling altitude adjustments and station-keeping to maintain the satellite's intended orbit.<br/>

The motion of a satellite can be modeled mathematically by considering it as a particle moving in the Earth's equatorial plane. Using Newton's laws, the satellite's equations of motion are derived in terms of forces acting along the coordinate axes. For enhanced convenience and clarity, these equations are often expressed in polar coordinates, with parameters such as radial distance and angular displacement offering intuitive insights into the satellite's behavior and dynamics.<br>

Mathematical Modelling:<br>

The satellite is modeled as a particle $P$ of mass $𝑚$ moving in the Earth's equatorial plane. Its motion is described using Newton's laws in rectangular coordinates $(x,y)$, with forces $f_x$ and $f_y$ acting along the respective axes.<br>

To simplify the analysis, the equations are converted to polar coordinates $(r,θ)$, where $x = r cosθ$ and $y=r sinθ$. Under the influence of external forces, the equations of motion in polar coordinates become:<br>

* Radial motion: $m \dot{\dot{r}} - mr \dot{θ}^2 +\frac{k}{r^2} = u_1$
* Angular motion: $2m \dot{r}\dot{θ} + m r \dot{\dot{θ}} = u_2$

Here, $u_1$ and $u_2$ represent the control inputs provided by radial and tangential thrusters, respectively, and $k$ represents the strength of the central force, such as the gravitational force between the satellite and the Earth.<br>


