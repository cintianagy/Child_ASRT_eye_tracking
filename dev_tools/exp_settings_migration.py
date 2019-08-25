# !/usr/bin/env python
# -*- coding: utf-8 -*-

#    ASRT script in Psychopy
#    Copyright (C) <2019>  <Tamás Zolnai>  <zolnaitamas2000@gmail.com>

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import shelve


def do_changes(settings_file):
    settings_file['experiment_type'] = 'reaction-time'


def migrate_setting_file(settings_path):

    settings_list = []

    try:
        with shelve.open(settings_path, "w") as settings_file:
            do_changes(settings_file)

    except Exception as exception:
        print('Excpetion raised while working on the settings file:\n' + settings_path)
        print(exception)
        return


def migrate_recursively(root_dir):
    for file in os.listdir(root_dir):
        file_path = os.path.join(root_dir, file)
        if os.path.isfile(file_path) and file == "settings.dat":
            migrate_setting_file(os.path.join(root_dir, "settings"))
        elif os.path.isdir(file_path):
            migrate_recursively(file_path)


if __name__ == "__main__":
    root_dir = os.path.split(os.path.abspath(__file__))[0]
    (root_dir, trail) = os.path.split(root_dir)
    migrate_recursively(root_dir)