# Ultraview

Ultraview is a graphical simulation in pygame of how a 4D world can be visualized.
Each one of the larger cubes are called "ultrapoints", representing entire 3d spaces.
Each ultrapoint has a position in the 4th dimension axis (which we call the "ultraline").
When running the program, you can use WASD to move horizontally and Space/Shift to move vertically inside the ultrapoint in which the cursor is located. To move between ultrapoints, you can use Q/E. For placing blocks, click with your mouse left button. For removing blocks, click with your right mouse button. To zoom in and out inside an ultrapoint, you can use the mouse wheel. If you do so while holding CTRL, you can zoom trough the entire ultraline.

### Setup

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```
