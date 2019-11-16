# !/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright (C) <2019>  <Tamás Zolnai>    <zolnaitamas2000@gmail.com>

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

import unittest
import os

if __name__ == "__main__":
    os.system('pytest all_settings_def_test.py')
    os.system('pytest calculate_stim_properties_test.py')
    os.system('pytest coordinate_test.py')
    os.system('pytest draw_instructions_test.py')
    os.system('pytest experiment_settings_file_handling_test.py')
    os.system('pytest eye_tracking_timing_test.py')
    os.system('pytest participant_id_test.py')
    #os.system('pytest integration_test.py')
    os.system('pytest person_data_handler_test.py')
    os.system('pytest presentation_test.py')
    os.system('pytest read_instructions_test.py')
    os.system('pytest show_basic_settings_dialog_test.py')
    os.system('pytest show_computer_and_display_settings_dialog_test.py')
    os.system('pytest show_epoch_and_block_settings_dialog_test.py')
    os.system('pytest show_feedback_test.py')
    os.system('pytest show_key_and_feedback_settings_dialog_test.py')
    os.system('pytest show_subject_attributes_dialog_test.py')
    os.system('pytest show_subject_continuation_dialog_test.py')
    os.system('pytest show_subject_identification_dialog_test.py')
    os.system('pytest which_code_test.py')