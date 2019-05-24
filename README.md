# F.I. World
# Controls
* W - Walk forwards
* A - Walk backwards
* S - Walk to the left
* D - Walk to the right
* Left Mouse Button - Break the highlighted block
* Right Mouse Button - Place at side of highlighted block
* Space - Jump
* Shift - Crouch
* 1 to 9 - Switch which slot is active in the hotbar or action bar
* E - Access inventory
* Esc - Pause game and open menu
* P - Respawn at starting position
# V1.2.5
* Fixed minor bugs
# V1.2.4
* Patched sprinting and flying:
    * Both sprinting and flying have a delay time of 250 milliseconds instead of the previous 1000 milliseconds.
* Updated placement and destruction of blocks:
    * The delay to break a block and consecutively place blocks have been shortened to 250 milliseconds as well.
* Tweaked/updated crouching:
    * Crouching now stops the player from falling off blocks if they try to walk off one.
* Fixed lag issues with larger worlds and initialization
* Tweaked/updated a lot of other things as well (such as window title, code format, etc.)
* What's next?
    * Adding animations is still on my list.
    * Items and visual cues will most likely occur before animations (with the exception of block breaking).
# V1.2.1
* Added sprinting and flying:
    * Sprinting can be achieved by double-pressing the "w" key.
    * Flying is enabled by double-pressing the "space" key.
* Updated placement and destruction of blocks:
    * Breaking any block now requires players to hold the left mouse button for 1 second.
    * Placing blocks are still done by right-clicking, but are now also able to be placed consecutively after a 250
    millisecond cool-down by holding the right mouse button.
* Tweaked/updated crouching:
    * Crouching now lowers the player's camera view by 0.125 meters instead of 0.3 meters.
* What's next?
    * Adding animations are next on my list, which will most likely take days to complete.
    * I also plan on adding basic items such as tools (shovels, pickaxes, axes, etc.)
# V1.0.0
* GitHub initialization
* Basic main and pause menu
* Loading screen along with instructions
* Fully functional world initialization and chunk generation
* Placement and destruction of blocks in-game
