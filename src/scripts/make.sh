cd ../..;
catkin_make;
source devel/setup.bash;
cd src/scripts;
rosrun cs1567p2 Localize.py;
