Title: DIYrotate
Slug: diyrotate

{% img {static}../images/diyrotate/comparison.gif 600 DIYrotate versus rotating frame footage comparison %}

_(L) DIYrotate versus (R) rotating frame footage. Both approaches enable observing fluid motions in a rotating tank with similar granularity!_

## Visit [https://diyrot.epss.ucla.edu/](https://diyrot.epss.ucla.edu/) to use DIYrotate!

DIYrotate is a web app for digitally rotating movies. Given footage of a rotating tank from above, the program can identify the tank and rotate it about its center per a specified rate. DIYrotate is easy to use with no sign up required -- simply input your movie and parameters then download the result!

---

## Goal: Enable users to clearly and conveniently observe fluid motions in a rotating tank

Rotating tank platforms are straightforward and insightful models for studying geophysical fluid dynamics. The systems capture the fundamental attributes of Earth's (and other planet's) atmospheres, oceans and interiors -- the water and rotation represent a planet's fluid bodies and rotation respectively. Fluid motions in the rotating tank are governed by the same fluid dynamics as counterparts in the real world. Thus, our goal is to observe the fluid motions to develop an intuition behind the forces responsible for our weather, ocean currents, magnetic field and more! There are two traditional approaches:

_Note that we are generally interested in observing fluid motions in a rotating tank from above. Rotation aligns fluid bodies with its axis and thus, for many experiments, the surface of the water expresses the key fluid dynamics of the system._

### Approach 1: Capture footage in the stationary frame

The stationary frame refers to the view of a camera fixed as the tank rotates -- this is analogous to a spacecraft observing a planet from afar. The filming setup is flexible -- the camera is supported above the tank by a point outside the system. The mount can be jerry rigged with basic requirements (suspend camera) and few constraints (can be heavy or light and large or small). However, results are difficult to interpret because fluid motions are coupled with rotation.

### Approach 2: Capture footage in the rotating frame

The rotating frame refers to the view of a camera rotating in sync with the tank -- this is analogous to a person observing a planet from its poles. The filming setup is subject to constraints  -- the camera is supported above the tank by a point within the system. The camera and its mount must not hinder the tank's rotation leading to limits on size and weight. Nevertheless, results are ideal for analysis because rotating the camera in sync with the tank abstracts away rotation thus yielding fluid motions themselves.

{% img {static}../images/diyrotate/stationary-frame-setup.png 400 Stationary frame filming setup %}
{% img {static}../images/diyrotate/rotating-frame-setup.gif 400 Rotating frame filming setup %}

_(L) Stationary frame filming setup -- a camera is fixed above the tank as it rotates. The camera is supported by a point outside of the system. Subject to few constraints, its mount can be put together with household items. If desired, larger cameras like DSLRs can be safely attached with sufficient reinforcement to mitigate fears of falling in water.  
(R) Rotating frame filming setup -- a camera is rotating in sync with the tank. The camera is supported by a point within the system. Its mount is constained by size and weight to enable the tank to continue rotating unhindered. Attaching larger cameras like DSLRs are a risky proposition without the luxury of added support. Meanwhile, the camera mount can interfere with during experiments as users must perform necessary steps (e.g. adding food coloring) whilst avoiding the structure._

{% img {static}../images/diyrotate/stationary-frame-result.gif 400 Stationary frame footage %}
{% img {static}../images/diyrotate/rotating-frame-result.gif 400 Rotating frame footage %}

_(L) Stationary frame footage -- difficult to discern fluid motions in the rotating tank. The fluid motion is coupled with the impact of rotation thus obscuring dynamic structures formed during experiments.  
(R) Rotating frame footage -- fluid motions in the rotating tank are apparent. The impact of rotation has been abstracted away yielding fluid motions themselves.  
Note that &Omega; indicates the rotation direction._

To this end, capturing footage in the rotating frame is the go-to option when recording experiments for analysis. Studying fluid motions of the system from an inside perspective removes the impact of rotation and provides an intuitive view of phenomena -- analogous to the camera, we (humans) are situated in the rotating frame of Earth. However, the filming setup may require additional thought. The rotating frame offers clear results and the stationary frame offers convenient setup -- what if we can combine the best of both worlds? We introduce a new approach:

### Approach 3: Obtain rotating frame results from stationary frame footage

DIYrotate fills this role! Use DIYrotate to digitally rotate stationary frame footage in the direction and magnitude opposite of the system's rotation -- we call this process de-rotation. This serves to cancel out and abstract away rotation leaving behind fluid motions themselves. By de-rotating the stationary frame footage, DIYrotate programatically yields results equivalent to rotating frame footage yet with fewer setup constraints to consider.

---

## How to use DIYrotate

DIYrotate can be accessed at [https://diyrot.epss.ucla.edu/](https://diyrot.epss.ucla.edu/). The web app features instructions guiding users through de-rotation step by step.

### Step 1: Capture stationary frame footage  
For best results, ensure that:  
- Lights are not reflecting on the surface of the water. Reflections from the stationary frame yield artifacts in rotating frame results.  
- Both the tank and camera are level. DIYrotate assumes that stationary frame footage is taken from directly above. Deviations from level can introduce distortions during de-rotation.  
- The tank encompasses the majority of the camera's view.

### Step 2: Upload stationary frame footage to DIYrotate

### Step 3: Provide parameters to DIYrotate
Necessary input includes:  
- The location of the circle forming the tank. Specify the circle by clicking on the center of the tank then dragging until the circle's radius reaches the tank's rim.  
- The de-rotation rate -- opposite direction and same magnitude as the system's rotation rate. Positive and negative de-rotation rates will counteract counterclockwise and clockwise system rotation respectively. Note that non-integer values can be provided.

### Step 4: Download de-rotated footage from DIYrotate!

{% img {static}../images/diyrotate/pre-diyrotate.gif 400 DIYrotate input %}
{% img {static}../images/diyrotate/post-diyrotate.gif 400 DIYrotate output %}

_(L) DIYrotate input (stationary frame footage) versus (R) DIYrotate output (programatically created rotating frame footage). Note that the impact of rotation has been removed!_

For a detailed version of the instructions and to see more results, watch the following video for a comprehensive overview of DIYrotate!

<iframe width="560" height="315" src="https://www.youtube.com/embed/u6OoYdrYZ0o" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

## Check out the code for DIYrotate

DIYrotate is an open source project available on GitHub!

### DIYrotate (web app) [https://github.com/OrangeRoof/diyrot](https://github.com/OrangeRoof/diyrot)
The web app version of DIYrotate is described above. This program is ideal for de-rotating stationary frame footage with no installation required.
### DIYrotate (local) [https://github.com/DIYnamics/DIYrotate](https://github.com/DIYnamics/DIYrotate)
The local version of DIYrotate enables users to de-rotate stationary frame footage similar to its web app counterpart. This program offers a multitude of options providing fine grained control over results. The local version of DIYrotate is launched from the Terminal and features a GUI for user input -- more details can be found on the GitHub repository.
