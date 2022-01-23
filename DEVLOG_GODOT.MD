# GODOT

- Python godot
got it to work

- voxel godot
- built in godot 4, but godot_python is running in 3.4 so best to switch back and rebuild for 3.4

build godot 3.4: `scons -j6 platform=x11`
build godot 4: `scons -j6 platform=x11linuxbsd`
settings that work:
- generator: voxelnoise, type SDF
- mesher transvoxel

collision layer vs mask:

- water shader 1 (used atm)
`https://www.youtube.com/watch?v=PgcMXPdQrLI`

- another water shader to test
`https://github.com/Chrisknyfe/godot-scraps/tree/master/water_shader`

#