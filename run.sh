cd ~/cs1567_ws;
catkin_make;
source devel/setup.bash;
cd ~/cs1567_ws/src/scripts;
printf '\a';
rosrun cs1567p2 Localize.py;
