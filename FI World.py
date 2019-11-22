# Jacob Meadows
# Computer Programming II, 6th Period
# 06 May, 2019
"""
F.I World: Jacob Meadows' final program for Computer Programming II
    Copyright (C) 2019  Jacob Meadows

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import os

import OpenGL.GL.shaders
import numpy
import pygame
import pyrr
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image


CUBE = numpy.array([0.0, 0.0, 1.0, 0.0, 0.0,
                    1.0, 0.0, 1.0, 1.0, 0.0,
                    1.0, 1.0, 1.0, 1.0, 1.0,
                    0.0, 1.0, 1.0, 0.0, 1.0,

                    0.0, 0.0, 0.0, 0.0, 0.0,
                    1.0, 0.0, 0.0, 1.0, 0.0,
                    1.0, 1.0, 0.0, 1.0, 1.0,
                    0.0, 1.0, 0.0, 0.0, 1.0,

                    1.0, 0.0, 0.0, 0.0, 0.0,
                    1.0, 1.0, 0.0, 0.0, 1.0,
                    1.0, 1.0, 1.0, 1.0, 1.0,
                    1.0, 0.0, 1.0, 1.0, 0.0,

                    0.0, 1.0, 0.0, 1.0, 1.0,
                    0.0, 0.0, 0.0, 1.0, 0.0,
                    0.0, 0.0, 1.0, 0.0, 0.0,
                    0.0, 1.0, 1.0, 0.0, 1.0,

                    0.0, 0.0, 0.0, 0.0, 0.0,
                    1.0, 0.0, 0.0, 1.0, 0.0,
                    1.0, 0.0, 1.0, 1.0, 1.0,
                    0.0, 0.0, 1.0, 0.0, 1.0,

                    1.0, 1.0, 0.0, 0.0, 0.0,
                    0.0, 1.0, 0.0, 1.0, 0.0,
                    0.0, 1.0, 1.0, 1.0, 1.0,
                    1.0, 1.0, 1.0, 0.0, 1.0], dtype=numpy.float32)
HIGHLIGHTED_CUBE = numpy.array([-0.02, -0.02, 1.02, 0.0, 0.0,
                                1.02, -0.02, 1.02, 1.0, 0.0,
                                1.02, 1.02, 1.02, 1.0, 1.0,
                                -0.02, 1.02, 1.02, 0.0, 1.0,

                                -0.02, -0.02, -0.02, 0.0, 0.0,
                                1.02, -0.02, -0.02, 1.0, 0.0,
                                1.02, 1.02, -0.02, 1.0, 1.0,
                                -0.02, 1.02, -0.02, 0.0, 1.0,

                                1.02, -0.02, -0.02, 0.0, 0.0,
                                1.02, 1.02, -0.02, 0.0, 1.0,
                                1.02, 1.02, 1.02, 1.0, 1.0,
                                1.02, -0.02, 1.02, 1.0, 0.0,

                                -0.02, 1.02, -0.02, 1.0, 1.0,
                                -0.02, -0.02, -0.02, 1.0, 0.0,
                                -0.02, -0.02, 1.02, 0.0, 0.0,
                                -0.02, 1.02, 1.02, 0.0, 1.0,

                                -0.02, -0.02, -0.02, 0.0, 0.0,
                                1.02, -0.02, -0.02, 1.0, 0.0,
                                1.02, -0.02, 1.02, 1.0, 1.0,
                                -0.02, -0.02, 1.02, 0.0, 1.0,

                                1.02, 1.02, -0.02, 0.0, 0.0,
                                -0.02, 1.02, -0.02, 1.0, 0.0,
                                -0.02, 1.02, 1.02, 1.0, 1.0,
                                1.02, 1.02, 1.02, 0.0, 1.0], dtype=numpy.float32)
HOTBAR = numpy.array([0.0, 0.0, 0.0, 0.0, 0.0,
                      0.0, 44.0, 0.0, 0.0, 1.0,
                      364.0, 44.0, 0.0, 1.0, 1.0,
                      364.0, 0.0, 0.0, 1.0, 0.0], dtype=numpy.float32)
ACTIVE_BAR = numpy.array([0.0, 0.0, 0.0, 0.0, 0.0,
                          0.0, 48.0, 0.0, 0.0, 1.0,
                          48.0, 48.0, 0.0, 1.0, 1.0,
                          48.0, 0.0, 0.0, 1.0, 0.0], dtype=numpy.float32)
HOTBAR_ICON = numpy.array([0.0, 0.0, 0.0, 0.0, 0.0,
                           0.0, 32.0, 0.0, 0.0, 1.0,
                           32.0, 32.0, 0.0, 1.0, 1.0,
                           32.0, 0.0, 0.0, 1.0, 0.0], dtype=numpy.float32)
CROSSHAIR_V = numpy.array([15.0, 0.0, 0.0, 0.0, 0.0,
                           15.0, 32.0, 0.0, 0.0, 1.0,
                           17.0, 32.0, 0.0, 1.0, 1.0,
                           17.0, 0.0, 0.0, 1.0, 0.0], dtype=numpy.float32)
CROSSHAIR_H = numpy.array([0.0, 15.0, 0.0, 0.0, 0.0,
                           0.0, 17.0, 0.0, 0.0, 1.0,
                           32.0, 17.0, 0.0, 1.0, 1.0,
                           32.0, 15.0, 0.0, 1.0, 0.0], dtype=numpy.float32)
INVENTORY = numpy.array([0.0, 0.0, 0.0, 0.0, 0.0,
                         0.0, 332.0, 0.0, 0.0, 1.0,
                         352.0, 332.0, 0.0, 1.0, 1.0,
                         352.0, 0.0, 0.0, 1.0, 0.0], dtype=numpy.float32)
SCREEN = numpy.array([0.0, 0.0, 0.0, 0.0, 0.0,
                      0.0, 720.0, 0.0, 0.0, 1.0,
                      1280.0, 720.0, 0.0, 1.0, 1.0,
                      1280.0, 0.0, 0.0, 1.0, 0.0], dtype=numpy.float32)
BUTTON_OUTLINE = numpy.array([0.0, 0.0, 0.0, 0.0, 0.0,
                              0.0, 40.0, 0.0, 0.0, 1.0,
                              400.0, 40.0, 0.0, 1.0, 1.0,
                              400.0, 0.0, 0.0, 1.0, 0.0], dtype=numpy.float32)
CUBE_INDICES = numpy.array([0, 1, 2, 2, 3, 0,
                            6, 5, 4, 4, 7, 6,
                            8, 9, 10, 10, 11, 8,
                            12, 13, 14, 14, 15, 12,
                            16, 17, 18, 18, 19, 16,
                            20, 21, 22, 22, 23, 20], dtype=numpy.uint32)
CUBE_INDICES_EDGES = numpy.array([0, 1, 2, 3,
                                  6, 5, 4, 7,
                                  8, 9, 10, 11,
                                  12, 13, 14, 15,
                                  16, 17, 18, 19,
                                  20, 21, 22, 23], dtype=numpy.uint32)
QUAD_INDICES = numpy.array([0, 1, 2, 2, 3, 0], dtype=numpy.uint32)
CHARACTER_DICT = {
    "a": (((8, 48), (5, 5)), ((8, 32), (5, 7))),
    "b": (((16, 48), (5, 7)), ((16, 32), (5, 7))),
    "c": (((24, 48), (5, 5)), ((24, 32), (5, 7))),
    "d": (((32, 48), (5, 7)), ((32, 32), (5, 7))),
    "e": (((40, 48), (5, 5)), ((40, 32), (5, 7))),
    "f": (((48, 48), (4, 7)), ((48, 32), (5, 7))),
    "g": (((56, 48), (5, 6)), ((56, 32), (5, 7))),
    "h": (((64, 48), (5, 7)), ((64, 32), (5, 7))),
    "i": (((72, 48), (1, 7)), ((72, 32), (3, 7))),
    "j": (((80, 48), (5, 8)), ((80, 32), (5, 7))),
    "k": (((88, 48), (4, 7)), ((88, 32), (5, 7))),
    "l": (((96, 48), (2, 7)), ((96, 32), (5, 7))),
    "m": (((104, 48), (5, 5)), ((104, 32), (5, 7))),
    "n": (((112, 48), (5, 5)), ((112, 32), (5, 7))),
    "o": (((120, 48), (5, 5)), ((120, 32), (5, 7))),
    "p": (((0, 56), (5, 6)), ((0, 40), (5, 7))),  # temporary capital size values (5, 7)
    "q": (((8, 56), (5, 6)), ((8, 40), (5, 7))),  # temporary capital size values (5, 7)
    "r": (((16, 56), (5, 5)), ((16, 40), (5, 7))),  # temporary capital size values (5, 7)
    "s": (((24, 56), (5, 5)), ((24, 40), (5, 7))),  # temporary capital size values (5, 7)
    "t": (((32, 56), (3, 7)), ((32, 40), (5, 7))),  # temporary capital size values (5, 7)
    "u": (((40, 56), (5, 5)), ((40, 40), (5, 7))),  # temporary capital size values (5, 7)
    "v": (((48, 56), (5, 5)), ((48, 40), (5, 7))),  # temporary capital size values (5, 7)
    "w": (((56, 56), (5, 5)), ((56, 40), (5, 7))),  # temporary capital size values (5, 7)
    "x": (((64, 56), (5, 5)), ((64, 40), (5, 7))),  # temporary capital size values (5, 7)
    "y": (((72, 56), (5, 6)), ((72, 40), (5, 7))),  # temporary capital size values (5, 7)
    "z": (((80, 56), (5, 5)), ((80, 40), (5, 7))),  # temporary capital size values (5, 7)
}
SPECIAL_CHARACTER_DICT = {
    ".": ((112, 16), (1, 2)),
    ">": ((112, 24), (4, 7)),
    ",": ((96, 16), (1, 3)),
    "<": ((96, 24), (4, 7)),
    "-": ((104, 16), (5, 1)),
    "*": ((80, 16), (4, 3)),
    ":": ((80, 24), (1, 6)),
    "0": ((0, 24), (5, 7)),
    "1": ((8, 24), (5, 7)),
    "2": ((16, 24), (5, 7)),
    "3": ((24, 24), (5, 7)),
    "4": ((32, 24), (5, 7)),
    "5": ((40, 24), (5, 7)),
    "6": ((48, 24), (5, 7)),
    "7": ((56, 24), (5, 7)),
    "8": ((64, 24), (5, 7)),
    "9": ((72, 24), (5, 7))
}
ASCII_PNG = Image.open("textures/character_sheet/ascii.png")


class App:
    def __init__(self, width, height):
        pygame.init()
        pygame.mixer.Sound("Loituma - levans Polka.ogg").play(-1)
        self.width, self.height = width, height
        pygame.display.set_caption("F.I. World")
        self.main_window = pygame.display.set_mode((self.width, self.height),
                                                   pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)

        self.clock = pygame.time.Clock()
        self.cam = Camera(self)

        self.chunks = 2  # radius of chunks around player in world (temporary variable)
        self.mouse_visibility = True
        self.in_menu = True
        self.in_game = False
        self.in_inventory = False
        self.paused = False
        self.new_game = False
        self.world_instances = dict()
        self.visible_blocks = dict()
        self.chunk_dict = dict()
        self.vao_3d_dict = dict()
        self.vao_2d_dict = dict()
        self.block_list = list()
        block_break = list()

        self.highlighted = None
        self.breaking_block = None
        self.selected_block = None
        self.jumping = False
        self.crouching = False
        self.holding_walk = False
        self.holding_jump = False
        self.sprinting = False
        self.flying = False
        self.placing = False
        self.breaking = False
        self.sprint_delay = 0
        self.place_delay = 0
        self.break_delay = 0
        self.fly_delay = 0
        self.air_velocity = 0
        self.fps = 0
        self.lastX, self.lastY = self.width / 2, self.height / 2

        glClearColor(135.0 / 255.0, 206.0 / 255.0, 235.0 / 255.0, 0.0)
        glClearDepth(1.0)  # may be optional
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        shader = self.compile_shader("generic_vertex_shader.vsh", "generic_fragment_shader.fsh")

        self.char_10 = TextManager(self, 10)
        self.char_4 = TextManager(self, 4)
        self.char_3 = TextManager(self, 3)
        self.char_2 = TextManager(self, 2)

        self.char_10.add_text("F.I. World", [430.0, 120.0, -0.4])
        self.vao_2d_dict["new_game_button_outline"] = VAOManager(
            BUTTON_OUTLINE, QUAD_INDICES, QUAD_INDICES, "textures/normal_button_outline.png", [[440.0, 290.0, -0.3]]
        )
        self.vao_2d_dict["quit_button_outline"] = VAOManager(
            BUTTON_OUTLINE, QUAD_INDICES, QUAD_INDICES, "textures/normal_button_outline.png", [[440.0, 340.0, -0.3]]
        )
        self.char_3.add_text("New Game", [565.0, 300.0, -0.3])
        self.char_3.add_text("Quit", [610.0, 350.0, -0.3])
        self.char_2.add_text(f"{self.fps}", [1240.0, 20.0, -0.4])
        for stage in range(10):
            block_break.append(self.load_texture(f"textures/destroy_stage_{stage}.png"))
        for block in os.listdir("./textures/blocks"):
            self.vao_3d_dict[f"textures/blocks/{block}"] = VAOManager(
                CUBE, CUBE_INDICES, CUBE_INDICES_EDGES, f"textures/blocks/{block}", []
            )
            self.block_list.append(f"textures/blocks/{block}")
        for x in range(-self.chunks, self.chunks):
            for z in range(-self.chunks, self.chunks):
                self.chunk_dict[(x * 16, -1, z * 16)] = ChunkManager((x, z), self, (x * 16, -1, z * 16))
        self.vao_2d_dict["crosshair_v"] = VAOManager(
            CROSSHAIR_V, QUAD_INDICES, QUAD_INDICES, "textures/white.png", [[624.0, 344.0, -0.6]]
        )
        self.vao_2d_dict["crosshair_h"] = VAOManager(
            CROSSHAIR_H, QUAD_INDICES, QUAD_INDICES, "textures/white.png", [[624.0, 344.0, -0.6]]
        )
        self.vao_2d_dict["hotbar"] = VAOManager(
            HOTBAR, QUAD_INDICES, QUAD_INDICES, "textures/hotbar.png", [[458.0, 676.0, -0.6]]
        )
        self.vao_2d_dict["active_bar"] = VAOManager(
            ACTIVE_BAR, QUAD_INDICES, QUAD_INDICES, "textures/active_bar.png", [[456.0, 674.0, -0.5]]
        )
        for i in range(1, 10):
            self.vao_2d_dict[f"hotbar_{i}"] = VAOManager(
                HOTBAR_ICON, QUAD_INDICES, QUAD_INDICES, f"{self.block_list[i]}",
                [[424.0 + i * 40, 682.0, -0.5]]
            )
            self.vao_2d_dict[f"inventory_hotbar_slot_{i}"] = VAOManager(
                HOTBAR_ICON, QUAD_INDICES, QUAD_INDICES, f"{self.block_list[i]}",
                [[444.0 + i * 36, 430.0, -0.3]]
            )
        for i in range(11, len(self.block_list)):
            self.vao_2d_dict[f"inventory_slot_{i - 10}"] = VAOManager(
                HOTBAR_ICON, QUAD_INDICES, QUAD_INDICES, f"{self.block_list[i]}",
                [[480.0 + ((i - 11) % 9) * 36, 314.0 + int((i - 11) / 9) * 36, -0.3]]
            )
        self.selected_block = self.vao_2d_dict["hotbar_1"].texture_name
        self.vao_2d_dict["inventory"] = VAOManager(
            INVENTORY, QUAD_INDICES, QUAD_INDICES, "textures/crafting_table.png", [[464.0, 146.0, -0.3]]
        )
        self.vao_2d_dict["active_inventory_slot"] = VAOManager(
            HOTBAR_ICON, QUAD_INDICES, QUAD_INDICES, "textures/white_tp.png", []
        )
        self.vao_2d_dict["paused"] = VAOManager(
            SCREEN, QUAD_INDICES, QUAD_INDICES, "textures/black_tp.png", [[0.0, 0.0, -0.4]]
        )
        self.vao_2d_dict["mouse_inventory"] = VAOManager(
            HOTBAR_ICON, QUAD_INDICES, QUAD_INDICES, "textures/tp.png", []
        )

        cube_model = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, -1.62, 0.0]))
        model_2d = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, 0.0]))
        proj = pyrr.matrix44.create_perspective_projection_matrix(90.0, self.width / self.height, 0.01, 100.0)
        proj_2d = pyrr.matrix44.create_orthogonal_projection_matrix(0, self.width, self.height, 0, 0.01, 100.0)
        model_loc = glGetUniformLocation(shader, "model")
        view_loc = glGetUniformLocation(shader, "view")
        proj_loc = glGetUniformLocation(shader, "proj")
        glUseProgram(shader)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    for vao in [*self.vao_3d_dict.values(), *self.vao_2d_dict.values()]:
                        glDeleteVertexArrays(1, vao.vao)
                        glDeleteBuffers(5, [vao.data_vbo, vao.instance_vbo, vao.highlighted_vbo, vao.ebo, vao.ebo_edge])
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    self.key_callback(event.key)
                    if self.new_game:
                        self.cam.camera_pos = pyrr.Vector3([0.0, 32, 0.0])
                        self.char_2.clear()
                        self.char_4.clear()
                        self.char_10.clear()
                        self.char_2.add_text(f"{self.fps}", [1240.0, 20.0, -0.4])
                        pygame.mouse.set_visible(False)
                        self.mouse_visibility = False
                        self.in_game = True
                        self.new_game = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_button_callback(event.button)
                elif event.type == pygame.MOUSEMOTION:
                    self.mouse_motion_callback(*event.pos)
                elif event.type == pygame.VIDEORESIZE:
                    self.width, self.height = event.w, event.h
                    glViewport(0, 0, event.w, event.h)

            old_fps = self.fps
            glClearColor(135.0 / 255.0, 206.0 / 255.0, 235.0 / 255.0, 1.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            view = self.cam.get_view_matrix()

            self.mouse_button_check()
            if self.in_game:
                if self.new_game:
                    self.game_init()
                    pygame.event.clear()
                if not self.paused:  # implement ray casting
                    self.do_movement()
                    view = self.cam.get_view_matrix()
                    mx, my = pygame.mouse.get_pos()
                    ray_nds = pyrr.Vector3([(2.0 * mx) / self.width - 1.0, 1.0 - (2.0 * my) / self.height, 1.0])
                    ray_clip = pyrr.Vector4([*ray_nds.xy, -1.0, 1.0])
                    ray_eye = pyrr.Vector4(numpy.dot(numpy.linalg.inv(proj), ray_clip))
                    ray_eye = pyrr.Vector4([*ray_eye.xy, -1.0, 0.0])
                    ray_wor = (numpy.linalg.inv(view) * ray_eye).xyz
                    self.ray_wor = pyrr.vector.normalise(ray_wor)
                    for i in numpy.arange(1, 4, 0.01):
                        ray_cam = self.cam.camera_pos + self.ray_wor * i
                        ray_cam.y += 1.62
                        self.ray_cam = ray_cam
                        self.ray_i = i
                        ray_cam.x, ray_cam.y, ray_cam.z = int(self.check_value(ray_cam.x, 0)), \
                            int(self.check_value(ray_cam.y, 0)), int(self.check_value(ray_cam.z, 0))
                        ray_cam = [int(axis) for axis in ray_cam]
                        if tuple(ray_cam) in self.visible_blocks:
                            self.highlighted = numpy.array(ray_cam, dtype=numpy.float32)
                            break
                    if self.highlighted is not None and list(self.highlighted) != ray_cam:
                        self.highlighted = None
                if self.in_inventory:
                    mx, my = pygame.mouse.get_pos()
                    self.vao_2d_dict["mouse_inventory"].vao_update(numpy.array(
                        [[mx * (1280 / self.width), my * (720 / self.height), -0.1]], dtype=numpy.float32
                    ))

            glUniformMatrix4fv(model_loc, 1, GL_FALSE, cube_model)
            glUniformMatrix4fv(proj_loc, 1, GL_FALSE, proj)
            glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)
            for vao in self.vao_3d_dict:
                if len(self.vao_3d_dict[vao].instances) > 0:
                    glBindVertexArray(self.vao_3d_dict[vao].vao)
                    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
                    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.vao_3d_dict[vao].ebo)
                    glBindTexture(GL_TEXTURE_2D, self.vao_3d_dict[vao].texture)
                    glBindBuffer(GL_ARRAY_BUFFER, self.vao_3d_dict[vao].data_vbo)
                    glBufferData(GL_ARRAY_BUFFER,
                                 self.vao_3d_dict[vao].vbo_data.itemsize * len(self.vao_3d_dict[vao].vbo_data),
                                 self.vao_3d_dict[vao].vbo_data, GL_STATIC_DRAW)
                    glBindBuffer(GL_ARRAY_BUFFER, self.vao_3d_dict[vao].instance_vbo)
                    glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
                    glEnableVertexAttribArray(2)
                    glVertexAttribDivisor(2, 1)
                    glDrawElementsInstanced(GL_TRIANGLES, len(CUBE_INDICES),
                                            GL_UNSIGNED_INT, None, int(len(self.vao_3d_dict[vao].instances)))
                    if self.highlighted is not None and self.visible_blocks[tuple(self.highlighted)] == vao:
                        if self.breaking:
                            if self.break_delay >= 0:
                                glBindTexture(GL_TEXTURE_2D, block_break[
                                    int(-(self.break_delay - (0.5 - (0.5 / 10))) / (0.5 / 10))
                                ])
                            else:
                                glBindTexture(GL_TEXTURE_2D, block_break[int((0.5 - (0.5 / 10)) / (0.5 / 10))])
                        glBindBuffer(GL_ARRAY_BUFFER, self.vao_3d_dict[vao].data_vbo)
                        glBufferData(GL_ARRAY_BUFFER, HIGHLIGHTED_CUBE.itemsize * len(HIGHLIGHTED_CUBE),
                                     HIGHLIGHTED_CUBE, GL_STATIC_DRAW)
                        glBindBuffer(GL_ARRAY_BUFFER, self.vao_3d_dict[vao].highlighted_vbo)
                        glBufferData(GL_ARRAY_BUFFER, self.highlighted.itemsize * len(self.highlighted.flatten()),
                                     self.highlighted.flatten(), GL_STATIC_DRAW)
                        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
                        glEnableVertexAttribArray(2)
                        glVertexAttribDivisor(2, 1)
                        if self.breaking:
                            glDrawElementsInstanced(GL_TRIANGLES, len(CUBE_INDICES),
                                                    GL_UNSIGNED_INT, None, int(len(self.highlighted)) - 2)
                        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
                        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.vao_3d_dict[vao].ebo_edge)
                        glBindTexture(GL_TEXTURE_2D, 0)
                        glLineWidth(4)  # todo figure out how large the outlines need to be for highlighted blocks
                        glDrawElementsInstanced(GL_QUADS, len(CUBE_INDICES_EDGES),
                                                GL_UNSIGNED_INT, None, int(len(self.highlighted)) - 2)
                    glBindVertexArray(0)

            glUniformMatrix4fv(model_loc, 1, GL_FALSE, model_2d)
            glUniformMatrix4fv(proj_loc, 1, GL_FALSE, proj_2d)
            glUniformMatrix4fv(view_loc, 1, GL_FALSE, model_2d)
            for vao in self.vao_2d_dict:
                if len(self.vao_2d_dict[vao].instances) > 0:
                    if ("inventory" in vao and self.in_inventory) or (vao == "paused" and self.paused) or \
                            ("button" in vao and self.in_menu) or ("character_3" in vao and self.in_menu) or \
                            ("bar" in vao and self.in_game and "inventory" not in vao) or \
                            ("cross" in vao and self.in_game) or \
                            ("inventory" not in vao and vao != "paused" and "button" not in vao and
                             "character_3" not in vao and "bar" not in vao and "cross" not in vao):
                        glBindVertexArray(self.vao_2d_dict[vao].vao)
                        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)  # is here only if the last 3d block is highlighted
                        glBindTexture(GL_TEXTURE_2D, self.vao_2d_dict[vao].texture)
                        glDrawElementsInstanced(GL_TRIANGLES, len(QUAD_INDICES),
                                                GL_UNSIGNED_INT, None, int(len(self.vao_2d_dict[vao].instances)))
                        glBindVertexArray(0)

            self.fps = round(self.clock.get_fps())
            self.char_2.remove_text(f"{old_fps}", [1240.0, 20.0, -0.4])
            self.char_2.add_text(f"{self.fps}", [1240.0, 20.0, -0.4])
            pygame.display.flip()
            self.clock.tick(60)

    def game_init(self):
        self.in_menu = False
        self.in_game = False
        if "return_button_outline" not in self.vao_2d_dict:
            self.vao_2d_dict["return_button_outline"] = VAOManager(
                BUTTON_OUTLINE, QUAD_INDICES, QUAD_INDICES, "textures/normal_button_outline.png", [[440.0, 240.0, -0.3]]
            )
            self.char_3.add_text("Return to Game", [520.0, 250.0, -0.3])
        self.char_4.add_text("Controls:", [200.0, 280.0, -0.4])
        self.char_2.add_text("* W - Walk forwards", [220.0, 340.0 - 10.0, -0.4])
        self.char_2.add_text("* A - Walk backwards", [220.0, 360.0 - 10.0, -0.4])
        self.char_2.add_text("* S - Walk to the left", [220.0, 380.0 - 10.0, -0.4])
        self.char_2.add_text("* D - Walk to the right", [220.0, 400.0 - 10.0, -0.4])
        self.char_2.add_text("* Left Mouse Button - Break the highlighted block", [220.0, 420.0 - 10.0, -0.4])
        self.char_2.add_text("* Right Mouse Button - Place at side of highlighted block",
                             [220.0, 440.0 - 10.0, -0.4])
        self.char_2.add_text("* Space - Jump", [220.0, 460.0 - 10.0, -0.4])
        self.char_2.add_text("* Shift - Crouch", [220.0, 480.0 - 10.0, -0.4])
        self.char_2.add_text("* 1 to 9 - Switch which slot is active in the hotbar or action bar",
                             [220.0, 500.0 - 10.0, -0.4])
        self.char_2.add_text("* E - Access inventory", [220.0, 520.0 - 10.0, -0.4])
        self.char_2.add_text("* Esc - Pause game and open menu", [220.0, 540.0 - 10.0, -0.4])
        self.char_2.add_text("* P - Respawn at starting position", [220.0, 560.0 - 10.0, -0.4])
        self.char_4.add_text("Loading...", [548.0, 600.0, -0.4])
        for vao in self.vao_2d_dict:
            if ("inventory" in vao and self.in_inventory) or (vao == "paused" and self.paused) or \
                    ("button" in vao and self.in_menu) or ("character_3" in vao and self.in_menu) or \
                    ("bar" in vao and self.in_game and "inventory" not in vao) or ("cross" in vao and self.in_game) or \
                    ("inventory" not in vao and vao != "paused" and "button" not in vao and "character_3" not in vao and
                     "bar" not in vao and "cross" not in vao):
                glBindVertexArray(self.vao_2d_dict[vao].vao)
                glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)  # is here only if the last 3d block is highlighted
                glBindTexture(GL_TEXTURE_2D, self.vao_2d_dict[vao].texture)
                glDrawElementsInstanced(GL_TRIANGLES, len(QUAD_INDICES),
                                        GL_UNSIGNED_INT, None, int(len(self.vao_2d_dict[vao].instances)))
                glBindVertexArray(0)
        pygame.display.flip()
        self.world_instances.clear()
        self.visible_blocks.clear()
        self.highlighted = None
        self.jumping = False
        self.crouching = False
        self.air_velocity = 0
        for vao in self.vao_3d_dict:
            self.vao_3d_dict[vao].vao_update([])
        for chunk in self.chunk_dict.values():
            chunk.chunk_init()
        for vao in self.vao_3d_dict:
            for pos in self.vao_3d_dict[vao].instances:
                self.world_instances[tuple(pos)] = vao
        for pos in self.world_instances:
            px, py, pz = pos
            if not ((px + 1, py, pz) in self.world_instances and (px, py + 1, pz) in self.world_instances and
                    (px, py, pz + 1) in self.world_instances and (px - 1, py, pz) in self.world_instances and
                    (px, py - 1, pz) in self.world_instances and (px, py, pz - 1) in self.world_instances):
                self.visible_blocks[pos] = self.world_instances[pos]
        for vao in self.vao_3d_dict:
            if vao in self.visible_blocks.values():
                self.vao_3d_dict[vao].instances = numpy.array([], dtype=numpy.float32)
                for pos in self.visible_blocks:
                    if self.visible_blocks[pos] == vao:
                        if len(self.vao_3d_dict[vao].instances) > 0:
                            self.vao_3d_dict[vao].instances = numpy.append(
                                self.vao_3d_dict[vao].instances, numpy.array([pos], dtype=numpy.float32), 0
                            )
                        else:
                            self.vao_3d_dict[vao].instances = numpy.array([pos], dtype=numpy.float32)
                self.vao_3d_dict[vao].vao_update()
        self.char_4.remove_text("Loading...", [548.0, 600.0, -0.4])
        self.char_4.add_text("Press any key to continue", [380.0, 600.0, -0.4])

    def do_movement(self):
        keys = pygame.key.get_pressed()
        mods = pygame.key.get_mods()
        time_s = self.clock.get_time() / 1000
        net_movement = 4.317 * time_s
        x, y, z = self.cam.camera_pos
        x, y, z = self.check_value(x, 0.3), numpy.ceil(self.check_value(y, 0)), self.check_value(z, 0.3)
        if keys[pygame.K_w]:
            if self.sprint_delay > 0 and not self.holding_walk:
                self.sprinting = True
            elif self.sprint_delay == 0 and not self.holding_walk:
                self.sprint_delay = 0.25
            self.holding_walk = True
            if self.flying:
                if self.sprinting:
                    self.cam.process_keyboard("FRONT", net_movement * 5.0)
                else:
                    self.cam.process_keyboard("FRONT", net_movement * 2.5)
            elif self.crouching:
                self.cam.process_keyboard("FRONT", net_movement * 0.3)
            else:
                if self.sprinting:
                    self.cam.process_keyboard("FRONT", net_movement * 1.3)
                else:
                    self.cam.process_keyboard("FRONT", net_movement)
        else:
            self.holding_walk = False
            self.sprinting = False
        if keys[pygame.K_a]:
            if self.flying:
                self.cam.process_keyboard("SIDE", -net_movement * 2.5)
            elif self.crouching:
                self.cam.process_keyboard("SIDE", -net_movement * 0.3)
            else:
                self.cam.process_keyboard("SIDE", -net_movement)
        if keys[pygame.K_s]:
            if self.flying:
                self.cam.process_keyboard("FRONT", -net_movement * 2.5)
            elif self.crouching:
                self.cam.process_keyboard("FRONT", -net_movement * 0.3)
            else:
                self.cam.process_keyboard("FRONT", -net_movement)
        if keys[pygame.K_d]:
            if self.flying:
                self.cam.process_keyboard("SIDE", net_movement * 2.5)
            elif self.crouching:
                self.cam.process_keyboard("SIDE", net_movement * 0.3)
            else:
                self.cam.process_keyboard("SIDE", net_movement)
        if keys[pygame.K_SPACE]:
            if self.fly_delay > 0 and not self.holding_jump:
                self.flying = not self.flying
                self.air_velocity = 0
                self.jumping = False
            elif self.fly_delay == 0 and not self.holding_jump:
                self.fly_delay = 0.25
            self.holding_jump = True
            if not self.jumping and not self.flying and \
                    ((int(x + 0.3), int(y - 1), int(z + 0.3)) in self.visible_blocks or
                     (int(x + 0.3), int(y - 1), int(z - 0.3)) in self.visible_blocks or
                     (int(x - 0.3), int(y - 1), int(z + 0.3)) in self.visible_blocks or
                     (int(x - 0.3), int(y - 1), int(z - 0.3)) in self.visible_blocks):
                self.air_velocity = 8.95142 * time_s
                self.cam.process_keyboard("UP", self.air_velocity)
                self.jumping = True
            if self.flying:
                self.cam.process_keyboard("UP", net_movement * 2)
        else:
            self.holding_jump = False
        if mods & pygame.KMOD_SHIFT:
            if not self.crouching:
                self.cam.camera_pos[1] -= 0.125
                self.crouching = True
            if self.flying:
                self.cam.process_keyboard("UP", -net_movement * 2)
        elif self.crouching:
            self.cam.camera_pos[1] += 0.125
            self.crouching = False
        cx, cy, cz = self.cam.camera_pos
        if self.crouching:
            cy += 0.125
        cx, cy, cz = self.check_value(cx, 0.3), self.check_value(cy, 0), self.check_value(cz, 0.3)
        if (int(cx + 0.3), int(numpy.ceil(cy - 1)), int(cz + 0.3)) not in self.visible_blocks and \
                (int(cx + 0.3), int(numpy.ceil(cy - 1)), int(cz - 0.3)) not in self.visible_blocks and \
                (int(cx - 0.3), int(numpy.ceil(cy - 1)), int(cz + 0.3)) not in self.visible_blocks and \
                (int(cx - 0.3), int(numpy.ceil(cy - 1)), int(cz - 0.3)) not in self.visible_blocks and not self.flying:
            self.air_velocity -= 32 * time_s ** 2
            if (int(cx + 0.3), int(numpy.ceil(cy + self.air_velocity - 1)), int(cz + 0.3)) \
                    not in self.visible_blocks and \
                    (int(cx + 0.3), int(numpy.ceil(cy + self.air_velocity - 1)), int(cz - 0.3)) \
                    not in self.visible_blocks and \
                    (int(cx - 0.3), int(numpy.ceil(cy + self.air_velocity - 1)), int(cz + 0.3)) \
                    not in self.visible_blocks and \
                    (int(cx - 0.3), int(numpy.ceil(cy + self.air_velocity - 1)), int(cz - 0.3)) \
                    not in self.visible_blocks:
                if (int(cx + 0.3), int(numpy.ceil(cy + 1.85 + self.air_velocity - 1)), int(cz + 0.3)) \
                        not in self.visible_blocks and \
                        (int(cx + 0.3), int(numpy.ceil(cy + 1.85 + self.air_velocity - 1)), int(cz - 0.3)) \
                        not in self.visible_blocks and \
                        (int(cx - 0.3), int(numpy.ceil(cy + 1.85 + self.air_velocity - 1)), int(cz + 0.3)) \
                        not in self.visible_blocks and \
                        (int(cx - 0.3), int(numpy.ceil(cy + 1.85 + self.air_velocity - 1)), int(cz - 0.3)) \
                        not in self.visible_blocks:
                    self.cam.process_keyboard("UP", self.air_velocity)
                else:
                    if not self.crouching:
                        self.cam.camera_pos[1] = int(self.cam.camera_pos[1]) + 0.15
                    else:
                        self.cam.camera_pos[1] = int(self.cam.camera_pos[1]) + 0.025
                    self.air_velocity = 0
                    self.jumping = False
                    self.flying = False
            else:
                if not self.crouching:
                    self.cam.camera_pos[1] = round(self.cam.camera_pos[1])
                else:
                    self.cam.camera_pos[1] = round(self.cam.camera_pos[1]) - 0.125
                self.air_velocity = 0
                self.jumping = False
                self.flying = False
        elif not ((int(cx + 0.3), int(numpy.ceil(cy - 1)), int(cz + 0.3)) not in self.visible_blocks and
                  (int(cx + 0.3), int(numpy.ceil(cy - 1)), int(cz - 0.3)) not in self.visible_blocks and
                  (int(cx - 0.3), int(numpy.ceil(cy - 1)), int(cz + 0.3)) not in self.visible_blocks and
                  (int(cx - 0.3), int(numpy.ceil(cy - 1)), int(cz - 0.3)) not in self.visible_blocks):
            if not self.crouching:
                self.cam.camera_pos[1] = round(self.cam.camera_pos[1])
            else:
                self.cam.camera_pos[1] = round(self.cam.camera_pos[1]) - 0.125
            self.air_velocity = 0
            self.jumping = False
            self.flying = False
        elif not ((int(cx + 0.3), int(numpy.ceil(cy + 1.85 + self.air_velocity - 1)), int(cz + 0.3))
                  not in self.visible_blocks and
                  (int(cx + 0.3), int(numpy.ceil(cy + 1.85 + self.air_velocity - 1)), int(cz - 0.3))
                  not in self.visible_blocks and
                  (int(cx - 0.3), int(numpy.ceil(cy + 1.85 + self.air_velocity - 1)), int(cz + 0.3))
                  not in self.visible_blocks and
                  (int(cx - 0.3), int(numpy.ceil(cy + 1.85 + self.air_velocity - 1)), int(cz - 0.3))
                  not in self.visible_blocks):
            if not self.crouching:
                self.cam.camera_pos[1] = int(self.cam.camera_pos[1]) + 0.149
            else:
                self.cam.camera_pos[1] = int(self.cam.camera_pos[1]) + 0.024
        if self.sprint_delay > 0:
            self.sprint_delay -= time_s
        else:
            self.sprint_delay = 0
        if self.fly_delay > 0:
            self.fly_delay -= time_s
        else:
            self.fly_delay = 0
        if self.cam.camera_pos[1] < -64 and self.in_game:
            self.cam.camera_pos = pyrr.Vector3([0.0, 32, 0.0])

    def mouse_button_check(self):
        mouse_buttons = pygame.mouse.get_pressed()
        time_s = self.clock.get_time() / 1000
        if self.breaking and (self.highlighted is None or self.breaking_block.tolist() != self.highlighted.tolist()):
            self.break_delay = 0.5
            self.breaking_block = self.highlighted
        if mouse_buttons[0]:
            if not self.mouse_visibility and self.highlighted is not None:
                if self.break_delay <= 0 and not self.breaking:
                    self.break_delay = 0.5
                    self.breaking = True
                    self.breaking_block = self.highlighted
                if self.break_delay <= 0 and self.breaking and \
                        self.visible_blocks[tuple(self.highlighted)] != "textures/blocks/bedrock.png":
                    px, py, pz = self.highlighted
                    px, py, pz = int(px), int(py), int(pz)
                    self.highlighted = tuple(self.highlighted)
                    self.vao_3d_dict[self.visible_blocks[self.highlighted]].instances = numpy.delete(
                        self.vao_3d_dict[self.visible_blocks[self.highlighted]].instances,
                        numpy.where((self.vao_3d_dict[self.visible_blocks[self.highlighted]].instances[:, 0] ==
                                     self.highlighted[0]) &
                                    (self.vao_3d_dict[self.visible_blocks[self.highlighted]].instances[:, 1] ==
                                     self.highlighted[1]) &
                                    (self.vao_3d_dict[self.visible_blocks[self.highlighted]].instances[:, 2] ==
                                     self.highlighted[2])), 0
                    )
                    self.vao_3d_dict[self.visible_blocks[self.highlighted]].vao_update()
                    del self.visible_blocks[self.highlighted]
                    del self.world_instances[self.highlighted]
                    for x, y, z in ((px + 1, py, pz), (px, py + 1, pz), (px, py, pz + 1),
                                    (px - 1, py, pz), (px, py - 1, pz), (px, py, pz - 1)):
                        if (x, y, z) not in self.visible_blocks and (x, y, z) in self.world_instances:
                            self.visible_blocks[(x, y, z)] = self.world_instances[(x, y, z)]
                            self.vao_3d_dict[self.world_instances[(x, y, z)]].instances = numpy.append(
                                self.vao_3d_dict[self.world_instances[(x, y, z)]].instances,
                                numpy.array([[x, y, z]], dtype=numpy.float32), 0
                            )
                            self.vao_3d_dict[self.world_instances[(x, y, z)]].vao_update()
                    self.highlighted = None
                    self.breaking_block = None
                    self.breaking = False
            else:
                self.break_delay = 0
                self.breaking = False
        else:
            self.break_delay = 0
            self.breaking = False
        if mouse_buttons[2]:
            if self.highlighted is not None and self.place_delay <= 0:
                self.place_delay += 0.25
                new_block = self.block_face()
                x, y, z = self.cam.camera_pos
                if self.crouching:
                    y += 0.125
                x, y, z = self.check_value(x, 0.3), self.check_value(y, 0), self.check_value(z, 0.3)
                player_hitbox = ((x, y, z), (x, y + 1, z), (x, y + 2, z),
                                 (int(x + 0.3), int(y), int(z + 0.3)),
                                 (int(x + 0.3), int(y), int(z - 0.3)),
                                 (int(x - 0.3), int(y), int(z + 0.3)),
                                 (int(x - 0.3), int(y), int(z - 0.3)),
                                 (int(x + 0.3), int(y + 1), int(z + 0.3)),
                                 (int(x + 0.3), int(y + 1), int(z - 0.3)),
                                 (int(x - 0.3), int(y + 1), int(z + 0.3)),
                                 (int(x - 0.3), int(y + 1), int(z - 0.3)),
                                 (int(x + 0.3), int(y + 1.85), int(z + 0.3)),
                                 (int(x + 0.3), int(y + 1.85), int(z - 0.3)),
                                 (int(x - 0.3), int(y + 1.85), int(z + 0.3)),
                                 (int(x - 0.3), int(y + 1.85), int(z - 0.3)))
                if new_block not in self.world_instances and new_block not in player_hitbox and \
                        "textures/blocks" in self.selected_block:
                    hx, hy, hz = self.highlighted
                    i = 0
                    for x, y, z in ((hx + 1, hy, hz), (hx, hy + 1, hz), (hx, hy, hz + 1),
                                    (hx - 1, hy, hz), (hx, hy - 1, hz), (hx, hy, hz - 1)):
                        if (x, y, z) in self.world_instances:
                            i += 1
                            # todo fix following code to be less resource intensive
                            if (x, y, z) in self.visible_blocks:
                                i2 = 0
                                for x2, y2, z2 in ((x + 1, y, z), (x, y + 1, z), (x, y, z + 1),
                                                   (x - 1, y, z), (x, y - 1, z), (x, y, z - 1)):
                                    if (x2, y2, z2) in self.world_instances and \
                                            "glass" not in self.world_instances[(x2, y2, z2)] and \
                                            "ice" not in self.world_instances[(x2, y2, z2)]:
                                        i2 += 1
                                if i2 >= 6:
                                    self.vao_3d_dict[self.visible_blocks[(x, y, z)]].instances = numpy.delete(
                                        self.vao_3d_dict[self.visible_blocks[(x, y, z)]].instances,
                                        numpy.where(
                                            (self.vao_3d_dict[self.visible_blocks[(x, y, z)]].instances[:, 0] == x) &
                                            (self.vao_3d_dict[self.visible_blocks[(x, y, z)]].instances[:, 1] == y) &
                                            (self.vao_3d_dict[self.visible_blocks[(x, y, z)]].instances[:, 2] == z)
                                        ), 0
                                    )
                                    self.vao_3d_dict[self.visible_blocks[(x, y, z)]].vao_update()
                                    del self.visible_blocks[(x, y, z)]
                    if i >= 6:
                        self.highlighted = tuple(self.highlighted)
                        self.vao_3d_dict[self.visible_blocks[self.highlighted]].instances = numpy.delete(
                            self.vao_3d_dict[self.visible_blocks[self.highlighted]].instances,
                            numpy.where((self.vao_3d_dict[self.visible_blocks[self.highlighted]].instances[:, 0] ==
                                         self.highlighted[0]) &
                                        (self.vao_3d_dict[self.visible_blocks[self.highlighted]].instances[:, 1] ==
                                         self.highlighted[1]) &
                                        (self.vao_3d_dict[self.visible_blocks[self.highlighted]].instances[:, 2] ==
                                         self.highlighted[2])), 0
                        )
                        self.vao_3d_dict[self.visible_blocks[self.highlighted]].vao_update()
                        del self.visible_blocks[self.highlighted]
                        self.highlighted = None
                    self.world_instances[new_block] = self.selected_block
                    self.visible_blocks[new_block] = self.selected_block
                    if len(self.vao_3d_dict[self.selected_block].instances) > 0:
                        self.vao_3d_dict[self.selected_block].instances = numpy.append(
                            self.vao_3d_dict[self.selected_block].instances,
                            numpy.array([new_block], dtype=numpy.float32), 0
                        )
                    else:
                        self.vao_3d_dict[self.selected_block].instances = numpy.array([new_block], dtype=numpy.float32)
                    self.vao_3d_dict[self.selected_block].vao_update()
        else:
            self.place_delay = 0
        if self.place_delay > 0:
            self.place_delay -= time_s
        if self.break_delay > 0:
            self.break_delay -= time_s

    def mouse_motion_callback(self, x_pos, y_pos):
        if not self.mouse_visibility:
            x_offset = x_pos - self.width / 2
            y_offset = self.height / 2 - y_pos

            self.cam.process_mouse_movement(x_offset, y_offset)
            pygame.mouse.set_pos(self.width / 2, self.height / 2)
        elif self.mouse_visibility:
            if self.in_menu:
                if "return_button_outline" in self.vao_2d_dict:
                    if (440 / 1280) * self.width < x_pos < ((440 + 400) / 1280) * self.width and \
                            (240 / 720) * self.height < y_pos < ((240 + 40) / 720) * self.height:
                        if self.vao_2d_dict["return_button_outline"].texture_name != \
                                "textures/highlighted_button_outline.png":
                            self.vao_2d_dict["return_button_outline"].texture_name = \
                                "textures/highlighted_button_outline.png"
                            self.vao_2d_dict["return_button_outline"].texture = \
                                self.load_texture("textures/highlighted_button_outline.png")
                    elif self.vao_2d_dict["return_button_outline"].texture_name != "textures/normal_button_outline.png":
                        self.vao_2d_dict["return_button_outline"].texture_name = "textures/normal_button_outline.png"
                        self.vao_2d_dict["return_button_outline"].texture = \
                            self.load_texture("textures/normal_button_outline.png")
                if (440 / 1280) * self.width < x_pos < ((440 + 400) / 1280) * self.width and \
                        (290 / 720) * self.height < y_pos < ((290 + 40) / 720) * self.height:
                    if self.vao_2d_dict["new_game_button_outline"].texture_name != \
                            "textures/highlighted_button_outline.png":
                        self.vao_2d_dict["new_game_button_outline"].texture_name = \
                            "textures/highlighted_button_outline.png"
                        self.vao_2d_dict["new_game_button_outline"].texture = \
                            self.load_texture("textures/highlighted_button_outline.png")
                elif self.vao_2d_dict["new_game_button_outline"].texture_name != "textures/normal_button_outline.png":
                    self.vao_2d_dict["new_game_button_outline"].texture_name = "textures/normal_button_outline.png"
                    self.vao_2d_dict["new_game_button_outline"].texture = \
                        self.load_texture("textures/normal_button_outline.png")
                if (440 / 1280) * self.width < x_pos < ((440 + 400) / 1280) * self.width and \
                        (340 / 720) * self.height < y_pos < ((340 + 40) / 720) * self.height:
                    if self.vao_2d_dict["quit_button_outline"].texture_name != \
                            "textures/highlighted_button_outline.png":
                        self.vao_2d_dict["quit_button_outline"].texture_name = "textures/highlighted_button_outline.png"
                        self.vao_2d_dict["quit_button_outline"].texture = \
                            self.load_texture("textures/highlighted_button_outline.png")
                elif self.vao_2d_dict["quit_button_outline"].texture_name != "textures/normal_button_outline.png":
                    self.vao_2d_dict["quit_button_outline"].texture_name = "textures/normal_button_outline.png"
                    self.vao_2d_dict["quit_button_outline"].texture = \
                        self.load_texture("textures/normal_button_outline.png")
            if self.in_inventory:
                for vao in self.vao_2d_dict:
                    if "slot" in vao and "inventory" in vao and "active" not in vao:
                        instance = tuple(self.vao_2d_dict[vao].instances[0])
                        if (int(instance[0]) / 1280) * self.width < x_pos < ((int(instance[0]) + 32) / 1280) * \
                                self.width and (int(instance[1]) / 720) * self.height < y_pos < \
                                ((int(instance[1]) + 32) / 720) * self.height:
                            self.vao_2d_dict["active_inventory_slot"].vao_update(numpy.array(
                                [[int(instance[0]), int(instance[1]), -0.2]], dtype=numpy.float32
                            ))
                            break
                        else:
                            self.vao_2d_dict["active_inventory_slot"].vao_update(numpy.array([], dtype=numpy.float32))

    def mouse_button_callback(self, button):
        mouse_pos = pygame.mouse.get_pos()
        if button == 1:
            if self.mouse_visibility:
                if self.in_menu:
                    if (440 / 1280) * self.width < mouse_pos[0] < ((440 + 400) / 1280) * self.width and \
                            (240 / 720) * self.height < mouse_pos[1] < ((240 + 40) / 720) * self.height:
                        pygame.mouse.set_visible(False)
                        self.mouse_visibility = False
                        pygame.mouse.set_pos(self.width / 2, self.height / 2)
                        self.paused = False
                        self.in_menu = False
                    elif (440 / 1280) * self.width < mouse_pos[0] < ((440 + 400) / 1280) * self.width and \
                            (290 / 720) * self.height < mouse_pos[1] < ((290 + 40) / 720) * self.height:
                        self.char_10.add_text("F.I. World", [430.0, 120.0, -0.4])
                        self.paused = False
                        self.in_game = True
                        self.new_game = True
                    elif (440 / 1280) * self.width < mouse_pos[0] < ((440 + 400) / 1280) * self.width and \
                            (340 / 720) * self.height < mouse_pos[1] < ((340 + 40) / 720) * self.height:
                        pygame.event.post(pygame.event.Event(pygame.QUIT, dict()))
                if self.in_inventory:
                    if not ((464 / 1280) * self.width < mouse_pos[0] < ((464 + 352) / 1280) * self.width and (146 / 720)
                            * self.height < mouse_pos[1] < ((146 + 332) / 720) * self.height):
                        pygame.mouse.set_pos(self.width / 2, self.height / 2)
                        pygame.mouse.set_visible(False)
                        self.mouse_visibility = False
                        self.paused = False
                        self.in_inventory = False
                    elif len(self.vao_2d_dict["active_inventory_slot"].instances) > 0:
                        instance = tuple(self.vao_2d_dict["active_inventory_slot"].instances[0])
                        if f"inventory_slot_{int(((int(instance[0]) - 444) / 36) + (int(instance[1]) - 314) / 4)}" in \
                                self.vao_2d_dict:
                            mouse_vao = \
                                f"inventory_slot_{int(((int(instance[0]) - 444) / 36) + (int(instance[1]) - 314) / 4)}"
                        elif f"inventory_hotbar_slot_{int(((int(instance[0]) - 444) / 36))}" in self.vao_2d_dict:
                            mouse_vao = f"inventory_hotbar_slot_{int(((int(instance[0]) - 444) / 36))}"
                        else:
                            mouse_vao = None
                        if mouse_vao is not None:
                            self.vao_2d_dict["mouse_inventory"].vao_update(numpy.array(
                                [[int(instance[0]), int(instance[1]), -0.3]], dtype=numpy.float32
                            ))
                            self.vao_2d_dict["mouse_inventory"].texture_name, \
                                self.vao_2d_dict[mouse_vao].texture_name = self.vao_2d_dict[mouse_vao].texture_name, \
                                self.vao_2d_dict["mouse_inventory"].texture_name
                            self.vao_2d_dict["mouse_inventory"].texture, self.vao_2d_dict[mouse_vao].texture = \
                                self.vao_2d_dict[mouse_vao].texture, self.vao_2d_dict["mouse_inventory"].texture
                            if "hotbar" in mouse_vao:
                                self.vao_2d_dict[f"hotbar_{mouse_vao[-1]}"].texture_name = \
                                    self.vao_2d_dict[mouse_vao].texture_name
                                self.vao_2d_dict[f"hotbar_{mouse_vao[-1]}"].texture = \
                                    self.vao_2d_dict[mouse_vao].texture
                                self.selected_block = self.vao_2d_dict[
                                    f"hotbar_{int((self.vao_2d_dict['active_bar'].instances[0][0] - 416.0) / 40.0)}"
                                ].texture_name
        elif button == 4:
            if not self.paused:
                new_hotbar = int((self.vao_2d_dict["active_bar"].instances[0][0] - 416.0) / 40.0 - 1.0)
                if new_hotbar < 1:
                    new_hotbar = 9
                self.selected_block = self.vao_2d_dict[f"hotbar_{new_hotbar}"].texture_name
                self.vao_2d_dict["active_bar"].instances = numpy.array(
                    [[new_hotbar * 40.0 + 416.0, 674.0, -0.5]], dtype=numpy.float32
                )
                self.vao_2d_dict["active_bar"].vao_update()
        elif button == 5:
            if not self.paused:
                new_hotbar = int((self.vao_2d_dict["active_bar"].instances[0][0] - 416.0) / 40.0 + 1.0)
                if new_hotbar > 9:
                    new_hotbar = 1
                self.selected_block = self.vao_2d_dict[f"hotbar_{new_hotbar}"].texture_name
                self.vao_2d_dict["active_bar"].instances = numpy.array(
                    [[new_hotbar * 40.0 + 416.0, 674.0, -0.5]], dtype=numpy.float32
                )
                self.vao_2d_dict["active_bar"].vao_update()

    def key_callback(self, key):
        if key == pygame.K_ESCAPE:
            if not self.mouse_visibility:
                pygame.mouse.set_visible(True)
                self.mouse_visibility = True
                pygame.mouse.set_pos(self.width / 2, self.height / 2)
                self.paused = True
                self.in_menu = True
            elif self.in_inventory:
                pygame.mouse.set_pos(self.width / 2, self.height / 2)
                pygame.mouse.set_visible(False)
                self.mouse_visibility = False
                self.in_inventory = False
                self.paused = False
            else:
                pygame.event.post(pygame.event.Event(pygame.QUIT, dict()))
        elif key == pygame.K_e:
            self.in_inventory = not self.in_inventory
            self.paused = not self.paused
            pygame.mouse.set_visible(not self.mouse_visibility)
            self.mouse_visibility = not self.mouse_visibility
            pygame.mouse.set_pos(self.width / 2, self.height / 2)
        elif key == pygame.K_p:
            self.cam.camera_pos = pyrr.Vector3([0.0, 32, 0.0])
        for i in range(1, 10):
            if key == getattr(pygame, f"K_{i}"):
                self.selected_block = self.vao_2d_dict[f"hotbar_{i}"].texture_name
                self.vao_2d_dict["active_bar"].instances = numpy.array(
                    [[416.0 + 40.0 * i, 674.0, -0.5]], dtype=numpy.float32
                )
                self.vao_2d_dict["active_bar"].vao_update()

    def block_face(self):
        x, y, z = self.cam.camera_pos + self.ray_wor * (self.ray_i - 0.01)
        y += 1.62
        x, y, z = int(self.check_value(x, 0)), int(self.check_value(y, 0)), int(self.check_value(z, 0))
        hx, hy, hz = self.highlighted
        if (x, y, z) in ((hx + 1, hy, hz), (hx, hy + 1, hz), (hx, hy, hz + 1),
                         (hx - 1, hy, hz), (hx, hy - 1, hz), (hx, hy, hz - 1)):
            return x, y, z
        else:
            return hx, hy, hz

    @staticmethod
    def compile_shader(vs, fs):
        vert_shader = App.load_shader(vs)
        frag_shader = App.load_shader(fs)

        shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vert_shader, GL_VERTEX_SHADER),
                                                  OpenGL.GL.shaders.compileShader(frag_shader, GL_FRAGMENT_SHADER))
        return shader

    @staticmethod
    def load_texture(path):
        texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture)
        # Set the texture wrapping parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        # Set texture filtering parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        if isinstance(path, str):
            # load image
            image = Image.open(path)
            width, height = image.width, image.height
            img_data = numpy.array(list(image.getdata()), numpy.uint8)
        else:
            cx, cy = path[1]
            image = path[0]
            orig_data = numpy.array(list(image.getdata()), numpy.uint8).reshape((image.height, image.width * 4))
            img_data = numpy.empty((8, path[2][0] * 4), dtype=numpy.uint8)
            for x in range(cx * 4, (cx + path[2][0]) * 4):
                for y in range(cy, cy + 8):
                    img_data[y - cy, x - (cx * 4)] = orig_data[y, x]
            width, height = path[2][0], 8
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
        return texture

    @staticmethod
    def load_shader(shader_file):
        with open(shader_file) as f:
            shader_source = f.read()
        f.close()
        return str.encode(shader_source)

    @staticmethod
    def check_value(value, limit):
        if value < limit:
            value -= 1
        return value


class Camera:
    def __init__(self, app):
        self.app = app
        self.camera_pos = pyrr.Vector3([0.0, -100.0, 0.0])
        self.camera_front = pyrr.Vector3([0.0, 0.0, -1.0])
        self.camera_up = pyrr.Vector3([0.0, 1.0, 0.0])
        self.camera_right = pyrr.Vector3([1.0, 0.0, 0.0])

        self.mouse_sensitivity = 0.125
        self.yaw = -90.0
        self.pitch = 0.0

    def get_view_matrix(self):
        return self.look_at(self.camera_pos, self.camera_pos + self.camera_front, self.camera_up)

    def process_keyboard(self, direction, velocity):
        if direction == "FRONT":
            self.camera_pos[0] += numpy.cos(numpy.radians(self.yaw)) * velocity
            self.check_pos(0, numpy.cos(numpy.radians(self.yaw)) * velocity)
            self.camera_pos[2] += numpy.sin(numpy.radians(self.yaw)) * velocity
            self.check_pos(2, numpy.sin(numpy.radians(self.yaw)) * velocity)
        elif direction == "SIDE":
            self.camera_pos[0] += numpy.cos(numpy.radians(self.yaw) + numpy.pi / 2) * velocity
            self.check_pos(0, numpy.cos(numpy.radians(self.yaw) + numpy.pi / 2) * velocity)
            self.camera_pos[2] += numpy.sin(numpy.radians(self.yaw) + numpy.pi / 2) * velocity
            self.check_pos(2, numpy.sin(numpy.radians(self.yaw) + numpy.pi / 2) * velocity)
        elif direction == "UP":
            self.camera_pos[1] += velocity

    def process_mouse_movement(self, x_offset, y_offset, constrain_pitch=True):
        x_offset *= self.mouse_sensitivity
        y_offset *= self.mouse_sensitivity

        self.yaw += x_offset
        self.pitch += y_offset

        if constrain_pitch:
            if self.pitch > 90.0:
                self.pitch = 90.0
            if self.pitch < -90.0:
                self.pitch = -90.0

        self.update_camera_vectors()

    def update_camera_vectors(self):
        front = pyrr.Vector3([0.0, 0.0, 0.0])
        front.x = numpy.cos(numpy.radians(self.yaw)) * numpy.cos(numpy.radians(self.pitch))
        front.y = numpy.sin(numpy.radians(self.pitch))
        front.z = numpy.sin(numpy.radians(self.yaw)) * numpy.cos(numpy.radians(self.pitch))

        self.camera_front = pyrr.vector.normalise(front)
        self.camera_right = pyrr.vector.normalise(pyrr.vector3.cross(self.camera_front, pyrr.Vector3([0.0, 1.0, 0.0])))
        self.camera_up = pyrr.vector.normalise(pyrr.vector3.cross(self.camera_right, self.camera_front))

    def check_pos(self, axis, distance):
        x, y, z = self.camera_pos
        if self.app.crouching:
            y += 0.125
        x, y, z = self.app.check_value(x, 0.3), self.app.check_value(y, 0), self.app.check_value(z, 0.3)
        crouch_counter = 0
        for i1, i2 in {(-.3, -.3), (-.3, .3), (.3, -.3), (.3, .3)}:
            ix, iy, iz = int(x + i1), y, int(z + i2)
            if (ix, int(iy), iz) in self.app.visible_blocks or (ix, int(iy + 1), iz) in self.app.visible_blocks or \
                    (ix, int(iy + 1.85), iz) in self.app.visible_blocks:
                self.camera_pos[axis] -= distance
                return
            elif self.app.crouching and not self.app.flying and not self.app.jumping \
                    and (ix, int(iy - 1), iz) not in self.app.visible_blocks:
                crouch_counter += 1
        if crouch_counter >= 4:
            self.camera_pos[axis] -= distance

    @staticmethod
    def look_at(position, target, world_up):
        z_axis = pyrr.vector.normalise(position - target)
        x_axis = pyrr.vector.normalise(pyrr.vector3.cross(pyrr.vector.normalise(world_up), z_axis))
        y_axis = pyrr.vector3.cross(z_axis, x_axis)

        translation = pyrr.Matrix44.identity()
        translation[3][0] = -position.x
        translation[3][1] = -position.y
        translation[3][2] = -position.z

        rotation = pyrr.Matrix44.identity()
        rotation[0][0] = x_axis[0]
        rotation[1][0] = x_axis[1]
        rotation[2][0] = x_axis[2]
        rotation[0][1] = y_axis[0]
        rotation[1][1] = y_axis[1]
        rotation[2][1] = y_axis[2]
        rotation[0][2] = z_axis[0]
        rotation[1][2] = z_axis[1]
        rotation[2][2] = z_axis[2]

        return rotation * translation


class ChunkManager:
    def __init__(self, chunk_i, app, pos):
        self.chunk_i = chunk_i
        self.app = app
        self.pos = pos

    def chunk_init(self):
        px, py, pz = self.pos
        self.app.vao_3d_dict["textures/blocks/bedrock.png"].vao_update(
            self.app.vao_3d_dict["textures/blocks/bedrock.png"].instances.tolist() + [
                [x, y, z] for x in range(px, px + 16) for y in range(-1, 0) for z in range(pz, pz + 16)
            ])
        self.app.vao_3d_dict["textures/blocks/stone.png"].vao_update(
            self.app.vao_3d_dict["textures/blocks/stone.png"].instances.tolist() + [
                [x, y, z] for x in range(px, px + 16) for y in range(0, 26) for z in range(pz, pz + 16)
            ])
        self.app.vao_3d_dict["textures/blocks/dirt.png"].vao_update(
            self.app.vao_3d_dict["textures/blocks/dirt.png"].instances.tolist() + [
                [x, y, z] for x in range(px, px + 16) for y in range(26, 31) for z in range(pz, pz + 16)
            ])
        self.app.vao_3d_dict["textures/blocks/grass_top.png"].vao_update(
            self.app.vao_3d_dict["textures/blocks/grass_top.png"].instances.tolist() + [
                [x, y, z] for x in range(px, px + 16) for y in range(31, 32) for z in range(pz, pz + 16)
            ])


class VAOManager:
    def __init__(self, vbo_data, ebo_data, ebo_edge_data, texture_dir, block_instances):
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)

        self.data_vbo = glGenBuffers(1)
        self.vbo_data = vbo_data
        glBindBuffer(GL_ARRAY_BUFFER, self.data_vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vbo_data.itemsize * len(self.vbo_data), self.vbo_data, GL_STATIC_DRAW)

        self.ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, ebo_data.itemsize * len(ebo_data), ebo_data, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.vbo_data.itemsize * 5, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, self.vbo_data.itemsize * 5, ctypes.c_void_p(12))
        glEnableVertexAttribArray(1)

        self.ebo_edge = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo_edge)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, ebo_edge_data.itemsize * len(ebo_edge_data),
                     ebo_edge_data, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.vbo_data.itemsize * 5, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(3, 2, GL_FLOAT, GL_FALSE, self.vbo_data.itemsize * 5, ctypes.c_void_p(12))
        glEnableVertexAttribArray(3)

        if isinstance(texture_dir, str):
            self.texture_name = texture_dir
            self.texture = App.load_texture(texture_dir)
        else:
            self.texture_name = texture_dir[0]
            self.texture = App.load_texture(texture_dir)
        self.instance_vbo = glGenBuffers(1)
        self.highlighted_vbo = glGenBuffers(1)
        self.instances = numpy.array(block_instances, dtype=numpy.float32)
        glBindBuffer(GL_ARRAY_BUFFER, self.instance_vbo)
        glBufferData(GL_ARRAY_BUFFER, self.instances.flatten().itemsize * len(self.instances.flatten()),
                     self.instances.flatten(), GL_STATIC_DRAW)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        glEnableVertexAttribArray(2)
        glVertexAttribDivisor(2, 1)
        glBindVertexArray(0)

    def vao_update(self, instances=None):
        if instances is not None:
            self.instances = numpy.array(instances, dtype=numpy.float32)
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, self.instance_vbo)
        glBufferData(GL_ARRAY_BUFFER, self.instances.flatten().itemsize *
                     len(self.instances.flatten()), self.instances.flatten(), GL_STATIC_DRAW)
        glBindVertexArray(0)


class TextManager:
    def __init__(self, app, character_size, ascii_type=ASCII_PNG):
        self.app = app
        self.character_size = character_size
        character = numpy.array([0.0, 0.0, 0.0, 0.0, 0.0,
                                 0.0, 8.0 * character_size, 0.0, 0.0, 1.0,
                                 8.0 * character_size, 8.0 * character_size, 0.0, 1.0, 1.0,
                                 8.0 * character_size, 0.0, 0.0, 1.0, 0.0], dtype=numpy.float32)
        self.app.vao_2d_dict[f"character_{self.character_size}_ "] = VAOManager(
            character, QUAD_INDICES, QUAD_INDICES, (ascii_type, (0, 16), (8, 8)), []
        )
        for char in CHARACTER_DICT:
            character = numpy.array([0.0, 0.0, 0.0, 0.0, 0.0,
                                     0.0, 8.0 * character_size, 0.0, 0.0, 1.0,
                                     CHARACTER_DICT[char][0][1][0] * character_size,
                                     8.0 * character_size, 0.0, 1.0, 1.0,
                                     CHARACTER_DICT[char][0][1][0] * character_size, 0.0, 0.0, 1.0, 0.0],
                                    dtype=numpy.float32)
            self.app.vao_2d_dict[f"character_{self.character_size}_{char}"] = VAOManager(
                character, QUAD_INDICES, QUAD_INDICES, (ascii_type, *CHARACTER_DICT[char][0]), []
            )
            character = numpy.array([0.0, 0.0, 0.0, 0.0, 0.0,
                                     0.0, 8.0 * character_size, 0.0, 0.0, 1.0,
                                     CHARACTER_DICT[char][1][1][0] * character_size,
                                     8.0 * character_size, 0.0, 1.0, 1.0,
                                     CHARACTER_DICT[char][1][1][0] * character_size, 0.0, 0.0, 1.0, 0.0],
                                    dtype=numpy.float32)
            self.app.vao_2d_dict[f"character_{self.character_size}_{char.upper()}"] = VAOManager(
                character, QUAD_INDICES, QUAD_INDICES, (ascii_type, *CHARACTER_DICT[char][1]), []
            )
        for char in SPECIAL_CHARACTER_DICT:
            character = numpy.array([0.0, 0.0, 0.0, 0.0, 0.0,
                                     0.0, 8.0 * character_size, 0.0, 0.0, 1.0,
                                     SPECIAL_CHARACTER_DICT[char][1][0] * character_size,
                                     8.0 * character_size, 0.0, 1.0, 1.0,
                                     SPECIAL_CHARACTER_DICT[char][1][0] * character_size, 0.0, 0.0, 1.0, 0.0],
                                    dtype=numpy.float32)
            self.app.vao_2d_dict[f"character_{self.character_size}_{char}"] = VAOManager(
                character, QUAD_INDICES, QUAD_INDICES, (ascii_type, *SPECIAL_CHARACTER_DICT[char]), []
            )

    def add_text(self, text, pos):
        for character in text:
            self.app.vao_2d_dict[f"character_{self.character_size}_{character}"].vao_update(
                self.app.vao_2d_dict[f"character_{self.character_size}_{character}"].instances.tolist() + [pos]
            )
            if character in CHARACTER_DICT:
                pos[0] += self.character_size * (CHARACTER_DICT[character][0][1][0] + 1)
            elif character.lower() in CHARACTER_DICT:
                pos[0] += self.character_size * (CHARACTER_DICT[character.lower()][1][1][0] + 1)
            elif character in SPECIAL_CHARACTER_DICT:
                pos[0] += self.character_size * (SPECIAL_CHARACTER_DICT[character][1][0] + 1)
            else:
                pos[0] += self.character_size * 5

    def remove_text(self, text, pos):
        for character in text:
            self.app.vao_2d_dict[f"character_{self.character_size}_{character}"].instances = numpy.delete(
                self.app.vao_2d_dict[f"character_{self.character_size}_{character}"].instances,
                numpy.where(
                    (self.app.vao_2d_dict[f"character_{self.character_size}_{character}"].instances[:, 0] == pos[0]) &
                    (self.app.vao_2d_dict[f"character_{self.character_size}_{character}"].instances[:, 1] == pos[1]) &
                    (self.app.vao_2d_dict[f"character_{self.character_size}_{character}"].instances[:, 2] == pos[2])
                ), 0
            )
            self.app.vao_2d_dict[f"character_{self.character_size}_{character}"].vao_update()
            if character in CHARACTER_DICT:
                pos[0] += self.character_size * (CHARACTER_DICT[character][0][1][0] + 1)
            elif character.lower() in CHARACTER_DICT:
                pos[0] += self.character_size * (CHARACTER_DICT[character.lower()][1][1][0] + 1)
            elif character in SPECIAL_CHARACTER_DICT:
                pos[0] += self.character_size * (SPECIAL_CHARACTER_DICT[character][1][0] + 1)
            else:
                pos[0] += self.character_size * 5

    def clear(self):
        for char in CHARACTER_DICT:
            if len(self.app.vao_2d_dict[f"character_{self.character_size}_{char}"].instances) > 0:
                self.app.vao_2d_dict[f"character_{self.character_size}_{char}"].vao_update([])
            if len(self.app.vao_2d_dict[f"character_{self.character_size}_{char.upper()}"].instances) > 0:
                self.app.vao_2d_dict[f"character_{self.character_size}_{char.upper()}"].vao_update([])
        for char in SPECIAL_CHARACTER_DICT:
            if len(self.app.vao_2d_dict[f"character_{self.character_size}_{char}"].instances) > 0:
                self.app.vao_2d_dict[f"character_{self.character_size}_{char}"].vao_update([])


if __name__ == '__main__':
    App(1280, 720)
