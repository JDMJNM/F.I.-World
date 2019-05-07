#version 330
layout(location = 0) in vec3 position;
layout(location = 1) in vec2 texture_cords;
layout(location = 2) in vec3 offset;

uniform mat4 model;
uniform mat4 view;
uniform mat4 proj;

out vec2 textures;

void main()
{
    vec3 final_pos = vec3(position.x + offset.x, position.y + offset.y, position.z + offset.z);
    gl_Position =  proj * view * model * vec4(final_pos, 1.0f);
    textures = texture_cords;
}
